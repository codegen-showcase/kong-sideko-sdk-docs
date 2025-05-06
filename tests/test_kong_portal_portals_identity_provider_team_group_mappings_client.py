import pydantic
import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_patch_200_success_example_1():
    """Tests a PATCH request to the /portals/{portalId}/identity-provider/team-group-mappings endpoint.

    Operation: patch
    Test Case ID: success_example_1
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalTeamGroupMappingResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        sideko_key="API_KEY",
        sideko_cookie="API_KEY",
        kong_pat="API_TOKEN",
        kong_sys_token="API_TOKEN",
        environment=SIDEKO_MOCK_SERVER,
    )
    response = client.kong_portal.portals.identity_provider.team_group_mappings.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        data=[
            {
                "groups": ["Service Developer"],
                "team_id": "af91db4c-6e51-403e-a2bf-33d27ae50c0a",
            },
            {
                "groups": ["Service Owner"],
                "team_id": "bc11db4c-6e51-403e-a2bf-33d27ae50c0a",
            },
        ],
    )
    try:
        pydantic.TypeAdapter(models.PortalTeamGroupMappingResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_example_1():
    """Tests a PATCH request to the /portals/{portalId}/identity-provider/team-group-mappings endpoint.

    Operation: patch
    Test Case ID: success_example_1
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalTeamGroupMappingResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        sideko_key="API_KEY",
        sideko_cookie="API_KEY",
        kong_pat="API_TOKEN",
        kong_sys_token="API_TOKEN",
        environment=SIDEKO_MOCK_SERVER,
    )
    response = (
        await client.kong_portal.portals.identity_provider.team_group_mappings.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            data=[
                {
                    "groups": ["Service Developer"],
                    "team_id": "af91db4c-6e51-403e-a2bf-33d27ae50c0a",
                },
                {
                    "groups": ["Service Owner"],
                    "team_id": "bc11db4c-6e51-403e-a2bf-33d27ae50c0a",
                },
            ],
        )
    )
    try:
        pydantic.TypeAdapter(models.PortalTeamGroupMappingResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/identity-provider/team-group-mappings endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalTeamGroupMappingResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        sideko_key="API_KEY",
        sideko_cookie="API_KEY",
        kong_pat="API_TOKEN",
        kong_sys_token="API_TOKEN",
        environment=SIDEKO_MOCK_SERVER,
    )
    response = client.kong_portal.portals.identity_provider.team_group_mappings.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", page_number=1, page_size=10
    )
    try:
        pydantic.TypeAdapter(models.PortalTeamGroupMappingResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/identity-provider/team-group-mappings endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalTeamGroupMappingResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        sideko_key="API_KEY",
        sideko_cookie="API_KEY",
        kong_pat="API_TOKEN",
        kong_sys_token="API_TOKEN",
        environment=SIDEKO_MOCK_SERVER,
    )
    response = (
        await client.kong_portal.portals.identity_provider.team_group_mappings.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            page_number=1,
            page_size=10,
        )
    )
    try:
        pydantic.TypeAdapter(models.PortalTeamGroupMappingResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
