import io
import pydantic
import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_run_200_success_default():
    """Tests a POST request to the /lint endpoint.

    Operation: run
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.LintReport

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
    response = client.sideko.lint.run(api_name="my-project", openapi=io.BytesIO(b"123"))
    try:
        pydantic.TypeAdapter(models.LintReport).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_run_200_success_default():
    """Tests a POST request to the /lint endpoint.

    Operation: run
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.LintReport

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
    response = await client.sideko.lint.run(
        api_name="my-project", openapi=io.BytesIO(b"123")
    )
    try:
        pydantic.TypeAdapter(models.LintReport).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
