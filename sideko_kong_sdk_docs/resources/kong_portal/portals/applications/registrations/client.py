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


class RegistrationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        application_id: str,
        portal_id: str,
        registration_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Registration

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes an application registration, which if currently approved will immediately block API traffic to the API.
        Note: Developers can request a new application registration for the given API as long as they have RBAC access to consume.

        DELETE /portals/{portalId}/applications/{applicationId}/registrations/{registrationId}

        Args:
            applicationId: ID of the application.
            portalId: ID of the portal.
            registrationId: ID of the application registration.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.applications.registrations.delete(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            registration_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/applications/{application_id}/registrations/{registration_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        application_id: str,
        portal_id: str,
        filter: typing.Union[
            typing.Optional[
                params.KongPortalPortalsApplicationsRegistrationsListFilter
            ],
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
    ) -> models.ListApplicationRegistrationsResponse:
        """
        List Registrations by Application

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists each API that this application is registered for and their current status (e.g., pending, approved, rejected, revoked).

        GET /portals/{portalId}/applications/{applicationId}/registrations

        Args:
            filter: Filter application registrations returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            sort: Sorts a set of registrations for an application. Supported sort attributes are:
          - created_at
          - updated_at
          - status

            applicationId: ID of the application.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of application registrations.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.applications.registrations.list(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
                    dump_with=params._SerializerKongPortalPortalsApplicationsRegistrationsListFilter,
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
            path=f"/portals/{portal_id}/applications/{application_id}/registrations",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListApplicationRegistrationsResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        application_id: str,
        portal_id: str,
        registration_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApplicationRegistration:
        """
        Fetch Registration

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns information about an application's registration status for a particular API.

        GET /portals/{portalId}/applications/{applicationId}/registrations/{registrationId}

        Args:
            applicationId: ID of the application.
            portalId: ID of the portal.
            registrationId: ID of the application registration.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about an application registration.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.applications.registrations.get(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            registration_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/applications/{application_id}/registrations/{registration_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.ApplicationRegistration,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        application_id: str,
        portal_id: str,
        registration_id: str,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["approved", "pending", "rejected", "revoked"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApplicationRegistration:
        """
        Update Registration

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the status of a particular application registration to an API. Approved application registrations will allow API traffic to the corresponding API. Revoked, rejected, or pending will not allow API traffic.

        PATCH /portals/{portalId}/applications/{applicationId}/registrations/{registrationId}

        Args:
            status: The status of an application registration request. Each registration is linked to a single API, and application credentials will not grant access to the API until the registration is approved.
        Pending, revoked, and rejected registrations will not provide access to the API.
            applicationId: ID of the application.
            portalId: ID of the portal.
            registrationId: ID of the application registration.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about the application registration being updated.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.applications.registrations.patch(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            registration_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            status="approved",
        )
        ```
        """
        _json = to_encodable(
            item={"status": status},
            dump_with=params._SerializerUpdateApplicationRegistrationRequest,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/applications/{application_id}/registrations/{registration_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.ApplicationRegistration,
            request_options=request_options or default_request_options(),
        )


class AsyncRegistrationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        application_id: str,
        portal_id: str,
        registration_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Registration

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes an application registration, which if currently approved will immediately block API traffic to the API.
        Note: Developers can request a new application registration for the given API as long as they have RBAC access to consume.

        DELETE /portals/{portalId}/applications/{applicationId}/registrations/{registrationId}

        Args:
            applicationId: ID of the application.
            portalId: ID of the portal.
            registrationId: ID of the application registration.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.applications.registrations.delete(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            registration_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/applications/{application_id}/registrations/{registration_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        application_id: str,
        portal_id: str,
        filter: typing.Union[
            typing.Optional[
                params.KongPortalPortalsApplicationsRegistrationsListFilter
            ],
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
    ) -> models.ListApplicationRegistrationsResponse:
        """
        List Registrations by Application

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists each API that this application is registered for and their current status (e.g., pending, approved, rejected, revoked).

        GET /portals/{portalId}/applications/{applicationId}/registrations

        Args:
            filter: Filter application registrations returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            sort: Sorts a set of registrations for an application. Supported sort attributes are:
          - created_at
          - updated_at
          - status

            applicationId: ID of the application.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of application registrations.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.applications.registrations.list(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
                    dump_with=params._SerializerKongPortalPortalsApplicationsRegistrationsListFilter,
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
            path=f"/portals/{portal_id}/applications/{application_id}/registrations",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListApplicationRegistrationsResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        application_id: str,
        portal_id: str,
        registration_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApplicationRegistration:
        """
        Fetch Registration

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns information about an application's registration status for a particular API.

        GET /portals/{portalId}/applications/{applicationId}/registrations/{registrationId}

        Args:
            applicationId: ID of the application.
            portalId: ID of the portal.
            registrationId: ID of the application registration.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about an application registration.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.applications.registrations.get(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            registration_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/applications/{application_id}/registrations/{registration_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.ApplicationRegistration,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        application_id: str,
        portal_id: str,
        registration_id: str,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["approved", "pending", "rejected", "revoked"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApplicationRegistration:
        """
        Update Registration

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the status of a particular application registration to an API. Approved application registrations will allow API traffic to the corresponding API. Revoked, rejected, or pending will not allow API traffic.

        PATCH /portals/{portalId}/applications/{applicationId}/registrations/{registrationId}

        Args:
            status: The status of an application registration request. Each registration is linked to a single API, and application credentials will not grant access to the API until the registration is approved.
        Pending, revoked, and rejected registrations will not provide access to the API.
            applicationId: ID of the application.
            portalId: ID of the portal.
            registrationId: ID of the application registration.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about the application registration being updated.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.applications.registrations.patch(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            registration_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            status="approved",
        )
        ```
        """
        _json = to_encodable(
            item={"status": status},
            dump_with=params._SerializerUpdateApplicationRegistrationRequest,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/applications/{application_id}/registrations/{registration_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.ApplicationRegistration,
            request_options=request_options or default_request_options(),
        )
