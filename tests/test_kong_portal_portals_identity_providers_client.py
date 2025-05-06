import pydantic
import pytest
import typing

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_create_201_success_saml_identity_provider_request_with_metadata_url():
    """Tests a POST request to the /portals/{portalId}/identity-providers endpoint.

    Operation: create
    Test Case ID: success_saml_identity_provider_request_with_metadata_url
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.IdentityProvider

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
    response = client.kong_portal.portals.identity_providers.create(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        config={
            "client_id": "YOUR_CLIENT_ID",
            "client_secret": "YOUR_CLIENT_SECRET",
            "issuer_url": "https://konghq.okta.com/oauth2/default",
        },
        type_="saml",
    )
    try:
        pydantic.TypeAdapter(models.IdentityProvider).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_saml_identity_provider_request_with_metadata_url():
    """Tests a POST request to the /portals/{portalId}/identity-providers endpoint.

    Operation: create
    Test Case ID: success_saml_identity_provider_request_with_metadata_url
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.IdentityProvider

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
    response = await client.kong_portal.portals.identity_providers.create(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        config={
            "client_id": "YOUR_CLIENT_ID",
            "client_secret": "YOUR_CLIENT_SECRET",
            "issuer_url": "https://konghq.okta.com/oauth2/default",
        },
        type_="saml",
    )
    try:
        pydantic.TypeAdapter(models.IdentityProvider).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_201_success_saml_identity_provider_request_with_metadata():
    """Tests a POST request to the /portals/{portalId}/identity-providers endpoint.

    Operation: create
    Test Case ID: success_saml_identity_provider_request_with_metadata
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.IdentityProvider

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
    response = client.kong_portal.portals.identity_providers.create(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        config={
            "client_id": "YOUR_CLIENT_ID",
            "client_secret": "YOUR_CLIENT_SECRET",
            "issuer_url": "https://konghq.okta.com/oauth2/default",
        },
        type_="saml",
    )
    try:
        pydantic.TypeAdapter(models.IdentityProvider).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_saml_identity_provider_request_with_metadata():
    """Tests a POST request to the /portals/{portalId}/identity-providers endpoint.

    Operation: create
    Test Case ID: success_saml_identity_provider_request_with_metadata
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.IdentityProvider

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
    response = await client.kong_portal.portals.identity_providers.create(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        config={
            "client_id": "YOUR_CLIENT_ID",
            "client_secret": "YOUR_CLIENT_SECRET",
            "issuer_url": "https://konghq.okta.com/oauth2/default",
        },
        type_="saml",
    )
    try:
        pydantic.TypeAdapter(models.IdentityProvider).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_201_success_oidc_identity_provider_request():
    """Tests a POST request to the /portals/{portalId}/identity-providers endpoint.

    Operation: create
    Test Case ID: success_oidc_identity_provider_request
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.IdentityProvider

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
    response = client.kong_portal.portals.identity_providers.create(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        config={
            "client_id": "YOUR_CLIENT_ID",
            "client_secret": "YOUR_CLIENT_SECRET",
            "issuer_url": "https://konghq.okta.com/oauth2/default",
        },
        type_="oidc",
    )
    try:
        pydantic.TypeAdapter(models.IdentityProvider).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_oidc_identity_provider_request():
    """Tests a POST request to the /portals/{portalId}/identity-providers endpoint.

    Operation: create
    Test Case ID: success_oidc_identity_provider_request
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.IdentityProvider

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
    response = await client.kong_portal.portals.identity_providers.create(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        config={
            "client_id": "YOUR_CLIENT_ID",
            "client_secret": "YOUR_CLIENT_SECRET",
            "issuer_url": "https://konghq.okta.com/oauth2/default",
        },
        type_="oidc",
    )
    try:
        pydantic.TypeAdapter(models.IdentityProvider).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_update_saml_identity_provider():
    """Tests a PATCH request to the /portals/{portalId}/identity-providers/{id} endpoint.

    Operation: patch
    Test Case ID: success_update_saml_identity_provider
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IdentityProvider

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
    response = client.kong_portal.portals.identity_providers.patch(
        id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        config={
            "client_id": "YOUR_CLIENT_ID",
            "client_secret": "YOUR_CLIENT_SECRET",
            "issuer_url": "https://konghq.okta.com/oauth2/default",
        },
        enabled=True,
    )
    try:
        pydantic.TypeAdapter(models.IdentityProvider).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_update_saml_identity_provider():
    """Tests a PATCH request to the /portals/{portalId}/identity-providers/{id} endpoint.

    Operation: patch
    Test Case ID: success_update_saml_identity_provider
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IdentityProvider

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
    response = await client.kong_portal.portals.identity_providers.patch(
        id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        config={
            "client_id": "YOUR_CLIENT_ID",
            "client_secret": "YOUR_CLIENT_SECRET",
            "issuer_url": "https://konghq.okta.com/oauth2/default",
        },
        enabled=True,
    )
    try:
        pydantic.TypeAdapter(models.IdentityProvider).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_update_oidc_identity_provider():
    """Tests a PATCH request to the /portals/{portalId}/identity-providers/{id} endpoint.

    Operation: patch
    Test Case ID: success_update_oidc_identity_provider
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IdentityProvider

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
    response = client.kong_portal.portals.identity_providers.patch(
        id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        config={
            "client_id": "YOUR_CLIENT_ID",
            "client_secret": "YOUR_CLIENT_SECRET",
            "issuer_url": "https://konghq.okta.com/oauth2/default",
        },
        enabled=True,
    )
    try:
        pydantic.TypeAdapter(models.IdentityProvider).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_update_oidc_identity_provider():
    """Tests a PATCH request to the /portals/{portalId}/identity-providers/{id} endpoint.

    Operation: patch
    Test Case ID: success_update_oidc_identity_provider
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IdentityProvider

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
    response = await client.kong_portal.portals.identity_providers.patch(
        id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        config={
            "client_id": "YOUR_CLIENT_ID",
            "client_secret": "YOUR_CLIENT_SECRET",
            "issuer_url": "https://konghq.okta.com/oauth2/default",
        },
        enabled=True,
    )
    try:
        pydantic.TypeAdapter(models.IdentityProvider).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/identity-providers/{id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.IdentityProvider

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
    response = client.kong_portal.portals.identity_providers.get(
        id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.IdentityProvider).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/identity-providers/{id} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.IdentityProvider

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
    response = await client.kong_portal.portals.identity_providers.get(
        id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.IdentityProvider).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/identity-providers endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.IdentityProvider]

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
    response = client.kong_portal.portals.identity_providers.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(typing.List[models.IdentityProvider]).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/identity-providers endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.IdentityProvider]

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
    response = await client.kong_portal.portals.identity_providers.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(typing.List[models.IdentityProvider]).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_204_generated_success():
    """Tests a DELETE request to the /portals/{portalId}/identity-providers/{id} endpoint.

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
    response = client.kong_portal.portals.identity_providers.delete(
        id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Tests a DELETE request to the /portals/{portalId}/identity-providers/{id} endpoint.

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
    response = await client.kong_portal.portals.identity_providers.delete(
        id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    assert response is None
