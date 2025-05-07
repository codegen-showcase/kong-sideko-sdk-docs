import argparse
import sys

from sideko_kong_sdk_docs import Client


def check_for_new_openapi_specs_and_sync(sideko_key: str, kong_pat: str, api_id: str):
    kong_sideko = Client(sideko_key=sideko_key, kong_pat=kong_pat)

    # TODO add flow for listening for updates to specs in Kong
    api_spec_id = "123"

    # download spec from kong
    new_oas = kong_sideko.kong_portal.get_spec(
        api_id=api_id, spec_id=api_spec_id
    ).content.encode("utf-8")

    # Upload spec to Sideko
    kong_sideko.sideko.api.spec.create(
        api_name=f"kong-integration-{api_id}",
        openapi=new_oas,
        version="patch",
        mock_server_enabled=True,
        notes="uploaded via the **kong** sdk docs integration",
    )

    # Trigger Sideko SDK Update Flow
    # kong_sideko.sideko.sdk.update()


def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Sync SDK with latest Kong API specifications"
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
        "--api-id",
        required=True,
        help="Kong API ID",
    )
    args = parser.parse_args()

    check_for_new_openapi_specs_and_sync(
        sideko_key=args.sideko_key, kong_pat=args.kong_pat, api_id=args.api_id
    )


if __name__ == "__main__":
    sys.exit(main())  # type: ignore
