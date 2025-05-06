import httpx
import typing

from sideko_kong_sdk_docs.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from sideko_kong_sdk_docs.types import params


class MoveClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def update(
        self,
        *,
        page_id: str,
        portal_id: str,
        index: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        parent_page_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Move Page

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        This api allows the user to move a page within the page tree using the parameters parent_page_id and index. If parent_page_id is not provided, the page will be placed at the top level of the page tree. index represents a zero-indexed page order relative to its siblings under the same parent. For example, if we want to put the page at top level in first position we would send parent_page_id: null and index: 0. This api also supports using a negative index to count backwards from the end of the page list, which means you can put the page in last position by using index: -1.

        PUT /portals/{portalId}/pages/{pageId}/move

        Args:
            index: index of the document in the parent document's children
            parent_page_id: parent page id
            pageId: ID of the page.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            The document has been moved

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.pages.move.update(
            page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            index=1,
            parent_page_id="dd4e1b98-3629-4dd3-acc0-759a726ffee2",
        )
        ```
        """
        _json = to_encodable(
            item={"index": index, "parent_page_id": parent_page_id},
            dump_with=params._SerializerMovePageRequestPayload,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/portals/{portal_id}/pages/{page_id}/move",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )


class AsyncMoveClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def update(
        self,
        *,
        page_id: str,
        portal_id: str,
        index: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        parent_page_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Move Page

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        This api allows the user to move a page within the page tree using the parameters parent_page_id and index. If parent_page_id is not provided, the page will be placed at the top level of the page tree. index represents a zero-indexed page order relative to its siblings under the same parent. For example, if we want to put the page at top level in first position we would send parent_page_id: null and index: 0. This api also supports using a negative index to count backwards from the end of the page list, which means you can put the page in last position by using index: -1.

        PUT /portals/{portalId}/pages/{pageId}/move

        Args:
            index: index of the document in the parent document's children
            parent_page_id: parent page id
            pageId: ID of the page.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            The document has been moved

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.pages.move.update(
            page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            index=1,
            parent_page_id="dd4e1b98-3629-4dd3-acc0-759a726ffee2",
        )
        ```
        """
        _json = to_encodable(
            item={"index": index, "parent_page_id": parent_page_id},
            dump_with=params._SerializerMovePageRequestPayload,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/portals/{portal_id}/pages/{page_id}/move",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )
