import pydantic
import typing


class OidcIdentityProviderClaimMappings(pydantic.BaseModel):
    """
    Defines the mappings between OpenID Connect (OIDC) claims and local claims used by your application for
    authentication.

    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    The claim mapping for the user's email address.
    """
    groups: typing.Optional[str] = pydantic.Field(alias="groups", default=None)
    """
    The claim mapping for the user's group membership information.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The claim mapping for the user's name.
    """
