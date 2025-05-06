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


class AssignedRolesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        portal_id: str,
        role_id: str,
        team_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove Role

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Removes an assigned role from a developer team. This deletes the association of the role with team and each of its members.

        DELETE /portals/{portalId}/teams/{teamId}/assigned-roles/{roleId}

        Args:
            portalId: ID of the portal.
            roleId: str
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.teams.assigned_roles.delete(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            role_id="8350205f-a305-4e39-abe9-bc082a80091a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/teams/{team_id}/assigned-roles/{role_id}",
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
        page_number: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AssignedPortalRoleCollectionResponse:
        """
        List Team Roles

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists the roles belonging to a developer team. Each role provides permissions to perform actions on a specified resource or collection.

        GET /portals/{portalId}/teams/{teamId}/assigned-roles

        Args:
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated collection of assigned roles.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.teams.assigned_roles.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            page_number=1,
            page_size=10,
        )
        ```
        """
        _query: QueryParams = {}
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
            path=f"/portals/{portal_id}/teams/{team_id}/assigned-roles",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.AssignedPortalRoleCollectionResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        portal_id: str,
        team_id: str,
        entity_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        entity_region: typing.Union[
            typing.Optional[
                typing_extensions.Literal["*", "au", "eu", "in", "me", "us"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        entity_type_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_number: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        role_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalAssignedRoleResponse:
        """
        Assign Role

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Assign a role to a developer team. This associates the set of permissions in a role with the team, so that they will be applied to any developer who is a member of the team.

        POST /portals/{portalId}/teams/{teamId}/assigned-roles

        Args:
            entity_id: str
            entity_region: Region of the entity.
            entity_type_name: str
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            role_name: str
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about the role assignment.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.teams.assigned_roles.create(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            entity_id="18ee2573-dec0-4b83-be99-fa7700bcdc61",
            entity_region="us",
            entity_type_name="Services",
            page_number=1,
            page_size=10,
            role_name="API Consumer",
        )
        ```
        """
        _query: QueryParams = {}
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
        _json = to_encodable(
            item={
                "entity_id": entity_id,
                "entity_region": entity_region,
                "entity_type_name": entity_type_name,
                "role_name": role_name,
            },
            dump_with=params._SerializerPortalAssignRoleRequest,
        )
        return self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/teams/{team_id}/assigned-roles",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            json=_json,
            cast_to=models.PortalAssignedRoleResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAssignedRolesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        portal_id: str,
        role_id: str,
        team_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove Role

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Removes an assigned role from a developer team. This deletes the association of the role with team and each of its members.

        DELETE /portals/{portalId}/teams/{teamId}/assigned-roles/{roleId}

        Args:
            portalId: ID of the portal.
            roleId: str
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.teams.assigned_roles.delete(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            role_id="8350205f-a305-4e39-abe9-bc082a80091a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/teams/{team_id}/assigned-roles/{role_id}",
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
        page_number: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AssignedPortalRoleCollectionResponse:
        """
        List Team Roles

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists the roles belonging to a developer team. Each role provides permissions to perform actions on a specified resource or collection.

        GET /portals/{portalId}/teams/{teamId}/assigned-roles

        Args:
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated collection of assigned roles.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.teams.assigned_roles.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            page_number=1,
            page_size=10,
        )
        ```
        """
        _query: QueryParams = {}
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
            path=f"/portals/{portal_id}/teams/{team_id}/assigned-roles",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.AssignedPortalRoleCollectionResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        portal_id: str,
        team_id: str,
        entity_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        entity_region: typing.Union[
            typing.Optional[
                typing_extensions.Literal["*", "au", "eu", "in", "me", "us"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        entity_type_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_number: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        role_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalAssignedRoleResponse:
        """
        Assign Role

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Assign a role to a developer team. This associates the set of permissions in a role with the team, so that they will be applied to any developer who is a member of the team.

        POST /portals/{portalId}/teams/{teamId}/assigned-roles

        Args:
            entity_id: str
            entity_region: Region of the entity.
            entity_type_name: str
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            role_name: str
            portalId: ID of the portal.
            teamId: ID of the team.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about the role assignment.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.teams.assigned_roles.create(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            entity_id="18ee2573-dec0-4b83-be99-fa7700bcdc61",
            entity_region="us",
            entity_type_name="Services",
            page_number=1,
            page_size=10,
            role_name="API Consumer",
        )
        ```
        """
        _query: QueryParams = {}
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
        _json = to_encodable(
            item={
                "entity_id": entity_id,
                "entity_region": entity_region,
                "entity_type_name": entity_type_name,
                "role_name": role_name,
            },
            dump_with=params._SerializerPortalAssignRoleRequest,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/portals/{portal_id}/teams/{team_id}/assigned-roles",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            json=_json,
            cast_to=models.PortalAssignedRoleResponse,
            request_options=request_options or default_request_options(),
        )
