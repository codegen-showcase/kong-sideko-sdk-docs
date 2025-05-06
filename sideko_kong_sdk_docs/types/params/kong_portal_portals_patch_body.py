import pydantic
import typing
import typing_extensions

from .labels_update import LabelsUpdate, _SerializerLabelsUpdate


class KongPortalPortalsPatchBody(typing_extensions.TypedDict, total=False):
    """
    KongPortalPortalsPatchBody
    """

    authentication_enabled: typing_extensions.NotRequired[bool]
    """
    Whether the portal supports developer authentication. If disabled, developers cannot register for accounts or create applications.
    """

    auto_approve_applications: typing_extensions.NotRequired[bool]
    """
    Whether requests from applications to register for APIs will be automatically approved, or if they will be set to pending until approved by an admin.
    """

    auto_approve_developers: typing_extensions.NotRequired[bool]
    """
    Whether developer account registrations will be automatically approved, or if they will be set to pending until approved by an admin.
    """

    canonical_domain: typing_extensions.NotRequired[str]
    """
    The canonical domain of the developer portal
    """

    created_at: typing_extensions.NotRequired[str]
    """
    An ISO-8601 timestamp representation of entity creation date.
    """

    default_api_visibility: typing_extensions.NotRequired[
        typing_extensions.Literal["private", "public"]
    ]
    """
    The default visibility of APIs in the portal. If set to `public`, newly published APIs are visible to unauthenticated developers. If set to `private`, newly published APIs are hidden from unauthenticated developers.
    """

    default_application_auth_strategy_id: typing_extensions.NotRequired[
        typing.Optional[str]
    ]
    """
    The default authentication strategy for APIs published to the portal. Newly published APIs will use this authentication strategy unless overridden during publication. If set to `null`, API publications will not use an authentication strategy unless set during publication. DCR support for Auth Strategies is currently in development.
    """

    default_domain: typing_extensions.NotRequired[str]
    """
    The domain assigned to the portal by Konnect. This is the default place to access the portal and its API if not using a `custom_domain``.
    """

    default_page_visibility: typing_extensions.NotRequired[
        typing_extensions.Literal["private", "public"]
    ]
    """
    The default visibility of pages in the portal. If set to `public`, newly created pages are visible to unauthenticated developers. If set to `private`, newly created pages are hidden from unauthenticated developers.
    """

    description: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A description of the portal.
    """

    display_name: typing_extensions.NotRequired[str]
    """
    The display name of the portal. This value will be the portal's `name` in Portal API.
    """

    id: typing_extensions.NotRequired[str]
    """
    Contains a unique identifier used for this resource.
    """

    labels: typing_extensions.NotRequired[typing.Optional[LabelsUpdate]]
    """
    Labels store metadata of an entity that can be used for filtering an entity list or for searching across entity types. 
    
    Labels are intended to store **INTERNAL** metadata.
    
    Keys must be of length 1-63 characters, and cannot start with "kong", "konnect", "mesh", "kic", or "_".
    
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of the portal, used to distinguish it from other portals. Name must be unique.
    """

    rbac_enabled: typing_extensions.NotRequired[bool]
    """
    Whether the portal resources are protected by Role Based Access Control (RBAC). If enabled, developers view or register for APIs until unless assigned to teams with access to view and consume specific APIs. Authentication must be enabled to use RBAC.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    An ISO-8601 timestamp representation of entity update date.
    """


class _SerializerKongPortalPortalsPatchBody(pydantic.BaseModel):
    """
    Serializer for KongPortalPortalsPatchBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    authentication_enabled: typing.Optional[bool] = pydantic.Field(
        alias="authentication_enabled", default=None
    )
    auto_approve_applications: typing.Optional[bool] = pydantic.Field(
        alias="auto_approve_applications", default=None
    )
    auto_approve_developers: typing.Optional[bool] = pydantic.Field(
        alias="auto_approve_developers", default=None
    )
    canonical_domain: typing.Optional[str] = pydantic.Field(
        alias="canonical_domain", default=None
    )
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    default_api_visibility: typing.Optional[
        typing_extensions.Literal["private", "public"]
    ] = pydantic.Field(alias="default_api_visibility", default=None)
    default_application_auth_strategy_id: typing.Optional[str] = pydantic.Field(
        alias="default_application_auth_strategy_id", default=None
    )
    default_domain: typing.Optional[str] = pydantic.Field(
        alias="default_domain", default=None
    )
    default_page_visibility: typing.Optional[
        typing_extensions.Literal["private", "public"]
    ] = pydantic.Field(alias="default_page_visibility", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    display_name: typing.Optional[str] = pydantic.Field(
        alias="display_name", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    labels: typing.Optional[_SerializerLabelsUpdate] = pydantic.Field(
        alias="labels", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    rbac_enabled: typing.Optional[bool] = pydantic.Field(
        alias="rbac_enabled", default=None
    )
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
