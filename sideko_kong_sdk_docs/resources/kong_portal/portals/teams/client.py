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
from sideko_kong_sdk_docs.resources.kong_portal.portals.teams.assigned_roles import (
    AssignedRolesClient,
    AsyncAssignedRolesClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.teams.developers import (
    AsyncDevelopersClient,
    DevelopersClient,
)
from sideko_kong_sdk_docs.types import models, params


class TeamsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.assigned_roles = AssignedRolesClient(base_client=self._base_client)
        self.developers = DevelopersClient(base_client=self._base_client)

    def delete(
        self,
        *,
        portal_id: str,
        team_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Team

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes a developer team from a portal. Deleting a team also deletes its assigned roles. Members of the team are not deleted, but they will lose any access provided through the team.

        DELETE /portals/{portalId}/teams/{teamId}

        Args:
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
        client.kong_portal.portals.teams.delete(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/teams/{team_id}",
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
            typing.Optional[params.KongPortalPortalsTeamsListFilter],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        page_number: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ListPortalTeamsResponse:
        """
        List Teams

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists the developer teams in a portal. Each team can contain any developer and developers can be part of multiple teams.

        GET /portals/{portalId}/teams

        Args:
            filter: Filter teams returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of teams in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.teams.list(
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
                    dump_with=params._SerializerKongPortalPortalsTeamsListFilter,
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
            path=f"/portals/{portal_id}/teams",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListPortalTeamsResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        portal_id: str,
        team_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalTeamResponse:
        """
        Get Team

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Get an individual team.

        GET /portals/{portalId}/teams/{teamId}

        Args:
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a team of developers in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.teams.get(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/teams/{team_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalTeamResponse,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        portal_id: str,
        team_id: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalTeamResponse:
        """
        Update Team

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates an individual developer team for a portal.

        PATCH /portals/{portalId}/teams/{teamId}

        Args:
            description: str
            name: str
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a team of developers in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.teams.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            description="The Identity Management (IDM) API team.",
            name="IDM - Developers",
        )
        ```
        """
        _json = to_encodable(
            item={"description": description, "name": name},
            dump_with=params._SerializerPortalUpdateTeamRequest,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/teams/{team_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalTeamResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        portal_id: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalTeamResponse:
        """
        Create Team

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates a developer team in a portal. Developers can be added to teams to provide RBAC access to API products. Teams can be assigned roles that grant permissions to perform an action on a resource.

        POST /portals/{portalId}/teams

        Args:
            description: str
            name: str
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a team of developers in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.teams.create(
            name="IDM - Developers",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            description="The Identity Management (IDM) API team.",
        )
        ```
        """
        _json = to_encodable(
            item={"description": description, "name": name},
            dump_with=params._SerializerPortalCreateTeamRequest,
        )
        return self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/teams",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalTeamResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncTeamsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.assigned_roles = AsyncAssignedRolesClient(base_client=self._base_client)
        self.developers = AsyncDevelopersClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        portal_id: str,
        team_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Team

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes a developer team from a portal. Deleting a team also deletes its assigned roles. Members of the team are not deleted, but they will lose any access provided through the team.

        DELETE /portals/{portalId}/teams/{teamId}

        Args:
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
        await client.kong_portal.portals.teams.delete(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/teams/{team_id}",
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
            typing.Optional[params.KongPortalPortalsTeamsListFilter],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        page_number: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ListPortalTeamsResponse:
        """
        List Teams

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists the developer teams in a portal. Each team can contain any developer and developers can be part of multiple teams.

        GET /portals/{portalId}/teams

        Args:
            filter: Filter teams returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of teams in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.teams.list(
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
                    dump_with=params._SerializerKongPortalPortalsTeamsListFilter,
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
            path=f"/portals/{portal_id}/teams",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListPortalTeamsResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        portal_id: str,
        team_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalTeamResponse:
        """
        Get Team

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Get an individual team.

        GET /portals/{portalId}/teams/{teamId}

        Args:
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a team of developers in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.teams.get(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/teams/{team_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalTeamResponse,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        portal_id: str,
        team_id: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalTeamResponse:
        """
        Update Team

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates an individual developer team for a portal.

        PATCH /portals/{portalId}/teams/{teamId}

        Args:
            description: str
            name: str
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a team of developers in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.teams.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            description="The Identity Management (IDM) API team.",
            name="IDM - Developers",
        )
        ```
        """
        _json = to_encodable(
            item={"description": description, "name": name},
            dump_with=params._SerializerPortalUpdateTeamRequest,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/teams/{team_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalTeamResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        portal_id: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalTeamResponse:
        """
        Create Team

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates a developer team in a portal. Developers can be added to teams to provide RBAC access to API products. Teams can be assigned roles that grant permissions to perform an action on a resource.

        POST /portals/{portalId}/teams

        Args:
            description: str
            name: str
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a team of developers in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.teams.create(
            name="IDM - Developers",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            description="The Identity Management (IDM) API team.",
        )
        ```
        """
        _json = to_encodable(
            item={"description": description, "name": name},
            dump_with=params._SerializerPortalCreateTeamRequest,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/teams",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalTeamResponse,
            request_options=request_options or default_request_options(),
        )
