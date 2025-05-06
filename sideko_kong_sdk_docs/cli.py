import argparse
import sys
from pathlib import Path
from enum import Enum
from os import getenv

from sideko_kong_sdk_docs import Client


class SdkLanguage(str, Enum):
    """Supported SDK languages."""

    PYTHON = "python"
    TYPESCRIPT = "typescript"
    JAVA = "java"
    GO = "go"
    RUST = "rust"


def process_kong_api(
    api_spec_id: str,
    api_id: str,
    portal_id: str,
    sdk_docs_path: Path,
    nav_snippet_name: str,
    sdk_language: SdkLanguage,
) -> None:
    """
    Process Kong API specification and generate SDK documentation with Sideko

    Args:
        api_spec_id: Kong API specification ID (triggered with polling or webhook)
        api_id: Kong API ID
        portal_id: Kong portal ID
        sdk_docs_path: Path to the SDK documentation root
        nav_snippet_name: Name of the navigation snippet
        sdk_language: SDK language to generate
    """
    print(f"Processing Kong API with specification ID: {api_spec_id}")
    print(f"API ID: {api_id}")
    print(f"Portal ID: {portal_id}")
    print(f"SDK docs path: {sdk_docs_path}")
    print(f"Navigation snippet name: {nav_snippet_name}")
    print(f"SDK language: {sdk_language}")

    kong_sideko = Client(
        sideko_key=getenv("SIDEKO_API_KEY"), kong_pat=getenv("KONG_PAT")
    )
    spec = kong_sideko.kong_portal.applications


def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Generate SDK documentation from Kong API specifications"
    )

    parser.add_argument(
        "--api-spec-id",
        required=True,
        help="Kong API specification ID (triggered with a polling script or future Kong webhook)",
    )
    parser.add_argument(
        "--api-id",
        required=True,
        help="Kong API ID",
    )
    parser.add_argument(
        "--portal-id",
        required=True,
        help="Kong portal ID",
    )
    parser.add_argument(
        "--sdk-docs-path",
        required=True,
        type=Path,
        help="Path to Kong portal SDK documentation root",
    )
    parser.add_argument(
        "--nav-snippet-name",
        required=True,
        help="Kong portal navigation snippet name",
    )
    parser.add_argument(
        "--sdk-language",
        required=True,
        type=lambda x: SdkLanguage(x),
        choices=list(SdkLanguage),
        help=f"SDK language (one of: {', '.join(e.value for e in SdkLanguage)})",
    )

    args = parser.parse_args()

    process_kong_api(
        api_spec_id=args.api_spec_id,
        api_id=args.api_id,
        portal_id=args.portal_id,
        sdk_docs_path=args.sdk_docs_path,
        nav_snippet_name=args.nav_snippet_name,
        sdk_language=args.sdk_language,
    )


if __name__ == "__main__":
    sys.exit(main())
