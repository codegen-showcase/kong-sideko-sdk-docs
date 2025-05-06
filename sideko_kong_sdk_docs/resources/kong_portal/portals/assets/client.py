from sideko_kong_sdk_docs.core import AsyncBaseClient, SyncBaseClient
from sideko_kong_sdk_docs.resources.kong_portal.portals.assets.favicon import (
    AsyncFaviconClient,
    FaviconClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.assets.logo import (
    AsyncLogoClient,
    LogoClient,
)


class AssetsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.favicon = FaviconClient(base_client=self._base_client)
        self.logo = LogoClient(base_client=self._base_client)


class AsyncAssetsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.favicon = AsyncFaviconClient(base_client=self._base_client)
        self.logo = AsyncLogoClient(base_client=self._base_client)
