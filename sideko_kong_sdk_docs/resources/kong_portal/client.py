from sideko_kong_sdk_docs.core import (
    AsyncBaseClient,
    SyncBaseClient,
    RequestOptions,
    default_request_options,
)
from sideko_kong_sdk_docs.resources.kong_portal.applications import (
    ApplicationsClient,
    AsyncApplicationsClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portal_roles import (
    AsyncPortalRolesClient,
    PortalRolesClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals import (
    AsyncPortalsClient,
    PortalsClient,
)
import typing
from sideko_kong_sdk_docs.types.models.apis_specifications_get_response import (
    ApisSpecificationsGetResponse,
)


class KongPortalClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.portals = PortalsClient(base_client=self._base_client)
        self.applications = ApplicationsClient(base_client=self._base_client)
        self.portal_roles = PortalRolesClient(base_client=self._base_client)

    def get_spec(
        self,
        *,
        api_id: str,
        spec_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApisSpecificationsGetResponse:
        """
        Fetch API Specification
        **THIS IS A CUSTOM FUNCTION ADDED TO A SIDEKO GENERATED SDK**

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Fetches the specification of an API.

        GET /apis/{apiId}/specifications/{specId}

        Args:
            apiId: The UUID API identifier
            specId: The API specification identifier
            request_options: Additional options to customize the HTTP request

        Returns:
            API specification

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.apis.specifications.get(
            api_id="9f5061ce-78f6-4452-9108-ad7c02821fd5",
            spec_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/apis/{api_id}/specifications/{spec_id}",
            auth_names=[
                "konnectAccessToken",
                "personalAccessToken",
                "systemAccountAccessToken",
            ],
            cast_to=ApisSpecificationsGetResponse,
            service_name="kong_portal",
            request_options=request_options or default_request_options(),
        )


class AsyncKongPortalClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.portals = AsyncPortalsClient(base_client=self._base_client)
        self.applications = AsyncApplicationsClient(base_client=self._base_client)
        self.portal_roles = AsyncPortalRolesClient(base_client=self._base_client)
