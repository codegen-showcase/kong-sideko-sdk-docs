import httpx
import typing

from sideko_kong_sdk_docs.core import (
    AsyncBaseClient,
    AuthBearer,
    AuthKeyCookie,
    AuthKeyHeader,
    SyncBaseClient,
)
from sideko_kong_sdk_docs.environment import (
    DEFAULT,
    Environment,
    ServerGroup,
    _get_base_url,
)
from sideko_kong_sdk_docs.resources.kong_portal import (
    AsyncKongPortalClient,
    KongPortalClient,
)
from sideko_kong_sdk_docs.resources.sideko import AsyncSidekoClient, SidekoClient


class Client:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        environment: ServerGroup = DEFAULT,
        sideko_key: typing.Optional[str] = None,
        sideko_cookie: typing.Optional[str] = None,
        kong_pat: typing.Optional[str] = None,
        kong_sys_token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url={
                "sideko": _get_base_url(
                    environment, "sideko", Environment.SIDEKO_PROD.value
                ),
                "kong_portal": _get_base_url(
                    environment, "kong_portal", Environment.KONG_US.value
                ),
            },
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "ApiKeyAuth", AuthKeyHeader(header_name="x-sideko-key", val=sideko_key)
        )
        self._base_client.register_auth(
            "CookieAuth", AuthKeyCookie(cookie_name="SIDEKO_SESSION", val=sideko_cookie)
        )
        self._base_client.register_auth("personalAccessToken", AuthBearer(val=kong_pat))
        self._base_client.register_auth(
            "systemAccountAccessToken", AuthBearer(val=kong_sys_token)
        )
        self.sideko = SidekoClient(base_client=self._base_client)
        self.kong_portal = KongPortalClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        environment: ServerGroup = DEFAULT,
        sideko_key: typing.Optional[str] = None,
        sideko_cookie: typing.Optional[str] = None,
        kong_pat: typing.Optional[str] = None,
        kong_sys_token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url={
                "sideko": _get_base_url(
                    environment, "sideko", Environment.SIDEKO_PROD.value
                ),
                "kong_portal": _get_base_url(
                    environment, "kong_portal", Environment.KONG_US.value
                ),
            },
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "ApiKeyAuth", AuthKeyHeader(header_name="x-sideko-key", val=sideko_key)
        )
        self._base_client.register_auth(
            "CookieAuth", AuthKeyCookie(cookie_name="SIDEKO_SESSION", val=sideko_cookie)
        )
        self._base_client.register_auth("personalAccessToken", AuthBearer(val=kong_pat))
        self._base_client.register_auth(
            "systemAccountAccessToken", AuthBearer(val=kong_sys_token)
        )
        self.sideko = AsyncSidekoClient(base_client=self._base_client)
        self.kong_portal = AsyncKongPortalClient(base_client=self._base_client)
