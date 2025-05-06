import pydantic
import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER
from sideko_kong_sdk_docs.types import models


def test_patch_200_success_example_1():
    """Tests a PATCH request to the /portals/{portalId}/authentication-settings endpoint.

    Operation: patch
    Test Case ID: success_example_1
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalAuthenticationSettingsResponse

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
    response = client.kong_portal.portals.authentication_settings.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        basic_auth_enabled=True,
        idp_mapping_enabled=True,
        konnect_mapping_enabled=False,
        oidc_auth_enabled=True,
        oidc_claim_mappings={
            "email": "email",
            "groups": "custom-group-claim",
            "name": "name",
        },
        oidc_client_id="x7id0o42lklas0blidl2",
        oidc_issuer="https://identity.example.com/v2",
        oidc_scopes=["email", "openid", "profile"],
        oidc_team_mapping_enabled=True,
        saml_auth_enabled=True,
    )
    try:
        pydantic.TypeAdapter(
            models.PortalAuthenticationSettingsResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_example_1():
    """Tests a PATCH request to the /portals/{portalId}/authentication-settings endpoint.

    Operation: patch
    Test Case ID: success_example_1
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalAuthenticationSettingsResponse

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
    response = await client.kong_portal.portals.authentication_settings.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        basic_auth_enabled=True,
        idp_mapping_enabled=True,
        konnect_mapping_enabled=False,
        oidc_auth_enabled=True,
        oidc_claim_mappings={
            "email": "email",
            "groups": "custom-group-claim",
            "name": "name",
        },
        oidc_client_id="x7id0o42lklas0blidl2",
        oidc_issuer="https://identity.example.com/v2",
        oidc_scopes=["email", "openid", "profile"],
        oidc_team_mapping_enabled=True,
        saml_auth_enabled=True,
    )
    try:
        pydantic.TypeAdapter(
            models.PortalAuthenticationSettingsResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_enable_oidc_team_mapping():
    """Tests a PATCH request to the /portals/{portalId}/authentication-settings endpoint.

    Operation: patch
    Test Case ID: success_enable_oidc_team_mapping
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalAuthenticationSettingsResponse

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
    response = client.kong_portal.portals.authentication_settings.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        basic_auth_enabled=True,
        idp_mapping_enabled=True,
        konnect_mapping_enabled=True,
        oidc_auth_enabled=False,
        oidc_claim_mappings={
            "email": "email",
            "groups": "custom-group-claim",
            "name": "name",
        },
        oidc_team_mapping_enabled=True,
        saml_auth_enabled=False,
    )
    try:
        pydantic.TypeAdapter(
            models.PortalAuthenticationSettingsResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_enable_oidc_team_mapping():
    """Tests a PATCH request to the /portals/{portalId}/authentication-settings endpoint.

    Operation: patch
    Test Case ID: success_enable_oidc_team_mapping
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalAuthenticationSettingsResponse

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
    response = await client.kong_portal.portals.authentication_settings.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        basic_auth_enabled=True,
        idp_mapping_enabled=True,
        konnect_mapping_enabled=True,
        oidc_auth_enabled=False,
        oidc_claim_mappings={
            "email": "email",
            "groups": "custom-group-claim",
            "name": "name",
        },
        oidc_team_mapping_enabled=True,
        saml_auth_enabled=False,
    )
    try:
        pydantic.TypeAdapter(
            models.PortalAuthenticationSettingsResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_enable_oidc_developer_auth():
    """Tests a PATCH request to the /portals/{portalId}/authentication-settings endpoint.

    Operation: patch
    Test Case ID: success_enable_oidc_developer_auth
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalAuthenticationSettingsResponse

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
    response = client.kong_portal.portals.authentication_settings.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        basic_auth_enabled=True,
        idp_mapping_enabled=True,
        konnect_mapping_enabled=True,
        oidc_auth_enabled=True,
        oidc_claim_mappings={
            "email": "email",
            "groups": "custom-group-claim",
            "name": "name",
        },
        oidc_client_id="x7id0o42lklas0blidl2",
        oidc_issuer="https://identity.example.com/v2",
        oidc_scopes=["email", "openid", "profile"],
        oidc_team_mapping_enabled=False,
        saml_auth_enabled=False,
    )
    try:
        pydantic.TypeAdapter(
            models.PortalAuthenticationSettingsResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_enable_oidc_developer_auth():
    """Tests a PATCH request to the /portals/{portalId}/authentication-settings endpoint.

    Operation: patch
    Test Case ID: success_enable_oidc_developer_auth
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalAuthenticationSettingsResponse

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
    response = await client.kong_portal.portals.authentication_settings.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        basic_auth_enabled=True,
        idp_mapping_enabled=True,
        konnect_mapping_enabled=True,
        oidc_auth_enabled=True,
        oidc_claim_mappings={
            "email": "email",
            "groups": "custom-group-claim",
            "name": "name",
        },
        oidc_client_id="x7id0o42lklas0blidl2",
        oidc_issuer="https://identity.example.com/v2",
        oidc_scopes=["email", "openid", "profile"],
        oidc_team_mapping_enabled=False,
        saml_auth_enabled=False,
    )
    try:
        pydantic.TypeAdapter(
            models.PortalAuthenticationSettingsResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_patch_200_success_disable_basic_developer_auth():
    """Tests a PATCH request to the /portals/{portalId}/authentication-settings endpoint.

    Operation: patch
    Test Case ID: success_disable_basic_developer_auth
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalAuthenticationSettingsResponse

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
    response = client.kong_portal.portals.authentication_settings.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        basic_auth_enabled=False,
        idp_mapping_enabled=True,
        konnect_mapping_enabled=False,
        oidc_auth_enabled=False,
        oidc_team_mapping_enabled=True,
        saml_auth_enabled=False,
    )
    try:
        pydantic.TypeAdapter(
            models.PortalAuthenticationSettingsResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_disable_basic_developer_auth():
    """Tests a PATCH request to the /portals/{portalId}/authentication-settings endpoint.

    Operation: patch
    Test Case ID: success_disable_basic_developer_auth
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalAuthenticationSettingsResponse

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
    response = await client.kong_portal.portals.authentication_settings.patch(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        basic_auth_enabled=False,
        idp_mapping_enabled=True,
        konnect_mapping_enabled=False,
        oidc_auth_enabled=False,
        oidc_team_mapping_enabled=True,
        saml_auth_enabled=False,
    )
    try:
        pydantic.TypeAdapter(
            models.PortalAuthenticationSettingsResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/authentication-settings endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PortalAuthenticationSettingsResponse

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
    response = client.kong_portal.portals.authentication_settings.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(
            models.PortalAuthenticationSettingsResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /portals/{portalId}/authentication-settings endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PortalAuthenticationSettingsResponse

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
    response = await client.kong_portal.portals.authentication_settings.list(
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(
            models.PortalAuthenticationSettingsResponse
        ).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
