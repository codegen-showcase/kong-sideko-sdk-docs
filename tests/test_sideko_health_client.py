import pydantic
import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_ping_200_generated_success():
    """Tests a GET request to the /_ping endpoint.

    Operation: ping
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.SidekoHealthPingResponse

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
    response = client.sideko.health.ping()
    try:
        pydantic.TypeAdapter(models.SidekoHealthPingResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_ping_200_generated_success():
    """Tests a GET request to the /_ping endpoint.

    Operation: ping
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.SidekoHealthPingResponse

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
    response = await client.sideko.health.ping()
    try:
        pydantic.TypeAdapter(models.SidekoHealthPingResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_check_200_generated_success():
    """Tests a GET request to the /_health endpoint.

    Operation: check
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.SidekoHealthCheckResponse

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
    response = client.sideko.health.check()
    try:
        pydantic.TypeAdapter(models.SidekoHealthCheckResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_check_200_generated_success():
    """Tests a GET request to the /_health endpoint.

    Operation: check
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.SidekoHealthCheckResponse

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
    response = await client.sideko.health.check()
    try:
        pydantic.TypeAdapter(models.SidekoHealthCheckResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
