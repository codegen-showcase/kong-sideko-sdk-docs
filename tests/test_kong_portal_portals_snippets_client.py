import pydantic
import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_create_201_success_example_1():
    """Tests a POST request to the /portals/{portalId}/snippets endpoint.

    Operation: create
    Test Case ID: success_example_1
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.PortalSnippetResponse

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
    response = client.kong_portal.portals.snippets.create(
        content="Welcome to the Getting Started page. This is where you can learn how to use our APIs.",
        name="getting-started",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        title="Getting Started",
        status="published",
        visibility="public",
    )
    try:
        pydantic.TypeAdapter(models.PortalSnippetResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_example_1():
    """Tests a POST request to the /portals/{portalId}/snippets endpoint.

    Operation: create
    Test Case ID: success_example_1
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.PortalSnippetResponse

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
    response = await client.kong_portal.portals.snippets.create(
        content="Welcome to the Getting Started page. This is where you can learn how to use our APIs.",
        name="getting-started",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        title="Getting Started",
        status="published",
        visibility="public",
    )
    try:
        pydantic.TypeAdapter(models.PortalSnippetResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_example_1():
    """Tests a PATCH request to the /portals/{portalId}/snippets/{snippetId} endpoint.

    Operation: patch
    Test Case ID: success_example_1
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalSnippetResponse

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
    response = client.kong_portal.portals.snippets.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
        content="Welcome to the About Us page. This is where you can learn about our company.",
        name="about-us",
        title="About Us",
    )
    try:
        pydantic.TypeAdapter(models.PortalSnippetResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_example_1():
    """Tests a PATCH request to the /portals/{portalId}/snippets/{snippetId} endpoint.

    Operation: patch
    Test Case ID: success_example_1
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalSnippetResponse

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
    response = await client.kong_portal.portals.snippets.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
        content="Welcome to the About Us page. This is where you can learn about our company.",
        name="about-us",
        title="About Us",
    )
    try:
        pydantic.TypeAdapter(models.PortalSnippetResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/snippets/{snippetId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalSnippetResponse

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
    response = client.kong_portal.portals.snippets.get(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
    )
    try:
        pydantic.TypeAdapter(models.PortalSnippetResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/snippets/{snippetId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalSnippetResponse

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
    response = await client.kong_portal.portals.snippets.get(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
    )
    try:
        pydantic.TypeAdapter(models.PortalSnippetResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/snippets endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ListPortalSnippetsResponse

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
    response = client.kong_portal.portals.snippets.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", page_number=1, page_size=10
    )
    try:
        pydantic.TypeAdapter(models.ListPortalSnippetsResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/snippets endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ListPortalSnippetsResponse

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
    response = await client.kong_portal.portals.snippets.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", page_number=1, page_size=10
    )
    try:
        pydantic.TypeAdapter(models.ListPortalSnippetsResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_204_generated_success():
    """Tests a DELETE request to the /portals/{portalId}/snippets/{snippetId} endpoint.

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
    response = client.kong_portal.portals.snippets.delete(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Tests a DELETE request to the /portals/{portalId}/snippets/{snippetId} endpoint.

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
    response = await client.kong_portal.portals.snippets.delete(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
    )
    assert response is None
