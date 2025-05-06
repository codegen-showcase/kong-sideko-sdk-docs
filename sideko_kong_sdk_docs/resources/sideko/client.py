from sideko_kong_sdk_docs.core import AsyncBaseClient, SyncBaseClient
from sideko_kong_sdk_docs.resources.sideko.api import ApiClient, AsyncApiClient
from sideko_kong_sdk_docs.resources.sideko.api_link import (
    ApiLinkClient,
    AsyncApiLinkClient,
)
from sideko_kong_sdk_docs.resources.sideko.asset import AssetClient, AsyncAssetClient
from sideko_kong_sdk_docs.resources.sideko.auth import AsyncAuthClient, AuthClient
from sideko_kong_sdk_docs.resources.sideko.cli import AsyncCliClient, CliClient
from sideko_kong_sdk_docs.resources.sideko.doc import AsyncDocClient, DocClient
from sideko_kong_sdk_docs.resources.sideko.health import AsyncHealthClient, HealthClient
from sideko_kong_sdk_docs.resources.sideko.lint import AsyncLintClient, LintClient
from sideko_kong_sdk_docs.resources.sideko.org import AsyncOrgClient, OrgClient
from sideko_kong_sdk_docs.resources.sideko.role import AsyncRoleClient, RoleClient
from sideko_kong_sdk_docs.resources.sideko.sdk import AsyncSdkClient, SdkClient
from sideko_kong_sdk_docs.resources.sideko.service_account import (
    AsyncServiceAccountClient,
    ServiceAccountClient,
)
from sideko_kong_sdk_docs.resources.sideko.user import AsyncUserClient, UserClient
from sideko_kong_sdk_docs.resources.sideko.webhook import (
    AsyncWebhookClient,
    WebhookClient,
)


class SidekoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.api = ApiClient(base_client=self._base_client)
        self.api_link = ApiLinkClient(base_client=self._base_client)
        self.doc = DocClient(base_client=self._base_client)
        self.asset = AssetClient(base_client=self._base_client)
        self.role = RoleClient(base_client=self._base_client)
        self.service_account = ServiceAccountClient(base_client=self._base_client)
        self.health = HealthClient(base_client=self._base_client)
        self.auth = AuthClient(base_client=self._base_client)
        self.cli = CliClient(base_client=self._base_client)
        self.org = OrgClient(base_client=self._base_client)
        self.sdk = SdkClient(base_client=self._base_client)
        self.user = UserClient(base_client=self._base_client)
        self.lint = LintClient(base_client=self._base_client)
        self.webhook = WebhookClient(base_client=self._base_client)


class AsyncSidekoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.api = AsyncApiClient(base_client=self._base_client)
        self.api_link = AsyncApiLinkClient(base_client=self._base_client)
        self.doc = AsyncDocClient(base_client=self._base_client)
        self.asset = AsyncAssetClient(base_client=self._base_client)
        self.role = AsyncRoleClient(base_client=self._base_client)
        self.service_account = AsyncServiceAccountClient(base_client=self._base_client)
        self.health = AsyncHealthClient(base_client=self._base_client)
        self.auth = AsyncAuthClient(base_client=self._base_client)
        self.cli = AsyncCliClient(base_client=self._base_client)
        self.org = AsyncOrgClient(base_client=self._base_client)
        self.sdk = AsyncSdkClient(base_client=self._base_client)
        self.user = AsyncUserClient(base_client=self._base_client)
        self.lint = AsyncLintClient(base_client=self._base_client)
        self.webhook = AsyncWebhookClient(base_client=self._base_client)
