from sideko_kong_sdk_docs import Client

"""
Sample for syncing API Specs Flow
"""


def sync_apis(sideko_key: str, kong_pat: str, api_id: str, api_spec_id: str):
    kong_sideko = Client(sideko_key=sideko_key, kong_pat=kong_pat)

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
