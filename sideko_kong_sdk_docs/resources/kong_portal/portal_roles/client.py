import typing

from sideko_kong_sdk_docs.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from sideko_kong_sdk_docs.types import models


class PortalRolesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ListRolesResponse:
        """
        List Portal Roles

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        List roles that can be assigned to teams in a portal. Each role provides a set of permissions to perform an action on a resource.

        GET /portal-roles

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            A set of roles available in portals.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portal_roles.list()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/portal-roles",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.ListRolesResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncPortalRolesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.ListRolesResponse:
        """
        List Portal Roles

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        List roles that can be assigned to teams in a portal. Each role provides a set of permissions to perform an action on a resource.

        GET /portal-roles

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            A set of roles available in portals.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portal_roles.list()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/portal-roles",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.ListRolesResponse,
            request_options=request_options or default_request_options(),
        )
