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
from sideko_kong_sdk_docs.resources.kong_portal.portals.developers.teams import (
    AsyncTeamsClient,
    TeamsClient,
)
from sideko_kong_sdk_docs.types import models, params


class DevelopersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.teams = TeamsClient(base_client=self._base_client)

    def delete(
        self,
        *,
        developer_id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Developer

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes a developer, which will discontinue their ability to login, view any non-public resources, and delete all applications owned by them. All credentials issued to the developer will no longer provide access to any APIs. A deleted developer's unique email must be re-registered and approved to gain access again.

        DELETE /portals/{portalId}/developers/{developerId}

        Args:
            developerId: ID of the developer.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.developers.delete(
            developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/developers/{developer_id}",
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
            typing.Optional[params.KongPortalPortalsDevelopersListFilter],
            type_utils.NotGiven,
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
    ) -> models.ListDevelopersResponse:
        """
        List Developers

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists the developers that have registered for this portal. Each developer can be registered to one portal and must be approved to login unless using the developer auto-approve setting.

        GET /portals/{portalId}/developers

        Args:
            filter: Filter developers returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            sort: Sorts a collection of developers. Supported sort attributes are:
          - created_at
          - updated_at
          - email
          - name
          - status

            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of developers in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.developers.list(
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
                    dump_with=params._SerializerKongPortalPortalsDevelopersListFilter,
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
            path=f"/portals/{portal_id}/developers",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListDevelopersResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        developer_id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalDeveloper:
        """
        Fetch Developer

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns information about a single developer in this portal. Each developer manages a set applications, providing them credentials to access registered APIs. Developer registration access can be limited to specific APIs using RBAC.

        GET /portals/{portalId}/developers/{developerId}

        Args:
            developerId: ID of the developer.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a developer in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.developers.get(
            developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/developers/{developer_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalDeveloper,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        developer_id: str,
        portal_id: str,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["approved", "pending", "rejected", "revoked"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalDeveloper:
        """
        Update Developer

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the status of a particular developer. Approved developers have access to login to the portal. Revoked, rejected, or pending are not allowed to login. Even if a developer's status is no longer approved, they will still be able to using any existing credentials generated while they were approved, until each application registration is revoked or deleted.

        PATCH /portals/{portalId}/developers/{developerId}

        Args:
            status: The status of a developer in a portal. Approved developers can log in, create applications, and view and register for products they have access to. Pending, revoked, and rejected developers cannot login or view any non-public portal information, or create or modify applications or registrations.
            developerId: ID of the developer.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about the developer being updated.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.developers.patch(
            developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            status="approved",
        )
        ```
        """
        _json = to_encodable(
            item={"status": status}, dump_with=params._SerializerUpdateDeveloperRequest
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/developers/{developer_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalDeveloper,
            request_options=request_options or default_request_options(),
        )


class AsyncDevelopersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.teams = AsyncTeamsClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        developer_id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Developer

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes a developer, which will discontinue their ability to login, view any non-public resources, and delete all applications owned by them. All credentials issued to the developer will no longer provide access to any APIs. A deleted developer's unique email must be re-registered and approved to gain access again.

        DELETE /portals/{portalId}/developers/{developerId}

        Args:
            developerId: ID of the developer.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.developers.delete(
            developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/developers/{developer_id}",
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
            typing.Optional[params.KongPortalPortalsDevelopersListFilter],
            type_utils.NotGiven,
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
    ) -> models.ListDevelopersResponse:
        """
        List Developers

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists the developers that have registered for this portal. Each developer can be registered to one portal and must be approved to login unless using the developer auto-approve setting.

        GET /portals/{portalId}/developers

        Args:
            filter: Filter developers returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            sort: Sorts a collection of developers. Supported sort attributes are:
          - created_at
          - updated_at
          - email
          - name
          - status

            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of developers in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.developers.list(
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
                    dump_with=params._SerializerKongPortalPortalsDevelopersListFilter,
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
            path=f"/portals/{portal_id}/developers",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListDevelopersResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        developer_id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalDeveloper:
        """
        Fetch Developer

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns information about a single developer in this portal. Each developer manages a set applications, providing them credentials to access registered APIs. Developer registration access can be limited to specific APIs using RBAC.

        GET /portals/{portalId}/developers/{developerId}

        Args:
            developerId: ID of the developer.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a developer in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.developers.get(
            developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/developers/{developer_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalDeveloper,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        developer_id: str,
        portal_id: str,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["approved", "pending", "rejected", "revoked"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalDeveloper:
        """
        Update Developer

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the status of a particular developer. Approved developers have access to login to the portal. Revoked, rejected, or pending are not allowed to login. Even if a developer's status is no longer approved, they will still be able to using any existing credentials generated while they were approved, until each application registration is revoked or deleted.

        PATCH /portals/{portalId}/developers/{developerId}

        Args:
            status: The status of a developer in a portal. Approved developers can log in, create applications, and view and register for products they have access to. Pending, revoked, and rejected developers cannot login or view any non-public portal information, or create or modify applications or registrations.
            developerId: ID of the developer.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about the developer being updated.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.developers.patch(
            developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            status="approved",
        )
        ```
        """
        _json = to_encodable(
            item={"status": status}, dump_with=params._SerializerUpdateDeveloperRequest
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/developers/{developer_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalDeveloper,
            request_options=request_options or default_request_options(),
        )
