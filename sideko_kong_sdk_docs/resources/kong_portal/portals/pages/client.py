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
from sideko_kong_sdk_docs.resources.kong_portal.portals.pages.move import (
    AsyncMoveClient,
    MoveClient,
)
from sideko_kong_sdk_docs.types import models, params


class PagesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.move = MoveClient(base_client=self._base_client)

    def delete(
        self,
        *,
        page_id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Page

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes a single custom page for this portal.

        DELETE /portals/{portalId}/pages/{pageId}

        Args:
            pageId: ID of the page.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.pages.delete(
            page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/pages/{page_id}",
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
            typing.Optional[params.PortalPagesFilterParameters], type_utils.NotGiven
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
    ) -> models.ListPortalPagesResponse:
        """
        List Pages

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the paginated list of custom pages that have been created for this portal.

        GET /portals/{portalId}/pages

        Args:
            filter: Filter pages returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            sort: Sorts a collection of portal pages. Supported sort attributes are:
          - created_at
          - updated_at
          - slug
          - title
          - visibility

            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of custom pages in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.pages.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            page_number=1,
            page_size=10,
        )
        ```
        """
        models.ListPortalPagesResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(filter, type_utils.NotGiven):
            encode_query_param(
                _query,
                "filter",
                to_encodable(
                    item=filter, dump_with=params._SerializerPortalPagesFilterParameters
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
            path=f"/portals/{portal_id}/pages",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListPortalPagesResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        page_id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalPageResponse:
        """
        Fetch Page

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the configuration of a single custom page for this portal. Custom pages can be used to display static content, documentation, or other information to developers.

        GET /portals/{portalId}/pages/{pageId}

        Args:
            pageId: ID of the page.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a page in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.pages.get(
            page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/pages/{page_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalPageResponse,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        page_id: str,
        portal_id: str,
        content: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        parent_page_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slug: typing.Union[
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
    ) -> models.PortalPageResponse:
        """
        Update Page

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the configuration of a single custom page for this portal.

        PATCH /portals/{portalId}/pages/{pageId}

        Args:
            content: The renderable markdown content of a page in a portal.
            description: str
            parent_page_id: Pages may be rendered as a tree of files.

        Specify the `id` of another page as the `parent_page_id` to add some hierarchy to your pages.

            slug: The slug of a page in a portal. Is used to compute the full path /slug1/slug2/slug3.
            status: Whether the resource is visible on a given portal. Defaults to false.
            title: The title of a page in a portal.
            visibility: Whether the resource is publicly accessible to non-authenticated users. Defaults to private.
            pageId: ID of the page.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a page in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.pages.patch(
            page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            content="Welcome to the About Us page. This is where you can learn about our company.",
            slug="/about-us",
            title="About Us",
        )
        ```
        """
        _json = to_encodable(
            item={
                "content": content,
                "description": description,
                "parent_page_id": parent_page_id,
                "slug": slug,
                "status": status,
                "title": title,
                "visibility": visibility,
            },
            dump_with=params._SerializerUpdatePortalPageRequest,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/pages/{page_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalPageResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        content: str,
        portal_id: str,
        slug: str,
        title: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        parent_page_id: typing.Union[
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
    ) -> models.PortalPageResponse:
        """
        Create Page

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates a new custom page for this portal. Custom pages can be used to display static content, documentation, or other information to developers.

        POST /portals/{portalId}/pages

        Args:
            description: str
            parent_page_id: Pages may be rendered as a tree of files.

        Specify the `id` of another page as the `parent_page_id` to add some hierarchy to your pages.

            status: Whether the resource is visible on a given portal. Defaults to false.
            visibility: Whether a page is publicly accessible to non-authenticated users.
            content: The renderable markdown content of a page in a portal.
            portalId: ID of the portal.
            slug: The slug of a page in a portal. Is used to compute the full path /slug1/slug2/slug3.
            title: The title of a page in a portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a page in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.pages.create(
            content="Welcome to the Getting Started page. This is where you can learn how to use our APIs.",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            slug="/getting-started",
            title="Getting Started",
            status="published",
            visibility="public",
        )
        ```
        """
        _json = to_encodable(
            item={
                "description": description,
                "parent_page_id": parent_page_id,
                "status": status,
                "visibility": visibility,
                "content": content,
                "slug": slug,
                "title": title,
            },
            dump_with=params._SerializerCreatePortalPageRequest,
        )
        return self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/pages",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalPageResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncPagesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.move = AsyncMoveClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        page_id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Page

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes a single custom page for this portal.

        DELETE /portals/{portalId}/pages/{pageId}

        Args:
            pageId: ID of the page.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.pages.delete(
            page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/pages/{page_id}",
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
            typing.Optional[params.PortalPagesFilterParameters], type_utils.NotGiven
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
    ) -> models.ListPortalPagesResponse:
        """
        List Pages

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the paginated list of custom pages that have been created for this portal.

        GET /portals/{portalId}/pages

        Args:
            filter: Filter pages returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            sort: Sorts a collection of portal pages. Supported sort attributes are:
          - created_at
          - updated_at
          - slug
          - title
          - visibility

            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of custom pages in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.pages.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            page_number=1,
            page_size=10,
        )
        ```
        """
        models.ListPortalPagesResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(filter, type_utils.NotGiven):
            encode_query_param(
                _query,
                "filter",
                to_encodable(
                    item=filter, dump_with=params._SerializerPortalPagesFilterParameters
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
            path=f"/portals/{portal_id}/pages",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListPortalPagesResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        page_id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalPageResponse:
        """
        Fetch Page

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the configuration of a single custom page for this portal. Custom pages can be used to display static content, documentation, or other information to developers.

        GET /portals/{portalId}/pages/{pageId}

        Args:
            pageId: ID of the page.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a page in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.pages.get(
            page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/pages/{page_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalPageResponse,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        page_id: str,
        portal_id: str,
        content: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        parent_page_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        slug: typing.Union[
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
    ) -> models.PortalPageResponse:
        """
        Update Page

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the configuration of a single custom page for this portal.

        PATCH /portals/{portalId}/pages/{pageId}

        Args:
            content: The renderable markdown content of a page in a portal.
            description: str
            parent_page_id: Pages may be rendered as a tree of files.

        Specify the `id` of another page as the `parent_page_id` to add some hierarchy to your pages.

            slug: The slug of a page in a portal. Is used to compute the full path /slug1/slug2/slug3.
            status: Whether the resource is visible on a given portal. Defaults to false.
            title: The title of a page in a portal.
            visibility: Whether the resource is publicly accessible to non-authenticated users. Defaults to private.
            pageId: ID of the page.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a page in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.pages.patch(
            page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            content="Welcome to the About Us page. This is where you can learn about our company.",
            slug="/about-us",
            title="About Us",
        )
        ```
        """
        _json = to_encodable(
            item={
                "content": content,
                "description": description,
                "parent_page_id": parent_page_id,
                "slug": slug,
                "status": status,
                "title": title,
                "visibility": visibility,
            },
            dump_with=params._SerializerUpdatePortalPageRequest,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/pages/{page_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalPageResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        content: str,
        portal_id: str,
        slug: str,
        title: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        parent_page_id: typing.Union[
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
    ) -> models.PortalPageResponse:
        """
        Create Page

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates a new custom page for this portal. Custom pages can be used to display static content, documentation, or other information to developers.

        POST /portals/{portalId}/pages

        Args:
            description: str
            parent_page_id: Pages may be rendered as a tree of files.

        Specify the `id` of another page as the `parent_page_id` to add some hierarchy to your pages.

            status: Whether the resource is visible on a given portal. Defaults to false.
            visibility: Whether a page is publicly accessible to non-authenticated users.
            content: The renderable markdown content of a page in a portal.
            portalId: ID of the portal.
            slug: The slug of a page in a portal. Is used to compute the full path /slug1/slug2/slug3.
            title: The title of a page in a portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a page in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.pages.create(
            content="Welcome to the Getting Started page. This is where you can learn how to use our APIs.",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            slug="/getting-started",
            title="Getting Started",
            status="published",
            visibility="public",
        )
        ```
        """
        _json = to_encodable(
            item={
                "description": description,
                "parent_page_id": parent_page_id,
                "status": status,
                "visibility": visibility,
                "content": content,
                "slug": slug,
                "title": title,
            },
            dump_with=params._SerializerCreatePortalPageRequest,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/pages",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalPageResponse,
            request_options=request_options or default_request_options(),
        )
