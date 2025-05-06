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


class SnippetsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        portal_id: str,
        snippet_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Snippet

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes a single custom snippet for this portal.

        DELETE /portals/{portalId}/snippets/{snippetId}

        Args:
            portalId: ID of the portal.
            snippetId: ID of the snippet.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.snippets.delete(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/snippets/{snippet_id}",
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
            typing.Optional[params.PortalSnippetsFilterParameters], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_number: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sort: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ListPortalSnippetsResponse:
        """
        List Snippets

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the paginated list of custom snippets that have been created for this portal.

        GET /portals/{portalId}/snippets

        Args:
            filter: Filter snippets returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            sort: Sorts a collection of portal snippets. Supported sort attributes are:
          - created_at
          - updated_at
          - name
          - title
          - visibility

            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of custom snippets in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.snippets.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            page_number=1,
            page_size=10,
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
                    dump_with=params._SerializerPortalSnippetsFilterParameters,
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(page_number, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page[number]",
                to_encodable(item=page_number, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(page_size, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page[size]",
                to_encodable(item=page_size, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(sort, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sort",
                to_encodable(item=sort, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/snippets",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListPortalSnippetsResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        portal_id: str,
        snippet_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalSnippetResponse:
        """
        Fetch Snippet

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the configuration of a single custom snippet for this portal. Custom snippets can be used to display static content, documentation, or other information to developers.

        GET /portals/{portalId}/snippets/{snippetId}

        Args:
            portalId: ID of the portal.
            snippetId: ID of the snippet.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a snippet in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.snippets.get(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/snippets/{snippet_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalSnippetResponse,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        portal_id: str,
        snippet_id: str,
        content: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["published", "unpublished"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        visibility: typing.Union[
            typing.Optional[typing_extensions.Literal["private", "public"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalSnippetResponse:
        """
        Update Snippet

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the configuration of a single custom snippet for this portal.

        PATCH /portals/{portalId}/snippets/{snippetId}

        Args:
            content: The renderable markdown content of a page in a portal.
            description: str
            name: The unique name of a snippet in a portal.
            status: Whether the resource is visible on a given portal. Defaults to false.
            title: The display title of a snippet in a portal.
            visibility: Whether the resource is publicly accessible to non-authenticated users. Defaults to private.
            portalId: ID of the portal.
            snippetId: ID of the snippet.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a snippet in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.snippets.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
            content="Welcome to the About Us page. This is where you can learn about our company.",
            name="about-us",
            title="About Us",
        )
        ```
        """
        _json = to_encodable(
            item={
                "content": content,
                "description": description,
                "name": name,
                "status": status,
                "title": title,
                "visibility": visibility,
            },
            dump_with=params._SerializerUpdatePortalSnippetRequest,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/snippets/{snippet_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalSnippetResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        content: str,
        name: str,
        portal_id: str,
        title: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["published", "unpublished"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        visibility: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalSnippetResponse:
        """
        Create Snippet

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates a new custom snippet for this portal. Custom snippets can be used to display static content, documentation, or other information to developers.

        POST /portals/{portalId}/snippets

        Args:
            description: str
            status: Whether the resource is visible on a given portal. Defaults to false.
            visibility: Whether a page is publicly accessible to non-authenticated users.
            content: The renderable markdown content of a page in a portal.
            name: The unique name of a snippet in a portal.
            portalId: ID of the portal.
            title: The display title of a snippet in a portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a snippet in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.snippets.create(
            content="Welcome to the Getting Started page. This is where you can learn how to use our APIs.",
            name="getting-started",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            title="Getting Started",
            status="published",
            visibility="public",
        )
        ```
        """
        _json = to_encodable(
            item={
                "description": description,
                "status": status,
                "visibility": visibility,
                "content": content,
                "name": name,
                "title": title,
            },
            dump_with=params._SerializerCreatePortalSnippetRequest,
        )
        return self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/snippets",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalSnippetResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncSnippetsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        portal_id: str,
        snippet_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Snippet

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes a single custom snippet for this portal.

        DELETE /portals/{portalId}/snippets/{snippetId}

        Args:
            portalId: ID of the portal.
            snippetId: ID of the snippet.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.snippets.delete(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/snippets/{snippet_id}",
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
            typing.Optional[params.PortalSnippetsFilterParameters], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_number: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sort: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ListPortalSnippetsResponse:
        """
        List Snippets

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the paginated list of custom snippets that have been created for this portal.

        GET /portals/{portalId}/snippets

        Args:
            filter: Filter snippets returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            sort: Sorts a collection of portal snippets. Supported sort attributes are:
          - created_at
          - updated_at
          - name
          - title
          - visibility

            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of custom snippets in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.snippets.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            page_number=1,
            page_size=10,
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
                    dump_with=params._SerializerPortalSnippetsFilterParameters,
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(page_number, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page[number]",
                to_encodable(item=page_number, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(page_size, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page[size]",
                to_encodable(item=page_size, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(sort, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sort",
                to_encodable(item=sort, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/snippets",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListPortalSnippetsResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        portal_id: str,
        snippet_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalSnippetResponse:
        """
        Fetch Snippet

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the configuration of a single custom snippet for this portal. Custom snippets can be used to display static content, documentation, or other information to developers.

        GET /portals/{portalId}/snippets/{snippetId}

        Args:
            portalId: ID of the portal.
            snippetId: ID of the snippet.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a snippet in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.snippets.get(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/snippets/{snippet_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalSnippetResponse,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        portal_id: str,
        snippet_id: str,
        content: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["published", "unpublished"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        visibility: typing.Union[
            typing.Optional[typing_extensions.Literal["private", "public"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalSnippetResponse:
        """
        Update Snippet

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the configuration of a single custom snippet for this portal.

        PATCH /portals/{portalId}/snippets/{snippetId}

        Args:
            content: The renderable markdown content of a page in a portal.
            description: str
            name: The unique name of a snippet in a portal.
            status: Whether the resource is visible on a given portal. Defaults to false.
            title: The display title of a snippet in a portal.
            visibility: Whether the resource is publicly accessible to non-authenticated users. Defaults to private.
            portalId: ID of the portal.
            snippetId: ID of the snippet.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a snippet in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.snippets.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
            content="Welcome to the About Us page. This is where you can learn about our company.",
            name="about-us",
            title="About Us",
        )
        ```
        """
        _json = to_encodable(
            item={
                "content": content,
                "description": description,
                "name": name,
                "status": status,
                "title": title,
                "visibility": visibility,
            },
            dump_with=params._SerializerUpdatePortalSnippetRequest,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/snippets/{snippet_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalSnippetResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        content: str,
        name: str,
        portal_id: str,
        title: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["published", "unpublished"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        visibility: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalSnippetResponse:
        """
        Create Snippet

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates a new custom snippet for this portal. Custom snippets can be used to display static content, documentation, or other information to developers.

        POST /portals/{portalId}/snippets

        Args:
            description: str
            status: Whether the resource is visible on a given portal. Defaults to false.
            visibility: Whether a page is publicly accessible to non-authenticated users.
            content: The renderable markdown content of a page in a portal.
            name: The unique name of a snippet in a portal.
            portalId: ID of the portal.
            title: The display title of a snippet in a portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a snippet in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.snippets.create(
            content="Welcome to the Getting Started page. This is where you can learn how to use our APIs.",
            name="getting-started",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            title="Getting Started",
            status="published",
            visibility="public",
        )
        ```
        """
        _json = to_encodable(
            item={
                "description": description,
                "status": status,
                "visibility": visibility,
                "content": content,
                "name": name,
                "title": title,
            },
            dump_with=params._SerializerCreatePortalSnippetRequest,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/snippets",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalSnippetResponse,
            request_options=request_options or default_request_options(),
        )
