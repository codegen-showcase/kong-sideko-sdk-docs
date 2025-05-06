import pydantic
import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_create_201_success_api_viewer():
    """Tests a POST request to the /portals/{portalId}/teams/{teamId}/assigned-roles endpoint.

    Operation: create
    Test Case ID: success_api_viewer
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.PortalAssignedRoleResponse

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
    response = client.kong_portal.portals.teams.assigned_roles.create(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        entity_id="18ee2573-dec0-4b83-be99-fa7700bcdc61",
        entity_region="us",
        entity_type_name="Services",
        page_number=1,
        page_size=10,
        role_name="API Viewer",
    )
    try:
        pydantic.TypeAdapter(models.PortalAssignedRoleResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_api_viewer():
    """Tests a POST request to the /portals/{portalId}/teams/{teamId}/assigned-roles endpoint.

    Operation: create
    Test Case ID: success_api_viewer
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.PortalAssignedRoleResponse

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
    response = await client.kong_portal.portals.teams.assigned_roles.create(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        entity_id="18ee2573-dec0-4b83-be99-fa7700bcdc61",
        entity_region="us",
        entity_type_name="Services",
        page_number=1,
        page_size=10,
        role_name="API Viewer",
    )
    try:
        pydantic.TypeAdapter(models.PortalAssignedRoleResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_201_success_api_consumer():
    """Tests a POST request to the /portals/{portalId}/teams/{teamId}/assigned-roles endpoint.

    Operation: create
    Test Case ID: success_api_consumer
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.PortalAssignedRoleResponse

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
    response = client.kong_portal.portals.teams.assigned_roles.create(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        entity_id="18ee2573-dec0-4b83-be99-fa7700bcdc61",
        entity_region="us",
        entity_type_name="Services",
        page_number=1,
        page_size=10,
        role_name="API Consumer",
    )
    try:
        pydantic.TypeAdapter(models.PortalAssignedRoleResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_api_consumer():
    """Tests a POST request to the /portals/{portalId}/teams/{teamId}/assigned-roles endpoint.

    Operation: create
    Test Case ID: success_api_consumer
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.PortalAssignedRoleResponse

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
    response = await client.kong_portal.portals.teams.assigned_roles.create(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        entity_id="18ee2573-dec0-4b83-be99-fa7700bcdc61",
        entity_region="us",
        entity_type_name="Services",
        page_number=1,
        page_size=10,
        role_name="API Consumer",
    )
    try:
        pydantic.TypeAdapter(models.PortalAssignedRoleResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/teams/{teamId}/assigned-roles endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.AssignedPortalRoleCollectionResponse

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
    response = client.kong_portal.portals.teams.assigned_roles.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        page_number=1,
        page_size=10,
    )
    try:
        pydantic.TypeAdapter(
            models.AssignedPortalRoleCollectionResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/teams/{teamId}/assigned-roles endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.AssignedPortalRoleCollectionResponse

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
    response = await client.kong_portal.portals.teams.assigned_roles.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        page_number=1,
        page_size=10,
    )
    try:
        pydantic.TypeAdapter(
            models.AssignedPortalRoleCollectionResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_204_generated_success():
    """Tests a DELETE request to the /portals/{portalId}/teams/{teamId}/assigned-roles/{roleId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 204
    Mode: Synchronous execution

    Empty response expected

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
    response = client.kong_portal.portals.teams.assigned_roles.delete(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        role_id="8350205f-a305-4e39-abe9-bc082a80091a",
        team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Tests a DELETE request to the /portals/{portalId}/teams/{teamId}/assigned-roles/{roleId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 204
    Mode: Asynchronous execution

    Empty response expected

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
    response = await client.kong_portal.portals.teams.assigned_roles.delete(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        role_id="8350205f-a305-4e39-abe9-bc082a80091a",
        team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    )
    assert response is None
