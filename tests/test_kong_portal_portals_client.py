import pydantic
import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_create_201_success_example_1():
    """Tests a POST request to the /portals endpoint.

    Operation: create
    Test Case ID: success_example_1
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.KongPortalPortalsCreateResponse

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
    response = client.kong_portal.portals.create(
        name="MyDevPortal",
        authentication_enabled=True,
        auto_approve_applications=False,
        auto_approve_developers=False,
        rbac_enabled=True,
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsCreateResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_example_1():
    """Tests a POST request to the /portals endpoint.

    Operation: create
    Test Case ID: success_example_1
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.KongPortalPortalsCreateResponse

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
    response = await client.kong_portal.portals.create(
        name="MyDevPortal",
        authentication_enabled=True,
        auto_approve_applications=False,
        auto_approve_developers=False,
        rbac_enabled=True,
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsCreateResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_201_success_enable_rbac():
    """Tests a POST request to the /portals endpoint.

    Operation: create
    Test Case ID: success_enable_rbac
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.KongPortalPortalsCreateResponse

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
    response = client.kong_portal.portals.create(
        name="MyDevPortal", authentication_enabled=True, rbac_enabled=True
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsCreateResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_enable_rbac():
    """Tests a POST request to the /portals endpoint.

    Operation: create
    Test Case ID: success_enable_rbac
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.KongPortalPortalsCreateResponse

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
    response = await client.kong_portal.portals.create(
        name="MyDevPortal", authentication_enabled=True, rbac_enabled=True
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsCreateResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_201_success_auto_approve_settings():
    """Tests a POST request to the /portals endpoint.

    Operation: create
    Test Case ID: success_auto_approve_settings
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.KongPortalPortalsCreateResponse

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
    response = client.kong_portal.portals.create(
        name="MyDevPortal", auto_approve_applications=True, auto_approve_developers=True
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsCreateResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_auto_approve_settings():
    """Tests a POST request to the /portals endpoint.

    Operation: create
    Test Case ID: success_auto_approve_settings
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.KongPortalPortalsCreateResponse

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
    response = await client.kong_portal.portals.create(
        name="MyDevPortal", auto_approve_applications=True, auto_approve_developers=True
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsCreateResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_201_success_authentication_disabled():
    """Tests a POST request to the /portals endpoint.

    Operation: create
    Test Case ID: success_authentication_disabled
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.KongPortalPortalsCreateResponse

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
    response = client.kong_portal.portals.create(
        name="MyDevPortal", authentication_enabled=False
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsCreateResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_authentication_disabled():
    """Tests a POST request to the /portals endpoint.

    Operation: create
    Test Case ID: success_authentication_disabled
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.KongPortalPortalsCreateResponse

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
    response = await client.kong_portal.portals.create(
        name="MyDevPortal", authentication_enabled=False
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsCreateResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_example_1():
    """Tests a PATCH request to the /portals/{portalId} endpoint.

    Operation: patch
    Test Case ID: success_example_1
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.KongPortalPortalsPatchResponse

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
    response = client.kong_portal.portals.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        authentication_enabled=False,
        auto_approve_applications=False,
        auto_approve_developers=False,
        rbac_enabled=False,
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsPatchResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_example_1():
    """Tests a PATCH request to the /portals/{portalId} endpoint.

    Operation: patch
    Test Case ID: success_example_1
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.KongPortalPortalsPatchResponse

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
    response = await client.kong_portal.portals.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        authentication_enabled=False,
        auto_approve_applications=False,
        auto_approve_developers=False,
        rbac_enabled=False,
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsPatchResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_enable_rbac():
    """Tests a PATCH request to the /portals/{portalId} endpoint.

    Operation: patch
    Test Case ID: success_enable_rbac
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.KongPortalPortalsPatchResponse

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
    response = client.kong_portal.portals.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        authentication_enabled=True,
        rbac_enabled=True,
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsPatchResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_enable_rbac():
    """Tests a PATCH request to the /portals/{portalId} endpoint.

    Operation: patch
    Test Case ID: success_enable_rbac
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.KongPortalPortalsPatchResponse

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
    response = await client.kong_portal.portals.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        authentication_enabled=True,
        rbac_enabled=True,
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsPatchResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_auto_approve_settings():
    """Tests a PATCH request to the /portals/{portalId} endpoint.

    Operation: patch
    Test Case ID: success_auto_approve_settings
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.KongPortalPortalsPatchResponse

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
    response = client.kong_portal.portals.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        auto_approve_applications=True,
        auto_approve_developers=True,
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsPatchResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_auto_approve_settings():
    """Tests a PATCH request to the /portals/{portalId} endpoint.

    Operation: patch
    Test Case ID: success_auto_approve_settings
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.KongPortalPortalsPatchResponse

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
    response = await client.kong_portal.portals.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        auto_approve_applications=True,
        auto_approve_developers=True,
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsPatchResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_authentication_disabled():
    """Tests a PATCH request to the /portals/{portalId} endpoint.

    Operation: patch
    Test Case ID: success_authentication_disabled
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.KongPortalPortalsPatchResponse

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
    response = client.kong_portal.portals.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", authentication_enabled=False
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsPatchResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_authentication_disabled():
    """Tests a PATCH request to the /portals/{portalId} endpoint.

    Operation: patch
    Test Case ID: success_authentication_disabled
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.KongPortalPortalsPatchResponse

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
    response = await client.kong_portal.portals.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", authentication_enabled=False
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsPatchResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /portals/{portalId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.KongPortalPortalsGetResponse

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
    response = client.kong_portal.portals.get(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsGetResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /portals/{portalId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.KongPortalPortalsGetResponse

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
    response = await client.kong_portal.portals.get(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsGetResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /portals endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.KongPortalPortalsListResponse

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
    response = client.kong_portal.portals.list(page_number=1, page_size=10)
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsListResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /portals endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.KongPortalPortalsListResponse

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
    response = await client.kong_portal.portals.list(page_number=1, page_size=10)
    try:
        pydantic.TypeAdapter(models.KongPortalPortalsListResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_204_generated_success():
    """Tests a DELETE request to the /portals/{portalId} endpoint.

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
    response = client.kong_portal.portals.delete(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Tests a DELETE request to the /portals/{portalId} endpoint.

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
    response = await client.kong_portal.portals.delete(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert response is None
