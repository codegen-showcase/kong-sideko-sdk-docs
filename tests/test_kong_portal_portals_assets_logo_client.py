import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.core import BinaryResponse
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER


def test_update_200_success_example_1():
    """Tests a PUT request to the /portals/{portalId}/assets/logo endpoint.

    Operation: update
    Test Case ID: success_example_1
    Expected Status: 200
    Mode: Synchronous execution

    Response : BinaryResponse

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
    response = client.kong_portal.portals.assets.logo.update(
        data="data:image/png;base64,bmljZV9sb29raW5nX3BpY3R1cmU=",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        filename="logo.png",
    )
    is_binary = isinstance(response, BinaryResponse)
    assert is_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_example_1():
    """Tests a PUT request to the /portals/{portalId}/assets/logo endpoint.

    Operation: update
    Test Case ID: success_example_1
    Expected Status: 200
    Mode: Asynchronous execution

    Response : BinaryResponse

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
    response = await client.kong_portal.portals.assets.logo.update(
        data="data:image/png;base64,bmljZV9sb29raW5nX3BpY3R1cmU=",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        filename="logo.png",
    )
    is_binary = isinstance(response, BinaryResponse)
    assert is_binary, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/assets/logo endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : BinaryResponse

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
    response = client.kong_portal.portals.assets.logo.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    is_binary = isinstance(response, BinaryResponse)
    assert is_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/assets/logo endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : BinaryResponse

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
    response = await client.kong_portal.portals.assets.logo.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    is_binary = isinstance(response, BinaryResponse)
    assert is_binary, "failed response type check"
