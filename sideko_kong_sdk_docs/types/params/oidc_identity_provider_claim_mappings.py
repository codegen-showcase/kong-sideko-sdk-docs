import pydantic
import typing
import typing_extensions


class OidcIdentityProviderClaimMappings(typing_extensions.TypedDict):
    """
    Defines the mappings between OpenID Connect (OIDC) claims and local claims used by your application for
    authentication.

    """

    email: typing_extensions.NotRequired[str]
    """
    The claim mapping for the user's email address.
    """

    groups: typing_extensions.NotRequired[str]
    """
    The claim mapping for the user's group membership information.
    """

    name: typing_extensions.NotRequired[str]
    """
    The claim mapping for the user's name.
    """


class _SerializerOidcIdentityProviderClaimMappings(pydantic.BaseModel):
    """
    Serializer for OidcIdentityProviderClaimMappings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    groups: typing.Optional[str] = pydantic.Field(alias="groups", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
