import typing
import typing_extensions

from sideko_kong_sdk_docs.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from sideko_kong_sdk_docs.types import models, params


class IdentityProvidersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Identity Provider

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes an existing identity provider configuration. This operation removes a specific identity provider
        from the portal.

        DELETE /portals/{portalId}/identity-providers/{id}

        Args:
            id: ID of the identity provider.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.identity_providers.delete(
            id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/identity-providers/{id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        portal_id: str,
        filter: typing.Union[
            typing.Optional[params.KongPortalPortalsIdentityProvidersListFilter],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.IdentityProvider]:
        """
        Retrieve Identity Providers

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Retrieves the identity providers available within the portal. This operation provides information about
        various identity providers for SAML or OIDC authentication integrations.

        GET /portals/{portalId}/identity-providers

        Args:
            filter: Filter identity providers returned in the response.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A collection of identity providers. This response contains a collection of identity providers, which may  include both OIDC and SAML identity providers.


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.identity_providers.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(filter, type_utils.NotGiven):
            encode_query_param(
                _query,
                "filter",
                to_encodable(
                    item=filter,
                    dump_with=params._SerializerKongPortalPortalsIdentityProvidersListFilter,
                ),
                style="deepObject",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/identity-providers",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=typing.List[models.IdentityProvider],
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityProvider:
        """
        Get Identity Provider

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Retrieves the configuration of a single identity provider. This operation returns information about a
        specific identity provider's settings and authentication integration details.

        GET /portals/{portalId}/identity-providers/{id}

        Args:
            id: ID of the identity provider.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            An identity provider configuration. This response represents the configuration of a specific identity provider, which can be either OIDC or SAML.


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.identity_providers.get(
            id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/identity-providers/{id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.IdentityProvider,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        id: str,
        portal_id: str,
        config: typing.Union[
            typing.Optional[
                typing.Union[
                    params.ConfigureOidcIdentityProviderConfig,
                    params.SamlIdentityProviderConfig,
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityProvider:
        """
        Update Identity Provider

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the configuration of an existing identity provider. This operation allows modifications to be made
        to an existing identity provider's configuration.

        PATCH /portals/{portalId}/identity-providers/{id}

        Args:
            config: typing.Union[ConfigureOidcIdentityProviderConfig, SamlIdentityProviderConfig]
            enabled: Indicates whether the identity provider is enabled.
        Only one identity provider can be active at a time, such as SAML or OIDC.

            id: ID of the identity provider.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            An identity provider configuration. This response represents the configuration of a specific identity provider, which can be either OIDC or SAML.


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.identity_providers.patch(
            id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            config={
                "client_id": "YOUR_CLIENT_ID",
                "client_secret": "YOUR_CLIENT_SECRET",
                "issuer_url": "https://konghq.okta.com/oauth2/default",
            },
            enabled=True,
        )
        ```
        """
        _json = to_encodable(
            item={"config": config, "enabled": enabled},
            dump_with=params._SerializerUpdateIdentityProvider,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/identity-providers/{id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.IdentityProvider,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        portal_id: str,
        config: typing.Union[
            typing.Optional[
                typing.Union[
                    params.ConfigureOidcIdentityProviderConfig,
                    params.SamlIdentityProviderConfig,
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["oidc", "saml"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityProvider:
        """
        Create Identity Provider

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates a new identity provider. This operation allows the creation of a new identity provider for
        authentication purposes.

        POST /portals/{portalId}/identity-providers

        Args:
            config: typing.Union[ConfigureOidcIdentityProviderConfig, SamlIdentityProviderConfig]
            type: Specifies the type of identity provider.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            An identity provider configuration. This response represents the configuration of a specific identity provider, which can be either OIDC or SAML.


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.identity_providers.create(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            config={
                "client_id": "YOUR_CLIENT_ID",
                "client_secret": "YOUR_CLIENT_SECRET",
                "issuer_url": "https://konghq.okta.com/oauth2/default",
            },
            type_="oidc",
        )
        ```
        """
        _json = to_encodable(
            item={"config": config, "type_": type_},
            dump_with=params._SerializerCreateIdentityProvider,
        )
        return self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/identity-providers",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.IdentityProvider,
            request_options=request_options or default_request_options(),
        )


class AsyncIdentityProvidersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Identity Provider

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes an existing identity provider configuration. This operation removes a specific identity provider
        from the portal.

        DELETE /portals/{portalId}/identity-providers/{id}

        Args:
            id: ID of the identity provider.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.identity_providers.delete(
            id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/identity-providers/{id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        portal_id: str,
        filter: typing.Union[
            typing.Optional[params.KongPortalPortalsIdentityProvidersListFilter],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.IdentityProvider]:
        """
        Retrieve Identity Providers

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Retrieves the identity providers available within the portal. This operation provides information about
        various identity providers for SAML or OIDC authentication integrations.

        GET /portals/{portalId}/identity-providers

        Args:
            filter: Filter identity providers returned in the response.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A collection of identity providers. This response contains a collection of identity providers, which may  include both OIDC and SAML identity providers.


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.identity_providers.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(filter, type_utils.NotGiven):
            encode_query_param(
                _query,
                "filter",
                to_encodable(
                    item=filter,
                    dump_with=params._SerializerKongPortalPortalsIdentityProvidersListFilter,
                ),
                style="deepObject",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/identity-providers",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=typing.List[models.IdentityProvider],
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityProvider:
        """
        Get Identity Provider

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Retrieves the configuration of a single identity provider. This operation returns information about a
        specific identity provider's settings and authentication integration details.

        GET /portals/{portalId}/identity-providers/{id}

        Args:
            id: ID of the identity provider.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            An identity provider configuration. This response represents the configuration of a specific identity provider, which can be either OIDC or SAML.


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.identity_providers.get(
            id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/identity-providers/{id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.IdentityProvider,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        id: str,
        portal_id: str,
        config: typing.Union[
            typing.Optional[
                typing.Union[
                    params.ConfigureOidcIdentityProviderConfig,
                    params.SamlIdentityProviderConfig,
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityProvider:
        """
        Update Identity Provider

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the configuration of an existing identity provider. This operation allows modifications to be made
        to an existing identity provider's configuration.

        PATCH /portals/{portalId}/identity-providers/{id}

        Args:
            config: typing.Union[ConfigureOidcIdentityProviderConfig, SamlIdentityProviderConfig]
            enabled: Indicates whether the identity provider is enabled.
        Only one identity provider can be active at a time, such as SAML or OIDC.

            id: ID of the identity provider.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            An identity provider configuration. This response represents the configuration of a specific identity provider, which can be either OIDC or SAML.


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.identity_providers.patch(
            id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            config={
                "client_id": "YOUR_CLIENT_ID",
                "client_secret": "YOUR_CLIENT_SECRET",
                "issuer_url": "https://konghq.okta.com/oauth2/default",
            },
            enabled=True,
        )
        ```
        """
        _json = to_encodable(
            item={"config": config, "enabled": enabled},
            dump_with=params._SerializerUpdateIdentityProvider,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/identity-providers/{id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.IdentityProvider,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        portal_id: str,
        config: typing.Union[
            typing.Optional[
                typing.Union[
                    params.ConfigureOidcIdentityProviderConfig,
                    params.SamlIdentityProviderConfig,
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["oidc", "saml"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityProvider:
        """
        Create Identity Provider

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates a new identity provider. This operation allows the creation of a new identity provider for
        authentication purposes.

        POST /portals/{portalId}/identity-providers

        Args:
            config: typing.Union[ConfigureOidcIdentityProviderConfig, SamlIdentityProviderConfig]
            type: Specifies the type of identity provider.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            An identity provider configuration. This response represents the configuration of a specific identity provider, which can be either OIDC or SAML.


        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.identity_providers.create(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            config={
                "client_id": "YOUR_CLIENT_ID",
                "client_secret": "YOUR_CLIENT_SECRET",
                "issuer_url": "https://konghq.okta.com/oauth2/default",
            },
            type_="oidc",
        )
        ```
        """
        _json = to_encodable(
            item={"config": config, "type_": type_},
            dump_with=params._SerializerCreateIdentityProvider,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/identity-providers",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.IdentityProvider,
            request_options=request_options or default_request_options(),
        )
