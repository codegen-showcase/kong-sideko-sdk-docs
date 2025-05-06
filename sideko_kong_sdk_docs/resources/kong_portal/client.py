from sideko_kong_sdk_docs.core import AsyncBaseClient, SyncBaseClient
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


class KongPortalClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.portals = PortalsClient(base_client=self._base_client)
        self.applications = ApplicationsClient(base_client=self._base_client)
        self.portal_roles = PortalRolesClient(base_client=self._base_client)


class AsyncKongPortalClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.portals = AsyncPortalsClient(base_client=self._base_client)
        self.applications = AsyncApplicationsClient(base_client=self._base_client)
        self.portal_roles = AsyncPortalRolesClient(base_client=self._base_client)
