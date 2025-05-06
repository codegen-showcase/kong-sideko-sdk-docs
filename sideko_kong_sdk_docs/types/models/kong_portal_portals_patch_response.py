import pydantic
import typing
import typing_extensions

from .labels import Labels


class KongPortalPortalsPatchResponse(pydantic.BaseModel):
    """
    KongPortalPortalsPatchResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    authentication_enabled: bool = pydantic.Field(
        alias="authentication_enabled",
    )
    """
    Whether the portal supports developer authentication. If disabled, developers cannot register for accounts or create applications.
    """
    auto_approve_applications: bool = pydantic.Field(
        alias="auto_approve_applications",
    )
    """
    Whether requests from applications to register for APIs will be automatically approved, or if they will be set to pending until approved by an admin.
    """
    auto_approve_developers: bool = pydantic.Field(
        alias="auto_approve_developers",
    )
    """
    Whether developer account registrations will be automatically approved, or if they will be set to pending until approved by an admin.
    """
    canonical_domain: str = pydantic.Field(
        alias="canonical_domain",
    )
    """
    The canonical domain of the developer portal
    """
    created_at: str = pydantic.Field(
        alias="created_at",
    )
    """
    An ISO-8601 timestamp representation of entity creation date.
    """
    default_api_visibility: typing_extensions.Literal["private", "public"] = (
        pydantic.Field(
            alias="default_api_visibility",
        )
    )
    """
    The default visibility of APIs in the portal. If set to `public`, newly published APIs are visible to unauthenticated developers. If set to `private`, newly published APIs are hidden from unauthenticated developers.
    """
    default_application_auth_strategy_id: typing.Optional[str] = pydantic.Field(
        alias="default_application_auth_strategy_id",
    )
    """
    The default authentication strategy for APIs published to the portal. Newly published APIs will use this authentication strategy unless overridden during publication. If set to `null`, API publications will not use an authentication strategy unless set during publication. DCR support for Auth Strategies is currently in development.
    """
    default_domain: str = pydantic.Field(
        alias="default_domain",
    )
    """
    The domain assigned to the portal by Konnect. This is the default place to access the portal and its API if not using a `custom_domain``.
    """
    default_page_visibility: typing_extensions.Literal["private", "public"] = (
        pydantic.Field(
            alias="default_page_visibility",
        )
    )
    """
    The default visibility of pages in the portal. If set to `public`, newly created pages are visible to unauthenticated developers. If set to `private`, newly created pages are hidden from unauthenticated developers.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description",
    )
    """
    A description of the portal.
    """
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    """
    The display name of the portal. This value will be the portal's `name` in Portal API.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Contains a unique identifier used for this resource.
    """
    labels: typing.Optional[Labels] = pydantic.Field(alias="labels", default=None)
    """
    Labels store metadata of an entity that can be used for filtering an entity list or for searching across entity types. 
    
    Keys must be of length 1-63 characters, and cannot start with "kong", "konnect", "mesh", "kic", or "_".
    
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The name of the portal, used to distinguish it from other portals. Name must be unique.
    """
    rbac_enabled: bool = pydantic.Field(
        alias="rbac_enabled",
    )
    """
    Whether the portal resources are protected by Role Based Access Control (RBAC). If enabled, developers view or register for APIs until unless assigned to teams with access to view and consume specific APIs. Authentication must be enabled to use RBAC.
    """
    updated_at: str = pydantic.Field(
        alias="updated_at",
    )
    """
    An ISO-8601 timestamp representation of entity update date.
    """
