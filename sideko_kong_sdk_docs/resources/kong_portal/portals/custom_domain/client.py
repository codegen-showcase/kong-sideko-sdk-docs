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


class CustomDomainClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove Domain

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes the custom domain associated with the portal.

        DELETE /portals/{portalId}/custom-domain

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.custom_domain.delete(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/custom-domain",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.PortalCustomDomain:
        """
        Get Custom Domain

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Get the custom domain associated to the portal.

        GET /portals/{portalId}/custom-domain

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Portal custom domain

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.custom_domain.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/custom-domain",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalCustomDomain,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        portal_id: str,
        enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalCustomDomain:
        """
        Enable or Disable Domain

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the portal domain associated with the portal.

        PATCH /portals/{portalId}/custom-domain

        Args:
            enabled: bool
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Portal custom domain

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.custom_domain.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _json = to_encodable(
            item={"enabled": enabled},
            dump_with=params._SerializerUpdatePortalCustomDomainRequest,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/custom-domain",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalCustomDomain,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        enabled: bool,
        hostname: str,
        portal_id: str,
        ssl: params.CreatePortalCustomDomainSsl,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalCustomDomain:
        """
        Create Custom Domain

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates the custom domain associated with the portal. Only one custom domain can be associated with a portal at a time.

        POST /portals/{portalId}/custom-domain

        Args:
            enabled: bool
            hostname: str
            portalId: ID of the portal.
            ssl: CreatePortalCustomDomainSsl
            request_options: Additional options to customize the HTTP request

        Returns:
            Portal custom domain

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.custom_domain.create(
            enabled=True,
            hostname="string",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            ssl={"domain_verification_method": "http"},
        )
        ```
        """
        _json = to_encodable(
            item={"enabled": enabled, "hostname": hostname, "ssl": ssl},
            dump_with=params._SerializerCreatePortalCustomDomainRequest,
        )
        return self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/custom-domain",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalCustomDomain,
            request_options=request_options or default_request_options(),
        )


class AsyncCustomDomainClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove Domain

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes the custom domain associated with the portal.

        DELETE /portals/{portalId}/custom-domain

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.custom_domain.delete(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/custom-domain",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.PortalCustomDomain:
        """
        Get Custom Domain

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Get the custom domain associated to the portal.

        GET /portals/{portalId}/custom-domain

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Portal custom domain

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.custom_domain.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/custom-domain",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalCustomDomain,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        portal_id: str,
        enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalCustomDomain:
        """
        Enable or Disable Domain

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the portal domain associated with the portal.

        PATCH /portals/{portalId}/custom-domain

        Args:
            enabled: bool
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Portal custom domain

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.custom_domain.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _json = to_encodable(
            item={"enabled": enabled},
            dump_with=params._SerializerUpdatePortalCustomDomainRequest,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/custom-domain",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalCustomDomain,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        enabled: bool,
        hostname: str,
        portal_id: str,
        ssl: params.CreatePortalCustomDomainSsl,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalCustomDomain:
        """
        Create Custom Domain

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates the custom domain associated with the portal. Only one custom domain can be associated with a portal at a time.

        POST /portals/{portalId}/custom-domain

        Args:
            enabled: bool
            hostname: str
            portalId: ID of the portal.
            ssl: CreatePortalCustomDomainSsl
            request_options: Additional options to customize the HTTP request

        Returns:
            Portal custom domain

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.custom_domain.create(
            enabled=True,
            hostname="string",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            ssl={"domain_verification_method": "http"},
        )
        ```
        """
        _json = to_encodable(
            item={"enabled": enabled, "hostname": hostname, "ssl": ssl},
            dump_with=params._SerializerCreatePortalCustomDomainRequest,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/custom-domain",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalCustomDomain,
            request_options=request_options or default_request_options(),
        )
