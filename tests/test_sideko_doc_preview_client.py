import pydantic
import pytest
import typing

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_create_password_200_success_default():
    """Tests a POST request to the /doc_project/{doc_name}/password endpoint.

    Operation: create_password
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DocPreviewPassword

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
    response = client.sideko.doc.preview.create_password(
        doc_name="my-project", name="My customer preview"
    )
    try:
        pydantic.TypeAdapter(models.DocPreviewPassword).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_password_200_success_default():
    """Tests a POST request to the /doc_project/{doc_name}/password endpoint.

    Operation: create_password
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DocPreviewPassword

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
    response = await client.sideko.doc.preview.create_password(
        doc_name="my-project", name="My customer preview"
    )
    try:
        pydantic.TypeAdapter(models.DocPreviewPassword).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_passwords_200_generated_success():
    """Tests a GET request to the /doc_project/{doc_name}/password endpoint.

    Operation: list_passwords
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.DocPreviewPassword]

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
    response = client.sideko.doc.preview.list_passwords(doc_name="my-project")
    try:
        pydantic.TypeAdapter(typing.List[models.DocPreviewPassword]).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_passwords_200_generated_success():
    """Tests a GET request to the /doc_project/{doc_name}/password endpoint.

    Operation: list_passwords
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.DocPreviewPassword]

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
    response = await client.sideko.doc.preview.list_passwords(doc_name="my-project")
    try:
        pydantic.TypeAdapter(typing.List[models.DocPreviewPassword]).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_password_204_success_default():
    """Tests a DELETE request to the /doc_project/{doc_name}/password endpoint.

    Operation: delete_password
    Test Case ID: success_default
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
    response = client.sideko.doc.preview.delete_password(
        doc_name="my-project", name="My customer preview"
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_password_204_success_default():
    """Tests a DELETE request to the /doc_project/{doc_name}/password endpoint.

    Operation: delete_password
    Test Case ID: success_default
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
    response = await client.sideko.doc.preview.delete_password(
        doc_name="my-project", name="My customer preview"
    )
    assert response is None
