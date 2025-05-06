import httpx
import typing

from sideko_kong_sdk_docs.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)


class WebhookClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def vercel(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        webhooks sent to sideko by vercel

        POST /webhook/vercel

        Args:
            data: typing.Dict[str, typing.Any]
            request_options: Additional options to customize the HTTP request

        Returns:
            the webhook has been verified & accepted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sideko.webhook.vercel(data={})
        ```
        """
        _json = to_encodable(item=data, dump_with=typing.Dict[str, typing.Any])
        return self._base_client.request(
            method="POST",
            path="/webhook/vercel",
            service_name="sideko",
            auth_names=["ApiKeyAuth", "CookieAuth"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )


class AsyncWebhookClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def vercel(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        webhooks sent to sideko by vercel

        POST /webhook/vercel

        Args:
            data: typing.Dict[str, typing.Any]
            request_options: Additional options to customize the HTTP request

        Returns:
            the webhook has been verified & accepted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sideko.webhook.vercel(data={})
        ```
        """
        _json = to_encodable(item=data, dump_with=typing.Dict[str, typing.Any])
        return await self._base_client.request(
            method="POST",
            path="/webhook/vercel",
            service_name="sideko",
            auth_names=["ApiKeyAuth", "CookieAuth"],
            json=_json,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )
