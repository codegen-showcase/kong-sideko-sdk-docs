import typing

from sideko_kong_sdk_docs.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from sideko_kong_sdk_docs.types import models


class ApplicationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        application_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.ApplicationObj0, models.ApplicationObj1]:
        """
        Fetch Application

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the configuration of a single application in any portal. If an application is linked to a DCR Provider, the `dcr_provider.id` and `client_id` can be used to correlate it. An application manages a set of credentials and registrations for specific APIs.

        GET /applications/{applicationId}

        Args:
            applicationId: ID of the application.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about an application in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.applications.get(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/applications/{application_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=typing.Union[models.ApplicationObj0, models.ApplicationObj1],
            request_options=request_options or default_request_options(),
        )


class AsyncApplicationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        application_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.ApplicationObj0, models.ApplicationObj1]:
        """
        Fetch Application

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the configuration of a single application in any portal. If an application is linked to a DCR Provider, the `dcr_provider.id` and `client_id` can be used to correlate it. An application manages a set of credentials and registrations for specific APIs.

        GET /applications/{applicationId}

        Args:
            applicationId: ID of the application.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about an application in a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.applications.get(
            application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/applications/{application_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=typing.Union[models.ApplicationObj0, models.ApplicationObj1],
            request_options=request_options or default_request_options(),
        )
