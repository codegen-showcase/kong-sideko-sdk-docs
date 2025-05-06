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


class TeamGroupMappingsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        portal_id: str,
        page_number: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalTeamGroupMappingResponse:
        """
        List Team Group Mappings

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists mappings between Konnect portal teams and Identity Provider (IdP) groups. Returns a 400 error if an IdP has not yet been configured.

        GET /portals/{portalId}/identity-provider/team-group-mappings

        Args:
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated collection of mappings grouped by team ID.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.identity_provider.team_group_mappings.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
            path=f"/portals/{portal_id}/identity-provider/team-group-mappings",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.PortalTeamGroupMappingResponse,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        portal_id: str,
        data: typing.Union[
            typing.Optional[
                typing.List[params.PortalTeamGroupMappingsUpdateRequestDataItem]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalTeamGroupMappingResponse:
        """
        Update Team Group Mappings

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Allows partial updates to the mappings between Konnect portal teams and Identity Provider (IdP) groups. The request body must be keyed on team ID. For a given team ID, the given group list is a complete replacement. To remove all mappings for a given team, provide an empty group list.
        Returns a 400 error if an IdP has not yet been configured, or if a team ID in the request body is not found or is not a UUID.

        PATCH /portals/{portalId}/identity-provider/team-group-mappings

        Args:
            data: The IdP groups to map to the given team.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated collection of mappings grouped by team ID.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.identity_provider.team_group_mappings.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            data=[
                {
                    "groups": ["Service Developer"],
                    "team_id": "af91db4c-6e51-403e-a2bf-33d27ae50c0a",
                },
                {
                    "groups": ["Service Owner"],
                    "team_id": "bc11db4c-6e51-403e-a2bf-33d27ae50c0a",
                },
            ],
        )
        ```
        """
        _json = to_encodable(
            item={"data": data},
            dump_with=params._SerializerPortalTeamGroupMappingsUpdateRequest,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/identity-provider/team-group-mappings",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalTeamGroupMappingResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncTeamGroupMappingsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        portal_id: str,
        page_number: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalTeamGroupMappingResponse:
        """
        List Team Group Mappings

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists mappings between Konnect portal teams and Identity Provider (IdP) groups. Returns a 400 error if an IdP has not yet been configured.

        GET /portals/{portalId}/identity-provider/team-group-mappings

        Args:
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated collection of mappings grouped by team ID.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.identity_provider.team_group_mappings.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
            path=f"/portals/{portal_id}/identity-provider/team-group-mappings",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.PortalTeamGroupMappingResponse,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        portal_id: str,
        data: typing.Union[
            typing.Optional[
                typing.List[params.PortalTeamGroupMappingsUpdateRequestDataItem]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalTeamGroupMappingResponse:
        """
        Update Team Group Mappings

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Allows partial updates to the mappings between Konnect portal teams and Identity Provider (IdP) groups. The request body must be keyed on team ID. For a given team ID, the given group list is a complete replacement. To remove all mappings for a given team, provide an empty group list.
        Returns a 400 error if an IdP has not yet been configured, or if a team ID in the request body is not found or is not a UUID.

        PATCH /portals/{portalId}/identity-provider/team-group-mappings

        Args:
            data: The IdP groups to map to the given team.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated collection of mappings grouped by team ID.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.identity_provider.team_group_mappings.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            data=[
                {
                    "groups": ["Service Developer"],
                    "team_id": "af91db4c-6e51-403e-a2bf-33d27ae50c0a",
                },
                {
                    "groups": ["Service Owner"],
                    "team_id": "bc11db4c-6e51-403e-a2bf-33d27ae50c0a",
                },
            ],
        )
        ```
        """
        _json = to_encodable(
            item={"data": data},
            dump_with=params._SerializerPortalTeamGroupMappingsUpdateRequest,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/identity-provider/team-group-mappings",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalTeamGroupMappingResponse,
            request_options=request_options or default_request_options(),
        )
