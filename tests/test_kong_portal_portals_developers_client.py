import pydantic
import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_patch_200_success_revoked():
    """Tests a PATCH request to the /portals/{portalId}/developers/{developerId} endpoint.

    Operation: patch
    Test Case ID: success_revoked
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalDeveloper

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
    response = client.kong_portal.portals.developers.patch(
        developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        status="revoked",
    )
    try:
        pydantic.TypeAdapter(models.PortalDeveloper).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_revoked():
    """Tests a PATCH request to the /portals/{portalId}/developers/{developerId} endpoint.

    Operation: patch
    Test Case ID: success_revoked
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalDeveloper

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
    response = await client.kong_portal.portals.developers.patch(
        developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        status="revoked",
    )
    try:
        pydantic.TypeAdapter(models.PortalDeveloper).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_rejected():
    """Tests a PATCH request to the /portals/{portalId}/developers/{developerId} endpoint.

    Operation: patch
    Test Case ID: success_rejected
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalDeveloper

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
    response = client.kong_portal.portals.developers.patch(
        developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        status="rejected",
    )
    try:
        pydantic.TypeAdapter(models.PortalDeveloper).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_rejected():
    """Tests a PATCH request to the /portals/{portalId}/developers/{developerId} endpoint.

    Operation: patch
    Test Case ID: success_rejected
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalDeveloper

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
    response = await client.kong_portal.portals.developers.patch(
        developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        status="rejected",
    )
    try:
        pydantic.TypeAdapter(models.PortalDeveloper).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_pending():
    """Tests a PATCH request to the /portals/{portalId}/developers/{developerId} endpoint.

    Operation: patch
    Test Case ID: success_pending
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalDeveloper

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
    response = client.kong_portal.portals.developers.patch(
        developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        status="pending",
    )
    try:
        pydantic.TypeAdapter(models.PortalDeveloper).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_pending():
    """Tests a PATCH request to the /portals/{portalId}/developers/{developerId} endpoint.

    Operation: patch
    Test Case ID: success_pending
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalDeveloper

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
    response = await client.kong_portal.portals.developers.patch(
        developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        status="pending",
    )
    try:
        pydantic.TypeAdapter(models.PortalDeveloper).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_approved():
    """Tests a PATCH request to the /portals/{portalId}/developers/{developerId} endpoint.

    Operation: patch
    Test Case ID: success_approved
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalDeveloper

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
    response = client.kong_portal.portals.developers.patch(
        developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        status="approved",
    )
    try:
        pydantic.TypeAdapter(models.PortalDeveloper).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_approved():
    """Tests a PATCH request to the /portals/{portalId}/developers/{developerId} endpoint.

    Operation: patch
    Test Case ID: success_approved
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalDeveloper

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
    response = await client.kong_portal.portals.developers.patch(
        developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        status="approved",
    )
    try:
        pydantic.TypeAdapter(models.PortalDeveloper).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/developers/{developerId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalDeveloper

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
    response = client.kong_portal.portals.developers.get(
        developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.PortalDeveloper).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/developers/{developerId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalDeveloper

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
    response = await client.kong_portal.portals.developers.get(
        developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.PortalDeveloper).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/developers endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ListDevelopersResponse

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
    response = client.kong_portal.portals.developers.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", page_number=1, page_size=10
    )
    try:
        pydantic.TypeAdapter(models.ListDevelopersResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/developers endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ListDevelopersResponse

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
    response = await client.kong_portal.portals.developers.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", page_number=1, page_size=10
    )
    try:
        pydantic.TypeAdapter(models.ListDevelopersResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_204_generated_success():
    """Tests a DELETE request to the /portals/{portalId}/developers/{developerId} endpoint.

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
    response = client.kong_portal.portals.developers.delete(
        developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Tests a DELETE request to the /portals/{portalId}/developers/{developerId} endpoint.

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
    response = await client.kong_portal.portals.developers.delete(
        developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    assert response is None
