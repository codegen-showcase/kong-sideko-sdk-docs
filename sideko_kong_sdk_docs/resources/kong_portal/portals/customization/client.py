import typing

from sideko_kong_sdk_docs.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from sideko_kong_sdk_docs.types import models, params


class CustomizationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.PortalCustomization:
        """
        Get Customization

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the portal customization options.

        GET /portals/{portalId}/customization

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            The current customization options for a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.customization.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/customization",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalCustomization,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        portal_id: str,
        css: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        js: typing.Union[
            typing.Optional[params.PortalCustomizationJs], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        layout: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        menu: typing.Union[
            typing.Optional[params.PortalCustomizationMenu], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        robots: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        spec_renderer: typing.Union[
            typing.Optional[params.PortalCustomizationSpecRenderer], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        theme: typing.Union[
            typing.Optional[params.PortalCustomizationTheme], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalCustomization:
        """
        Update Customization

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Update the portal customization options, merging properties.

        PATCH /portals/{portalId}/customization

        Args:
            css: typing.Optional[str]
            js: PortalCustomizationJs
            layout: str
            menu: PortalCustomizationMenu
            robots: typing.Optional[str]
            spec_renderer: PortalCustomizationSpecRenderer
            theme: PortalCustomizationTheme
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            The current customization options for a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.customization.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _json = to_encodable(
            item={
                "css": css,
                "js": js,
                "layout": layout,
                "menu": menu,
                "robots": robots,
                "spec_renderer": spec_renderer,
                "theme": theme,
            },
            dump_with=params._SerializerPortalCustomization,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/customization",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalCustomization,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        portal_id: str,
        css: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        js: typing.Union[
            typing.Optional[params.PortalCustomizationJs], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        layout: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        menu: typing.Union[
            typing.Optional[params.PortalCustomizationMenu], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        robots: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        spec_renderer: typing.Union[
            typing.Optional[params.PortalCustomizationSpecRenderer], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        theme: typing.Union[
            typing.Optional[params.PortalCustomizationTheme], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalCustomization:
        """
        Replace Customization

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Replace the portal customization options.

        PUT /portals/{portalId}/customization

        Args:
            css: typing.Optional[str]
            js: PortalCustomizationJs
            layout: str
            menu: PortalCustomizationMenu
            robots: typing.Optional[str]
            spec_renderer: PortalCustomizationSpecRenderer
            theme: PortalCustomizationTheme
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            The current customization options for a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.customization.update(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _json = to_encodable(
            item={
                "css": css,
                "js": js,
                "layout": layout,
                "menu": menu,
                "robots": robots,
                "spec_renderer": spec_renderer,
                "theme": theme,
            },
            dump_with=params._SerializerPortalCustomization,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/portals/{portal_id}/customization",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalCustomization,
            request_options=request_options or default_request_options(),
        )


class AsyncCustomizationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.PortalCustomization:
        """
        Get Customization

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the portal customization options.

        GET /portals/{portalId}/customization

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            The current customization options for a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.customization.list(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}/customization",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.PortalCustomization,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        portal_id: str,
        css: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        js: typing.Union[
            typing.Optional[params.PortalCustomizationJs], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        layout: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        menu: typing.Union[
            typing.Optional[params.PortalCustomizationMenu], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        robots: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        spec_renderer: typing.Union[
            typing.Optional[params.PortalCustomizationSpecRenderer], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        theme: typing.Union[
            typing.Optional[params.PortalCustomizationTheme], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalCustomization:
        """
        Update Customization

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Update the portal customization options, merging properties.

        PATCH /portals/{portalId}/customization

        Args:
            css: typing.Optional[str]
            js: PortalCustomizationJs
            layout: str
            menu: PortalCustomizationMenu
            robots: typing.Optional[str]
            spec_renderer: PortalCustomizationSpecRenderer
            theme: PortalCustomizationTheme
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            The current customization options for a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.customization.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _json = to_encodable(
            item={
                "css": css,
                "js": js,
                "layout": layout,
                "menu": menu,
                "robots": robots,
                "spec_renderer": spec_renderer,
                "theme": theme,
            },
            dump_with=params._SerializerPortalCustomization,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}/customization",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalCustomization,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        portal_id: str,
        css: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        js: typing.Union[
            typing.Optional[params.PortalCustomizationJs], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        layout: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        menu: typing.Union[
            typing.Optional[params.PortalCustomizationMenu], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        robots: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        spec_renderer: typing.Union[
            typing.Optional[params.PortalCustomizationSpecRenderer], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        theme: typing.Union[
            typing.Optional[params.PortalCustomizationTheme], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PortalCustomization:
        """
        Replace Customization

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Replace the portal customization options.

        PUT /portals/{portalId}/customization

        Args:
            css: typing.Optional[str]
            js: PortalCustomizationJs
            layout: str
            menu: PortalCustomizationMenu
            robots: typing.Optional[str]
            spec_renderer: PortalCustomizationSpecRenderer
            theme: PortalCustomizationTheme
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            The current customization options for a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.customization.update(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _json = to_encodable(
            item={
                "css": css,
                "js": js,
                "layout": layout,
                "menu": menu,
                "robots": robots,
                "spec_renderer": spec_renderer,
                "theme": theme,
            },
            dump_with=params._SerializerPortalCustomization,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/portals/{portal_id}/customization",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.PortalCustomization,
            request_options=request_options or default_request_options(),
        )
