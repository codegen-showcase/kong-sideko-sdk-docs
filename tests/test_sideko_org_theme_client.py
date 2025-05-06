import pydantic
import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_update_200_success_default():
    """Tests a PUT request to the /organization/theme endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Theme

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
    response = client.sideko.org.theme.update(
        api_reference_group_variant="grouped",
        dark_active_button_bg_color="#FFFFFF",
        dark_active_button_text_color="#FFFFFF",
        dark_bg_color="#FFFFFF",
        dark_navbar_color="#FFFFFF",
        dark_navbar_text_color="#FFFFFF",
        light_active_button_bg_color="#FFFFFF",
        light_active_button_text_color="#FFFFFF",
        light_bg_color="#FFFFFF",
        light_navbar_color="#FFFFFF",
        light_navbar_text_color="#FFFFFF",
    )
    try:
        pydantic.TypeAdapter(models.Theme).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_default():
    """Tests a PUT request to the /organization/theme endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Theme

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
    response = await client.sideko.org.theme.update(
        api_reference_group_variant="grouped",
        dark_active_button_bg_color="#FFFFFF",
        dark_active_button_text_color="#FFFFFF",
        dark_bg_color="#FFFFFF",
        dark_navbar_color="#FFFFFF",
        dark_navbar_text_color="#FFFFFF",
        light_active_button_bg_color="#FFFFFF",
        light_active_button_text_color="#FFFFFF",
        light_bg_color="#FFFFFF",
        light_navbar_color="#FFFFFF",
        light_navbar_text_color="#FFFFFF",
    )
    try:
        pydantic.TypeAdapter(models.Theme).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /organization/theme endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Theme

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
    response = client.sideko.org.theme.get()
    try:
        pydantic.TypeAdapter(models.Theme).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /organization/theme endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Theme

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
    response = await client.sideko.org.theme.get()
    try:
        pydantic.TypeAdapter(models.Theme).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
