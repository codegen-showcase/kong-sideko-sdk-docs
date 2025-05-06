import httpx
import typing

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


class DevelopersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        developer_id: str,
        portal_id: str,
        team_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove Developer from Team

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Removes a developer from a team. This removes the association of the team's roles from the developer.

        DELETE /portals/{portalId}/teams/{teamId}/developers/{developerId}

        Args:
            developerId: ID of the developer.
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.teams.developers.delete(
            developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/teams/{team_id}/developers/{developer_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        portal_id: str,
        team_id: str,
        filter: typing.Union[
            typing.Optional[params.KongPortalPortalsTeamsDevelopersListFilter],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        page_number: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ListBasicDevelopersResponse:
        """
        List Team Developers

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        List a team's developers.

        GET /portals/{portalId}/teams/{teamId}/developers

        Args:
            filter: Filter developers returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of basic developer information.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.teams.developers.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
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
                    dump_with=params._SerializerKongPortalPortalsTeamsDevelopersListFilter,
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
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/teams/{team_id}/developers",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListBasicDevelopersResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        id: str,
        portal_id: str,
        team_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Add Developer to Team

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Adds a developer to a team. This associates them with all of the roles that have been assigned to the team, providing specific permissions to perform actions on resources.

        POST /portals/{portalId}/teams/{teamId}/developers

        Args:
            id: str
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.teams.developers.create(
            id="df120cb4-f60b-47bc-a2f8-6a28e6a3c63b",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        ```
        """
        _json = to_encodable(
            item={"id": id}, dump_with=params._SerializerAddDeveloperToTeamRequest
        )
        return self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/teams/{team_id}/developers",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )


class AsyncDevelopersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        developer_id: str,
        portal_id: str,
        team_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove Developer from Team

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Removes a developer from a team. This removes the association of the team's roles from the developer.

        DELETE /portals/{portalId}/teams/{teamId}/developers/{developerId}

        Args:
            developerId: ID of the developer.
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.teams.developers.delete(
            developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/teams/{team_id}/developers/{developer_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        portal_id: str,
        team_id: str,
        filter: typing.Union[
            typing.Optional[params.KongPortalPortalsTeamsDevelopersListFilter],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        page_number: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ListBasicDevelopersResponse:
        """
        List Team Developers

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        List a team's developers.

        GET /portals/{portalId}/teams/{teamId}/developers

        Args:
            filter: Filter developers returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of basic developer information.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.teams.developers.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
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
                    dump_with=params._SerializerKongPortalPortalsTeamsDevelopersListFilter,
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
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/teams/{team_id}/developers",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListBasicDevelopersResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        id: str,
        portal_id: str,
        team_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Add Developer to Team

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Adds a developer to a team. This associates them with all of the roles that have been assigned to the team, providing specific permissions to perform actions on resources.

        POST /portals/{portalId}/teams/{teamId}/developers

        Args:
            id: str
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            Created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.teams.developers.create(
            id="df120cb4-f60b-47bc-a2f8-6a28e6a3c63b",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        ```
        """
        _json = to_encodable(
            item={"id": id}, dump_with=params._SerializerAddDeveloperToTeamRequest
        )
        return await self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/teams/{team_id}/developers",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )
