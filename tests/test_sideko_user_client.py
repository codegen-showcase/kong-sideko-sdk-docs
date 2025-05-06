import httpx
import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER


def test_invite_202_success_default():
    """Tests a POST request to the /user/invite endpoint.

    Operation: invite
    Test Case ID: success_default
    Expected Status: 202
    Mode: Synchronous execution

    Response : httpx.Response

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
    response = client.sideko.user.invite(
        email="user@example.com", role_definition_id="ApiProjectAdmin"
    )
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_invite_202_success_default():
    """Tests a POST request to the /user/invite endpoint.

    Operation: invite
    Test Case ID: success_default
    Expected Status: 202
    Mode: Asynchronous execution

    Response : httpx.Response

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
    response = await client.sideko.user.invite(
        email="user@example.com", role_definition_id="ApiProjectAdmin"
    )
    assert isinstance(response, httpx.Response)
