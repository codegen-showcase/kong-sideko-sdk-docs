from sideko_kong_sdk_docs.core import AsyncBaseClient, SyncBaseClient
from sideko_kong_sdk_docs.resources.kong_portal.portals.identity_provider.team_group_mappings import (
    AsyncTeamGroupMappingsClient,
    TeamGroupMappingsClient,
)


class IdentityProviderClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.team_group_mappings = TeamGroupMappingsClient(
            base_client=self._base_client
        )


class AsyncIdentityProviderClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.team_group_mappings = AsyncTeamGroupMappingsClient(
            base_client=self._base_client
        )
