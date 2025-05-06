import pydantic
import pytest
import typing

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_create_200_success_default():
    """Tests a POST request to the /service_account endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.UserApiKey

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
    response = client.sideko.service_account.create(
        name="Documentation Publisher Service Account",
        object_roles=[
            {
                "object_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "object_type": "api_project",
                "role_definition_id": "ApiProjectAdmin",
            }
        ],
        expiration="2025-01-01T00:00:00",
    )
    try:
        pydantic.TypeAdapter(models.UserApiKey).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /service_account endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.UserApiKey

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
    response = await client.sideko.service_account.create(
        name="Documentation Publisher Service Account",
        object_roles=[
            {
                "object_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "object_type": "api_project",
                "role_definition_id": "ApiProjectAdmin",
            }
        ],
        expiration="2025-01-01T00:00:00",
    )
    try:
        pydantic.TypeAdapter(models.UserApiKey).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /service_account/{id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.User

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
    response = client.sideko.service_account.get(
        id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /service_account/{id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.User

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
    response = await client.sideko.service_account.get(
        id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /service_account endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.User]

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
    response = client.sideko.service_account.list()
    try:
        pydantic.TypeAdapter(typing.List[models.User]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /service_account endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.User]

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
    response = await client.sideko.service_account.list()
    try:
        pydantic.TypeAdapter(typing.List[models.User]).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_204_generated_success():
    """Tests a DELETE request to the /service_account/{id} endpoint.

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
    response = client.sideko.service_account.delete(
        id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Tests a DELETE request to the /service_account/{id} endpoint.

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
    response = await client.sideko.service_account.delete(
        id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert response is None
