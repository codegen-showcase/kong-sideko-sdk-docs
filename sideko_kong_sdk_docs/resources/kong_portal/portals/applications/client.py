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
from sideko_kong_sdk_docs.resources.kong_portal.portals.applications.registrations import (
    AsyncRegistrationsClient,
    RegistrationsClient,
)
from sideko_kong_sdk_docs.types import models, params


class ApplicationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.registrations = RegistrationsClient(base_client=self._base_client)

    def delete(
        self,
        *,
        application_id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Application by Portal

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Delete a single application in this portal, along with its registrations and credentials.

        DELETE /portals/{portalId}/applications/{applicationId}

        Args:
            applicationId: ID of the application.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            The application has been deleted.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.applications.delete(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/applications/{application_id}",
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
            typing.Optional[params.KongPortalPortalsApplicationsListFilter],
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
    ) -> models.ListApplicationsResponse:
        """
        List Applications

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists applications in this portal. Each application can be registered for various APIs, issuing credentials for API access. If using DCR, an application will be linked to an Identity Provider's application by its `client_id`.

        GET /portals/{portalId}/applications

        Args:
            filter: Filter applications returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            sort: Sorts a collection of applications. Supported sort attributes are:
          - created_at
          - developer_id
          - name

            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of applications in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.applications.list(
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
                    dump_with=params._SerializerKongPortalPortalsApplicationsListFilter,
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
            path=f"/portals/{portal_id}/applications",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListApplicationsResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        application_id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.ApplicationObj0, models.ApplicationObj1]:
        """
        Fetch Application by Portal

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the configuration of a single application in this portal. If an application is linked to a DCR Provider, the `dcr_provider.id` and `client_id` can be used to correlate it. An application manages a set of credentials and registrations for specific APIs.

        GET /portals/{portalId}/applications/{applicationId}

        Args:
            applicationId: ID of the application.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about an application in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.applications.get(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/applications/{application_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=typing.Union[models.ApplicationObj0, models.ApplicationObj1],
            request_options=request_options or default_request_options(),
        )


class AsyncApplicationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.registrations = AsyncRegistrationsClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        application_id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Application by Portal

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Delete a single application in this portal, along with its registrations and credentials.

        DELETE /portals/{portalId}/applications/{applicationId}

        Args:
            applicationId: ID of the application.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            The application has been deleted.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.applications.delete(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}/applications/{application_id}",
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
            typing.Optional[params.KongPortalPortalsApplicationsListFilter],
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
    ) -> models.ListApplicationsResponse:
        """
        List Applications

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists applications in this portal. Each application can be registered for various APIs, issuing credentials for API access. If using DCR, an application will be linked to an Identity Provider's application by its `client_id`.

        GET /portals/{portalId}/applications

        Args:
            filter: Filter applications returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            sort: Sorts a collection of applications. Supported sort attributes are:
          - created_at
          - developer_id
          - name

            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of applications in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.applications.list(
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
                    dump_with=params._SerializerKongPortalPortalsApplicationsListFilter,
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
            path=f"/portals/{portal_id}/applications",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.ListApplicationsResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        application_id: str,
        portal_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.ApplicationObj0, models.ApplicationObj1]:
        """
        Fetch Application by Portal

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the configuration of a single application in this portal. If an application is linked to a DCR Provider, the `dcr_provider.id` and `client_id` can be used to correlate it. An application manages a set of credentials and registrations for specific APIs.

        GET /portals/{portalId}/applications/{applicationId}

        Args:
            applicationId: ID of the application.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about an application in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.applications.get(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/applications/{application_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=typing.Union[models.ApplicationObj0, models.ApplicationObj1],
            request_options=request_options or default_request_options(),
        )
