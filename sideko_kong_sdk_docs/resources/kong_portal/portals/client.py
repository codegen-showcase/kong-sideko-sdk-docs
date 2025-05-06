import typing
import typing_extensions

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
from sideko_kong_sdk_docs.resources.kong_portal.portals.application_registrations import (
    ApplicationRegistrationsClient,
    AsyncApplicationRegistrationsClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.applications import (
    ApplicationsClient,
    AsyncApplicationsClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.assets import (
    AssetsClient,
    AsyncAssetsClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.authentication_settings import (
    AsyncAuthenticationSettingsClient,
    AuthenticationSettingsClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.custom_domain import (
    AsyncCustomDomainClient,
    CustomDomainClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.customization import (
    AsyncCustomizationClient,
    CustomizationClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.default_content import (
    AsyncDefaultContentClient,
    DefaultContentClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.developers import (
    AsyncDevelopersClient,
    DevelopersClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.identity_provider import (
    AsyncIdentityProviderClient,
    IdentityProviderClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.identity_providers import (
    AsyncIdentityProvidersClient,
    IdentityProvidersClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.pages import (
    AsyncPagesClient,
    PagesClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.snippets import (
    AsyncSnippetsClient,
    SnippetsClient,
)
from sideko_kong_sdk_docs.resources.kong_portal.portals.teams import (
    AsyncTeamsClient,
    TeamsClient,
)
from sideko_kong_sdk_docs.types import models, params


class PortalsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.applications = ApplicationsClient(base_client=self._base_client)
        self.custom_domain = CustomDomainClient(base_client=self._base_client)
        self.developers = DevelopersClient(base_client=self._base_client)
        self.identity_providers = IdentityProvidersClient(base_client=self._base_client)
        self.pages = PagesClient(base_client=self._base_client)
        self.snippets = SnippetsClient(base_client=self._base_client)
        self.teams = TeamsClient(base_client=self._base_client)
        self.application_registrations = ApplicationRegistrationsClient(
            base_client=self._base_client
        )
        self.assets = AssetsClient(base_client=self._base_client)
        self.authentication_settings = AuthenticationSettingsClient(
            base_client=self._base_client
        )
        self.customization = CustomizationClient(base_client=self._base_client)
        self.identity_provider = IdentityProviderClient(base_client=self._base_client)
        self.default_content = DefaultContentClient(base_client=self._base_client)

    def delete(
        self,
        *,
        portal_id: str,
        force: typing.Union[
            typing.Optional[typing_extensions.Literal["false", "true"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Portal

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes a single portal, along with all related entities.

        DELETE /portals/{portalId}

        Args:
            force: If true, the portal will be deleted, automatically deleting all API publications. If the force param is not set, the deletion will only succeed if there are no APIs currently published.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.delete(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(force, type_utils.NotGiven):
            encode_query_param(
                _query,
                "force",
                to_encodable(
                    item=force, dump_with=typing_extensions.Literal["false", "true"]
                ),
                style="form",
                explode=True,
            )
        self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        filter: typing.Union[
            typing.Optional[params.PortalFilterParameters], type_utils.NotGiven
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
    ) -> models.KongPortalPortalsListResponse:
        """
        List Portals

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists developer portals defined in this region for this organization. Each developer portal is available at a unique address and has isolated configuration, customization, developers, and applications.

        GET /portals

        Args:
            filter: Filter portals returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            sort: Sorts a collection of portals. Supported sort attributes are:
          - name
          - description
          - authentication_enabled
          - rbac_enabled
          - auto_approve_applications
          - auto_approve_developers
          - default_domain
          - canonical_domain
          - created_at
          - updated_at

            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of portals in the current region of an organization.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.list(page_number=1, page_size=10)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(filter, type_utils.NotGiven):
            encode_query_param(
                _query,
                "filter",
                to_encodable(
                    item=filter, dump_with=params._SerializerPortalFilterParameters
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
            path="/portals",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.KongPortalPortalsListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.KongPortalPortalsGetResponse:
        """
        Fetch Portal

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the configuration for a single developer portal, including  the current visibility, access, and domain settings.

        GET /portals/{portalId}

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.get(portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.KongPortalPortalsGetResponse,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        portal_id: str,
        authentication_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auto_approve_applications: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auto_approve_developers: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        canonical_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_api_visibility: typing.Union[
            typing.Optional[typing_extensions.Literal["private", "public"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        default_application_auth_strategy_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_page_visibility: typing.Union[
            typing.Optional[typing_extensions.Literal["private", "public"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        display_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        labels: typing.Union[
            typing.Optional[params.LabelsUpdate], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        rbac_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.KongPortalPortalsPatchResponse:
        """
        Update Portal

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the configuration for a single portal including the visibility, access, and custom domain settings.

        PATCH /portals/{portalId}

        Args:
            authentication_enabled: Whether the portal supports developer authentication. If disabled, developers cannot register for accounts or create applications.
            auto_approve_applications: Whether requests from applications to register for APIs will be automatically approved, or if they will be set to pending until approved by an admin.
            auto_approve_developers: Whether developer account registrations will be automatically approved, or if they will be set to pending until approved by an admin.
            canonical_domain: The canonical domain of the developer portal
            created_at: An ISO-8601 timestamp representation of entity creation date.
            default_api_visibility: The default visibility of APIs in the portal. If set to `public`, newly published APIs are visible to unauthenticated developers. If set to `private`, newly published APIs are hidden from unauthenticated developers.
            default_application_auth_strategy_id: The default authentication strategy for APIs published to the portal. Newly published APIs will use this authentication strategy unless overridden during publication. If set to `null`, API publications will not use an authentication strategy unless set during publication. DCR support for Auth Strategies is currently in development.
            default_domain: The domain assigned to the portal by Konnect. This is the default place to access the portal and its API if not using a `custom_domain``.
            default_page_visibility: The default visibility of pages in the portal. If set to `public`, newly created pages are visible to unauthenticated developers. If set to `private`, newly created pages are hidden from unauthenticated developers.
            description: A description of the portal.
            display_name: The display name of the portal. This value will be the portal's `name` in Portal API.
            id: Contains a unique identifier used for this resource.
            labels: Labels store metadata of an entity that can be used for filtering an entity list or for searching across entity types.

        Labels are intended to store **INTERNAL** metadata.

        Keys must be of length 1-63 characters, and cannot start with "kong", "konnect", "mesh", "kic", or "_".

            name: The name of the portal, used to distinguish it from other portals. Name must be unique.
            rbac_enabled: Whether the portal resources are protected by Role Based Access Control (RBAC). If enabled, developers view or register for APIs until unless assigned to teams with access to view and consume specific APIs. Authentication must be enabled to use RBAC.
            updated_at: An ISO-8601 timestamp representation of entity update date.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            authentication_enabled=False,
        )
        ```
        """
        _json = to_encodable(
            item={
                "authentication_enabled": authentication_enabled,
                "auto_approve_applications": auto_approve_applications,
                "auto_approve_developers": auto_approve_developers,
                "canonical_domain": canonical_domain,
                "created_at": created_at,
                "default_api_visibility": default_api_visibility,
                "default_application_auth_strategy_id": default_application_auth_strategy_id,
                "default_domain": default_domain,
                "default_page_visibility": default_page_visibility,
                "description": description,
                "display_name": display_name,
                "id": id,
                "labels": labels,
                "name": name,
                "rbac_enabled": rbac_enabled,
                "updated_at": updated_at,
            },
            dump_with=params._SerializerKongPortalPortalsPatchBody,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.KongPortalPortalsPatchResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        authentication_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auto_approve_applications: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auto_approve_developers: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        canonical_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_api_visibility: typing.Union[
            typing.Optional[typing_extensions.Literal["private", "public"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        default_application_auth_strategy_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_page_visibility: typing.Union[
            typing.Optional[typing_extensions.Literal["private", "public"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        display_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        labels: typing.Union[
            typing.Optional[params.LabelsUpdate], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        rbac_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.KongPortalPortalsCreateResponse:
        """
        Create Portal

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates a new developer portal scoped in this region for this organization.

        POST /portals

        Args:
            authentication_enabled: Whether the portal supports developer authentication. If disabled, developers cannot register for accounts or create applications.
            auto_approve_applications: Whether requests from applications to register for APIs will be automatically approved, or if they will be set to pending until approved by an admin.
            auto_approve_developers: Whether developer account registrations will be automatically approved, or if they will be set to pending until approved by an admin.
            canonical_domain: The canonical domain of the developer portal
            created_at: An ISO-8601 timestamp representation of entity creation date.
            default_api_visibility: The default visibility of APIs in the portal. If set to `public`, newly published APIs are visible to unauthenticated developers. If set to `private`, newly published APIs are hidden from unauthenticated developers.
            default_application_auth_strategy_id: The default authentication strategy for APIs published to the portal. Newly published APIs will use this authentication strategy unless overridden during publication. If set to `null`, API publications will not use an authentication strategy unless set during publication. DCR support for Auth Strategies is currently in development.
            default_domain: The domain assigned to the portal by Konnect. This is the default place to access the portal and its API if not using a `custom_domain``.
            default_page_visibility: The default visibility of pages in the portal. If set to `public`, newly created pages are visible to unauthenticated developers. If set to `private`, newly created pages are hidden from unauthenticated developers.
            description: A description of the portal.
            display_name: The display name of the portal. This value will be the portal's `name` in Portal API.
            id: Contains a unique identifier used for this resource.
            labels: Labels store metadata of an entity that can be used for filtering an entity list or for searching across entity types.

        Labels are intended to store **INTERNAL** metadata.

        Keys must be of length 1-63 characters, and cannot start with "kong", "konnect", "mesh", "kic", or "_".

            rbac_enabled: Whether the portal resources are protected by Role Based Access Control (RBAC). If enabled, developers view or register for APIs until unless assigned to teams with access to view and consume specific APIs. Authentication must be enabled to use RBAC.
            updated_at: An ISO-8601 timestamp representation of entity update date.
            name: The name of the portal, used to distinguish it from other portals. Name must be unique.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.kong_portal.portals.create(
            name="MyDevPortal", authentication_enabled=False
        )
        ```
        """
        _json = to_encodable(
            item={
                "authentication_enabled": authentication_enabled,
                "auto_approve_applications": auto_approve_applications,
                "auto_approve_developers": auto_approve_developers,
                "canonical_domain": canonical_domain,
                "created_at": created_at,
                "default_api_visibility": default_api_visibility,
                "default_application_auth_strategy_id": default_application_auth_strategy_id,
                "default_domain": default_domain,
                "default_page_visibility": default_page_visibility,
                "description": description,
                "display_name": display_name,
                "id": id,
                "labels": labels,
                "rbac_enabled": rbac_enabled,
                "updated_at": updated_at,
                "name": name,
            },
            dump_with=params._SerializerKongPortalPortalsCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/portals",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.KongPortalPortalsCreateResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncPortalsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.applications = AsyncApplicationsClient(base_client=self._base_client)
        self.custom_domain = AsyncCustomDomainClient(base_client=self._base_client)
        self.developers = AsyncDevelopersClient(base_client=self._base_client)
        self.identity_providers = AsyncIdentityProvidersClient(
            base_client=self._base_client
        )
        self.pages = AsyncPagesClient(base_client=self._base_client)
        self.snippets = AsyncSnippetsClient(base_client=self._base_client)
        self.teams = AsyncTeamsClient(base_client=self._base_client)
        self.application_registrations = AsyncApplicationRegistrationsClient(
            base_client=self._base_client
        )
        self.assets = AsyncAssetsClient(base_client=self._base_client)
        self.authentication_settings = AsyncAuthenticationSettingsClient(
            base_client=self._base_client
        )
        self.customization = AsyncCustomizationClient(base_client=self._base_client)
        self.identity_provider = AsyncIdentityProviderClient(
            base_client=self._base_client
        )
        self.default_content = AsyncDefaultContentClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        portal_id: str,
        force: typing.Union[
            typing.Optional[typing_extensions.Literal["false", "true"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Portal

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Deletes a single portal, along with all related entities.

        DELETE /portals/{portalId}

        Args:
            force: If true, the portal will be deleted, automatically deleting all API publications. If the force param is not set, the deletion will only succeed if there are no APIs currently published.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            No Content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.delete(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(force, type_utils.NotGiven):
            encode_query_param(
                _query,
                "force",
                to_encodable(
                    item=force, dump_with=typing_extensions.Literal["false", "true"]
                ),
                style="form",
                explode=True,
            )
        await self._base_client.request(
            method="DELETE",
            path=f"/portals/{portal_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        filter: typing.Union[
            typing.Optional[params.PortalFilterParameters], type_utils.NotGiven
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
    ) -> models.KongPortalPortalsListResponse:
        """
        List Portals

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Lists developer portals defined in this region for this organization. Each developer portal is available at a unique address and has isolated configuration, customization, developers, and applications.

        GET /portals

        Args:
            filter: Filter portals returned in the response.
            page[number]: Determines which page of the entities to retrieve.
            page[size]: The maximum number of items to include per page. The last page of a collection may include fewer items.
            sort: Sorts a collection of portals. Supported sort attributes are:
          - name
          - description
          - authentication_enabled
          - rbac_enabled
          - auto_approve_applications
          - auto_approve_developers
          - default_domain
          - canonical_domain
          - created_at
          - updated_at

            request_options: Additional options to customize the HTTP request

        Returns:
            A paginated list of portals in the current region of an organization.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.list(page_number=1, page_size=10)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(filter, type_utils.NotGiven):
            encode_query_param(
                _query,
                "filter",
                to_encodable(
                    item=filter, dump_with=params._SerializerPortalFilterParameters
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
            path="/portals",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            query_params=_query,
            cast_to=models.KongPortalPortalsListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, portal_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.KongPortalPortalsGetResponse:
        """
        Fetch Portal

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Returns the configuration for a single developer portal, including  the current visibility, access, and domain settings.

        GET /portals/{portalId}

        Args:
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.get(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/portals/{portal_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            cast_to=models.KongPortalPortalsGetResponse,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        portal_id: str,
        authentication_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auto_approve_applications: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auto_approve_developers: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        canonical_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_api_visibility: typing.Union[
            typing.Optional[typing_extensions.Literal["private", "public"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        default_application_auth_strategy_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_page_visibility: typing.Union[
            typing.Optional[typing_extensions.Literal["private", "public"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        display_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        labels: typing.Union[
            typing.Optional[params.LabelsUpdate], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        rbac_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.KongPortalPortalsPatchResponse:
        """
        Update Portal

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Updates the configuration for a single portal including the visibility, access, and custom domain settings.

        PATCH /portals/{portalId}

        Args:
            authentication_enabled: Whether the portal supports developer authentication. If disabled, developers cannot register for accounts or create applications.
            auto_approve_applications: Whether requests from applications to register for APIs will be automatically approved, or if they will be set to pending until approved by an admin.
            auto_approve_developers: Whether developer account registrations will be automatically approved, or if they will be set to pending until approved by an admin.
            canonical_domain: The canonical domain of the developer portal
            created_at: An ISO-8601 timestamp representation of entity creation date.
            default_api_visibility: The default visibility of APIs in the portal. If set to `public`, newly published APIs are visible to unauthenticated developers. If set to `private`, newly published APIs are hidden from unauthenticated developers.
            default_application_auth_strategy_id: The default authentication strategy for APIs published to the portal. Newly published APIs will use this authentication strategy unless overridden during publication. If set to `null`, API publications will not use an authentication strategy unless set during publication. DCR support for Auth Strategies is currently in development.
            default_domain: The domain assigned to the portal by Konnect. This is the default place to access the portal and its API if not using a `custom_domain``.
            default_page_visibility: The default visibility of pages in the portal. If set to `public`, newly created pages are visible to unauthenticated developers. If set to `private`, newly created pages are hidden from unauthenticated developers.
            description: A description of the portal.
            display_name: The display name of the portal. This value will be the portal's `name` in Portal API.
            id: Contains a unique identifier used for this resource.
            labels: Labels store metadata of an entity that can be used for filtering an entity list or for searching across entity types.

        Labels are intended to store **INTERNAL** metadata.

        Keys must be of length 1-63 characters, and cannot start with "kong", "konnect", "mesh", "kic", or "_".

            name: The name of the portal, used to distinguish it from other portals. Name must be unique.
            rbac_enabled: Whether the portal resources are protected by Role Based Access Control (RBAC). If enabled, developers view or register for APIs until unless assigned to teams with access to view and consume specific APIs. Authentication must be enabled to use RBAC.
            updated_at: An ISO-8601 timestamp representation of entity update date.
            portalId: ID of the portal.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.patch(
            portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            authentication_enabled=False,
        )
        ```
        """
        _json = to_encodable(
            item={
                "authentication_enabled": authentication_enabled,
                "auto_approve_applications": auto_approve_applications,
                "auto_approve_developers": auto_approve_developers,
                "canonical_domain": canonical_domain,
                "created_at": created_at,
                "default_api_visibility": default_api_visibility,
                "default_application_auth_strategy_id": default_application_auth_strategy_id,
                "default_domain": default_domain,
                "default_page_visibility": default_page_visibility,
                "description": description,
                "display_name": display_name,
                "id": id,
                "labels": labels,
                "name": name,
                "rbac_enabled": rbac_enabled,
                "updated_at": updated_at,
            },
            dump_with=params._SerializerKongPortalPortalsPatchBody,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/portals/{portal_id}",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.KongPortalPortalsPatchResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        authentication_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auto_approve_applications: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auto_approve_developers: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        canonical_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_api_visibility: typing.Union[
            typing.Optional[typing_extensions.Literal["private", "public"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        default_application_auth_strategy_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_domain: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_page_visibility: typing.Union[
            typing.Optional[typing_extensions.Literal["private", "public"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        display_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        labels: typing.Union[
            typing.Optional[params.LabelsUpdate], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        rbac_enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.KongPortalPortalsCreateResponse:
        """
        Create Portal

        **Pre-release Endpoint**
        This endpoint is currently in beta and is subject to change.

        Creates a new developer portal scoped in this region for this organization.

        POST /portals

        Args:
            authentication_enabled: Whether the portal supports developer authentication. If disabled, developers cannot register for accounts or create applications.
            auto_approve_applications: Whether requests from applications to register for APIs will be automatically approved, or if they will be set to pending until approved by an admin.
            auto_approve_developers: Whether developer account registrations will be automatically approved, or if they will be set to pending until approved by an admin.
            canonical_domain: The canonical domain of the developer portal
            created_at: An ISO-8601 timestamp representation of entity creation date.
            default_api_visibility: The default visibility of APIs in the portal. If set to `public`, newly published APIs are visible to unauthenticated developers. If set to `private`, newly published APIs are hidden from unauthenticated developers.
            default_application_auth_strategy_id: The default authentication strategy for APIs published to the portal. Newly published APIs will use this authentication strategy unless overridden during publication. If set to `null`, API publications will not use an authentication strategy unless set during publication. DCR support for Auth Strategies is currently in development.
            default_domain: The domain assigned to the portal by Konnect. This is the default place to access the portal and its API if not using a `custom_domain``.
            default_page_visibility: The default visibility of pages in the portal. If set to `public`, newly created pages are visible to unauthenticated developers. If set to `private`, newly created pages are hidden from unauthenticated developers.
            description: A description of the portal.
            display_name: The display name of the portal. This value will be the portal's `name` in Portal API.
            id: Contains a unique identifier used for this resource.
            labels: Labels store metadata of an entity that can be used for filtering an entity list or for searching across entity types.

        Labels are intended to store **INTERNAL** metadata.

        Keys must be of length 1-63 characters, and cannot start with "kong", "konnect", "mesh", "kic", or "_".

            rbac_enabled: Whether the portal resources are protected by Role Based Access Control (RBAC). If enabled, developers view or register for APIs until unless assigned to teams with access to view and consume specific APIs. Authentication must be enabled to use RBAC.
            updated_at: An ISO-8601 timestamp representation of entity update date.
            name: The name of the portal, used to distinguish it from other portals. Name must be unique.
            request_options: Additional options to customize the HTTP request

        Returns:
            Details about a portal.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.kong_portal.portals.create(
            name="MyDevPortal", authentication_enabled=False
        )
        ```
        """
        _json = to_encodable(
            item={
                "authentication_enabled": authentication_enabled,
                "auto_approve_applications": auto_approve_applications,
                "auto_approve_developers": auto_approve_developers,
                "canonical_domain": canonical_domain,
                "created_at": created_at,
                "default_api_visibility": default_api_visibility,
                "default_application_auth_strategy_id": default_application_auth_strategy_id,
                "default_domain": default_domain,
                "default_page_visibility": default_page_visibility,
                "description": description,
                "display_name": display_name,
                "id": id,
                "labels": labels,
                "rbac_enabled": rbac_enabled,
                "updated_at": updated_at,
                "name": name,
            },
            dump_with=params._SerializerKongPortalPortalsCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/portals",
            service_name="kong_portal",
            auth_names=["personalAccessToken", "systemAccountAccessToken"],
            json=_json,
            cast_to=models.KongPortalPortalsCreateResponse,
            request_options=request_options or default_request_options(),
        )
