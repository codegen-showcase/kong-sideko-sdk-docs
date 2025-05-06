import typing

from sideko_kong_sdk_docs.core import (
    AsyncBaseClient,
    BinaryResponse,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from sideko_kong_sdk_docs.types import params


class FaviconClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BinaryResponse:
        """
        Get Favicon

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the favicon of the portal.

        GET /portals/{portalId}/assets/favicon

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Logo of the portal. Can be either png or jpeg

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.assets.favicon.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/assets/favicon",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        data: str,
        portal_id: str,
        filename: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Replace Favicon

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Replaces the favicon of the portal. The favicon is used in the browser tab of the portal.

        PUT /portals/{portalId}/assets/favicon

        Args:
            filename: str
            data: must be a data URL with base64 image data, e.g., data:image/jpeg;base64,<BASE64_IMAGE_DATA>
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Logo of the portal. Can be either png or jpeg

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.assets.favicon.update(
            data="data:image/png;base64,bmljZV9sb29raW5nX3BpY3R1cmU=",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            filename="logo.png",
        )
        ```
        """
        _json = to_encodable(
            item={"filename": filename, "data": data},
            dump_with=typing.Optional[params._SerializerReplacePortalImageAsset],
        )
        return self._base_client.request(
            method="PUT",
            path=f"/portals/{portal_id}/assets/favicon",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncFaviconClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BinaryResponse:
        """
        Get Favicon

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the favicon of the portal.

        GET /portals/{portalId}/assets/favicon

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Logo of the portal. Can be either png or jpeg

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.assets.favicon.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/assets/favicon",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        data: str,
        portal_id: str,
        filename: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Replace Favicon

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Replaces the favicon of the portal. The favicon is used in the browser tab of the portal.

        PUT /portals/{portalId}/assets/favicon

        Args:
            filename: str
            data: must be a data URL with base64 image data, e.g., data:image/jpeg;base64,<BASE64_IMAGE_DATA>
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Logo of the portal. Can be either png or jpeg

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.assets.favicon.update(
            data="data:image/png;base64,bmljZV9sb29raW5nX3BpY3R1cmU=",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            filename="logo.png",
        )
        ```
        """
        _json = to_encodable(
            item={"filename": filename, "data": data},
            dump_with=typing.Optional[params._SerializerReplacePortalImageAsset],
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/portals/{portal_id}/assets/favicon",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )
