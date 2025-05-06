import typing

from sideko_kong_sdk_docs.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from sideko_kong_sdk_docs.types import models, params


class AuthenticationSettingsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.PortalAuthenticationSettingsResponse:
        """
        Get Auth Settings

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the developer authentication configuration for a portal, which determines how developers can log in and how they are assigned to teams.

        GET /portals/{portalId}/authentication-settings

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a portal's authentication settings.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.authentication_settings.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/authentication-settings",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalAuthenticationSettingsResponse,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        portal_id: str,
        basic_auth_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        idp_mapping_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        konnect_mapping_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_auth_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_claim_mappings: typing.Union[
            typing.Optional[params.PortalClaimMappings], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_client_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_client_secret: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_issuer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_scopes: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_team_mapping_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        saml_auth_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalAuthenticationSettingsResponse:
        """
        Update Auth Settings

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the developer authentication configuration for a portal. Developers can be allowed to login using basic auth (email & password) or use Single-Sign-On (SSO) through an OIDC Identity Provider (IdP). Developers can be automatically assigned to teams by mapping claims from thier IdP account.

        PATCH /portals/{portalId}/authentication-settings

        Args:
            basic_auth_enabled: The organization has basic auth enabled.
            idp_mapping_enabled: Whether IdP groups determine the Konnect Portal teams a developer has. This will soon replace oidc_team_mapping_enabled.
            konnect_mapping_enabled: Whether a Konnect Identity Admin assigns teams to a developer.
            oidc_auth_enabled: The organization has OIDC disabled.
            oidc_claim_mappings: Mappings from a portal developer atribute to an Identity Provider claim.
            oidc_client_id: str
            oidc_client_secret: str
            oidc_issuer: str
            oidc_scopes: typing.List[str]
            oidc_team_mapping_enabled: Whether IdP groups determine the Konnect Portal teams a developer has.
            saml_auth_enabled: The portal has SAML enabled or disabled.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a portal's authentication settings.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.authentication_settings.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            basic_auth_enabled=False,
            idp_mapping_enabled=True,
            konnect_mapping_enabled=False,
            oidc_auth_enabled=False,
            oidc_team_mapping_enabled=True,
            saml_auth_enabled=False,
        )
        ```
        """
        _json = to_encodable(
            item={
                "basic_auth_enabled": basic_auth_enabled,
                "idp_mapping_enabled": idp_mapping_enabled,
                "konnect_mapping_enabled": konnect_mapping_enabled,
                "oidc_auth_enabled": oidc_auth_enabled,
                "oidc_claim_mappings": oidc_claim_mappings,
                "oidc_client_id": oidc_client_id,
                "oidc_client_secret": oidc_client_secret,
                "oidc_issuer": oidc_issuer,
                "oidc_scopes": oidc_scopes,
                "oidc_team_mapping_enabled": oidc_team_mapping_enabled,
                "saml_auth_enabled": saml_auth_enabled,
            },
            dump_with=params._SerializerPortalAuthenticationSettingsUpdateRequest,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/authentication-settings",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalAuthenticationSettingsResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAuthenticationSettingsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.PortalAuthenticationSettingsResponse:
        """
        Get Auth Settings

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the developer authentication configuration for a portal, which determines how developers can log in and how they are assigned to teams.

        GET /portals/{portalId}/authentication-settings

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a portal's authentication settings.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.authentication_settings.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/authentication-settings",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalAuthenticationSettingsResponse,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        portal_id: str,
        basic_auth_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        idp_mapping_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        konnect_mapping_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_auth_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_claim_mappings: typing.Union[
            typing.Optional[params.PortalClaimMappings], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_client_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_client_secret: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_issuer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_scopes: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oidc_team_mapping_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        saml_auth_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalAuthenticationSettingsResponse:
        """
        Update Auth Settings

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the developer authentication configuration for a portal. Developers can be allowed to login using basic auth (email & password) or use Single-Sign-On (SSO) through an OIDC Identity Provider (IdP). Developers can be automatically assigned to teams by mapping claims from thier IdP account.

        PATCH /portals/{portalId}/authentication-settings

        Args:
            basic_auth_enabled: The organization has basic auth enabled.
            idp_mapping_enabled: Whether IdP groups determine the Konnect Portal teams a developer has. This will soon replace oidc_team_mapping_enabled.
            konnect_mapping_enabled: Whether a Konnect Identity Admin assigns teams to a developer.
            oidc_auth_enabled: The organization has OIDC disabled.
            oidc_claim_mappings: Mappings from a portal developer atribute to an Identity Provider claim.
            oidc_client_id: str
            oidc_client_secret: str
            oidc_issuer: str
            oidc_scopes: typing.List[str]
            oidc_team_mapping_enabled: Whether IdP groups determine the Konnect Portal teams a developer has.
            saml_auth_enabled: The portal has SAML enabled or disabled.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a portal's authentication settings.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.authentication_settings.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            basic_auth_enabled=False,
            idp_mapping_enabled=True,
            konnect_mapping_enabled=False,
            oidc_auth_enabled=False,
            oidc_team_mapping_enabled=True,
            saml_auth_enabled=False,
        )
        ```
        """
        _json = to_encodable(
            item={
                "basic_auth_enabled": basic_auth_enabled,
                "idp_mapping_enabled": idp_mapping_enabled,
                "konnect_mapping_enabled": konnect_mapping_enabled,
                "oidc_auth_enabled": oidc_auth_enabled,
                "oidc_claim_mappings": oidc_claim_mappings,
                "oidc_client_id": oidc_client_id,
                "oidc_client_secret": oidc_client_secret,
                "oidc_issuer": oidc_issuer,
                "oidc_scopes": oidc_scopes,
                "oidc_team_mapping_enabled": oidc_team_mapping_enabled,
                "saml_auth_enabled": saml_auth_enabled,
            },
            dump_with=params._SerializerPortalAuthenticationSettingsUpdateRequest,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/authentication-settings",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalAuthenticationSettingsResponse,
            request_options=request_options or default_request_options(),
        )
