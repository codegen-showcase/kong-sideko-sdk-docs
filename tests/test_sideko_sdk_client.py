import io
import pydantic
import pytest
import typing

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.core import BinaryResponse
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_update_201_success_default():
    """Tests a POST request to the /sdk/update endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : str

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
    response = client.sideko.sdk.update(
        config=io.BytesIO(b"123"),
        prev_sdk_git=io.BytesIO(b"123"),
        prev_sdk_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        sdk_version="major",
    )
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_text = True
    except pydantic.ValidationError:
        is_text = False
    assert is_text, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_201_success_default():
    """Tests a POST request to the /sdk/update endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : str

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
    response = await client.sideko.sdk.update(
        config=io.BytesIO(b"123"),
        prev_sdk_git=io.BytesIO(b"123"),
        prev_sdk_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        sdk_version="major",
    )
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_text = True
    except pydantic.ValidationError:
        is_text = False
    assert is_text, "failed response type check"


def test_generate_201_success_default():
    """Tests a POST request to the /sdk endpoint.

    Operation: generate
    Test Case ID: success_default
    Expected Status: 201
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
    response = client.sideko.sdk.generate(
        config=io.BytesIO(b"123"), language="go", sdk_version="0.1.0"
    )
    is_binary = isinstance(response, BinaryResponse)
    assert is_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_generate_201_success_default():
    """Tests a POST request to the /sdk endpoint.

    Operation: generate
    Test Case ID: success_default
    Expected Status: 201
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
    response = await client.sideko.sdk.generate(
        config=io.BytesIO(b"123"), language="go", sdk_version="0.1.0"
    )
    is_binary = isinstance(response, BinaryResponse)
    assert is_binary, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /sdk endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.SdkGeneration]

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
    response = client.sideko.sdk.list()
    try:
        pydantic.TypeAdapter(typing.List[models.SdkGeneration]).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /sdk endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.SdkGeneration]

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
    response = await client.sideko.sdk.list()
    try:
        pydantic.TypeAdapter(typing.List[models.SdkGeneration]).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
