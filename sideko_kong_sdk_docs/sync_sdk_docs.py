"""USAGE EXAMPLE
poetry run sync-sdk-docs \
    --sideko-key "xxx"   \
    --kong-pat "xxx"     \
    --portal-id "4f3d97b8-9e41-46f6-b85f-e43630f5375a" \
    --sdk-root-page-slug "/python" \
    --nav-snippet-name "python-sdk-navigation" \
    --sideko-sdk-id "8bc68a39-87b5-46db-b0d3-502d9c70b1ae" \
"""

import argparse
import sys
import typing

from sideko_kong_sdk_docs import Client
from sideko_kong_sdk_docs.types.models import ListPortalPagesResponse


def process_kong_api(
    sideko_key: str,
    kong_pat: str,
    portal_id: str,
    sdk_root_page_slug: str,
    nav_snippet_name: str,
    sideko_sdk_id: str,
) -> None:
    """
    Generate SDK documentation with Sideko and upload the docs to the Kong Portal

    Args:
        sideko_key: Sideko API Key
        kong_pat: Kong API Key
        portal_id: Kong portal ID
        sdk_docs_path: Path to the SDK documentation root
        nav_snippet_name: Name of the navigation snippet
        sdk_language: SDK language to generate
    """
    kong_sideko = Client(sideko_key=sideko_key, kong_pat=kong_pat)

    # Get SDK documentation from Sideko
    sdk_docs = kong_sideko.sideko.sdk.doc.create(sdk_id=sideko_sdk_id)

    # Get all existing portal pages from Kong
    all_pages_response = kong_sideko.kong_portal.portals.pages.list(
        portal_id=portal_id,
    )

    # Function to recursively collect all pages and their children
    def collect_all_pages(pages_list) -> typing.List[ListPortalPagesResponse]:
        all_pages = []

        def process_page(page):
            all_pages.append(page)
            if hasattr(page, "children") and page.children:
                for child in page.children:
                    process_page(child)

        for page in pages_list:
            process_page(page)

        return all_pages

    # Get a flat list of all pages including nested ones
    all_pages = collect_all_pages(all_pages_response.data)

    # Create a mapping of existing pages by slug for quick lookup
    existing_pages = {page.slug: page for page in all_pages}

    # Find the root SDK page in Kong
    root = next((page for page in all_pages if page.slug == sdk_root_page_slug), None)
    if not root:
        raise ValueError(f"Root page with slug {sdk_root_page_slug} not found")

    # Process SDK modules
    for module in sdk_docs.modules:
        # Create slug from module name - using the format we see in existing slugs
        module_slug = module.module.replace(".", "-")
        slug = f"/{module_slug}"

        print(f"Processing module: {module.module}, slug: {slug}")

        # Determine parent page ID
        module_parts = module.module.split(".")
        parent_page_id = root.id

        # Build hierarchy if needed
        for i in range(len(module_parts) - 1):
            parent_parts = module_parts[: i + 1]
            parent_module = ".".join(parent_parts)
            parent_slug = f"/{parent_module.replace('.', '-')}"

            if parent_slug in existing_pages:
                parent_page_id = existing_pages[parent_slug].id
            else:
                parent_page_content = f"""---
title: {module.module}
page-layout:
  sidebar-left: "{nav_snippet_name}"
---

::page-section
---
full-width: true
vertical-align: "center"
padding: "50px"
---

# {parent_module}

{module.content}
::
"""
                try:
                    parent_page = kong_sideko.kong_portal.portals.pages.create(
                        portal_id=portal_id,
                        slug=parent_slug,
                        title=parent_module,
                        parent_page_id=parent_page_id,
                        status="published",
                        visibility="public",
                        content=parent_page_content,
                    )
                    existing_pages[parent_slug] = parent_page
                    parent_page_id = parent_page.id
                    print(f"Created parent page: {parent_slug}")
                except Exception as e:
                    print(f"Failed to create parent page {parent_slug}: {e}")

        page_content = f"""---
title: {module.module}
page-layout:
  sidebar-left: "{nav_snippet_name}"
---

::page-section
---
full-width: true
vertical-align: "center"
padding: "50px"
---

{module.content}

::
"""

        # Check if the page already exists
        if slug in existing_pages:
            # Update existing page - fetch it first to get current data
            page_id = existing_pages[slug].id
            try:
                # Update the page with new content
                kong_sideko.kong_portal.portals.pages.patch(
                    page_id=page_id,
                    portal_id=portal_id,
                    content=page_content,
                    title=module.module,
                    parent_page_id=parent_page_id,
                    status="published",
                    visibility="public",
                    slug=slug,  # Keep the same slug
                )
                print(f"Updated page: {slug}")
            except Exception as e:
                print(f"Failed to update page {slug}: {e}")
                # If update fails, try patch with minimal fields
                try:
                    kong_sideko.kong_portal.portals.pages.patch(
                        page_id=page_id,
                        portal_id=portal_id,
                        content=page_content,
                    )
                    print(f"Patched page: {slug}")
                except Exception as e2:
                    print(f"Failed to patch page {slug}: {e2}")
        else:
            # Create new page
            try:
                new_page = kong_sideko.kong_portal.portals.pages.create(
                    portal_id=portal_id,
                    slug=slug,
                    title=module.module,
                    content=page_content,
                    parent_page_id=parent_page_id,
                    status="published",
                    visibility="public",
                )
                existing_pages[slug] = new_page
                print(f"Created page: {slug}")
            except Exception as e:
                print(f"Failed to create page {slug}: {e}")


def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Generate SDK documentation from Kong API specifications"
    )

    parser.add_argument(
        "--sideko-key",
        required=True,
        help="Sideko API Key",
    )
    parser.add_argument(
        "--kong-pat",
        required=True,
        help="Kong Personal API Token",
    )
    parser.add_argument(
        "--portal-id",
        required=True,
        help="Kong portal ID",
    )
    parser.add_argument(
        "--sdk-root-page-slug",
        required=True,
        help="Kong Portal Page slug of the root for SDK docs",
    )
    parser.add_argument(
        "--nav-snippet-name",
        required=True,
        help="Kong portal navigation snippet name",
    )
    parser.add_argument(
        "--sideko-sdk-id",
        required=True,
        help="Sideko SDK ID",
    )

    args = parser.parse_args()

    process_kong_api(
        sideko_key=args.sideko_key,
        kong_pat=args.kong_pat,
        portal_id=args.portal_id,
        sdk_root_page_slug=args.sdk_root_page_slug,
        nav_snippet_name=args.nav_snippet_name,
        sideko_sdk_id=args.sideko_sdk_id,
    )


if __name__ == "__main__":
    sys.exit(main())
