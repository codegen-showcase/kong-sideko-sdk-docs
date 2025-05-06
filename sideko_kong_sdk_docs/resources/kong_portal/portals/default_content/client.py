import typing

from sideko_kong_sdk_docs.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from sideko_kong_sdk_docs.types import models


class DefaultContentClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DefaultContent:
        """
        Creates Default Pages

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates the default pages for a portal if they do not already exists.

        POST /portals/{portalId}/default-content

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Summary of created default content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.default_content.create(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/default-content",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.DefaultContent,
            request_options=request_options or default_request_options(),
        )


class AsyncDefaultContentClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DefaultContent:
        """
        Creates Default Pages

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates the default pages for a portal if they do not already exists.

        POST /portals/{portalId}/default-content

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Summary of created default content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.default_content.create(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return await self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/default-content",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.DefaultContent,
            request_options=request_options or default_request_options(),
        )
