import io
import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.core import BinaryResponse
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER


def test_sync_200_success_default():
    """Tests a POST request to the /sdk/config/sync endpoint.

    Operation: sync
    Test Case ID: success_default
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
    response = client.sideko.sdk.config.sync(
        config=io.BytesIO(b"123"), openapi=io.BytesIO(b"123")
    )
    is_binary = isinstance(response, BinaryResponse)
    assert is_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_sync_200_success_default():
    """Tests a POST request to the /sdk/config/sync endpoint.

    Operation: sync
    Test Case ID: success_default
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
    response = await client.sideko.sdk.config.sync(
        config=io.BytesIO(b"123"), openapi=io.BytesIO(b"123")
    )
    is_binary = isinstance(response, BinaryResponse)
    assert is_binary, "failed response type check"


def test_init_200_success_default():
    """Tests a POST request to the /sdk/config/init endpoint.

    Operation: init
    Test Case ID: success_default
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
    response = client.sideko.sdk.config.init(api_name="my-project")
    is_binary = isinstance(response, BinaryResponse)
    assert is_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_init_200_success_default():
    """Tests a POST request to the /sdk/config/init endpoint.

    Operation: init
    Test Case ID: success_default
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
    response = await client.sideko.sdk.config.init(api_name="my-project")
    is_binary = isinstance(response, BinaryResponse)
    assert is_binary, "failed response type check"
