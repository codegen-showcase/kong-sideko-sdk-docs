import pydantic
import typing
import typing_extensions

from .oidc_identity_provider_claim_mappings import (
    OidcIdentityProviderClaimMappings,
    _SerializerOidcIdentityProviderClaimMappings,
)


class ConfigureOidcIdentityProviderConfig(typing_extensions.TypedDict, total=False):
    """
    The identity provider that contains configuration data for the OIDC authentication integration.
    """

    claim_mappings: typing_extensions.NotRequired[OidcIdentityProviderClaimMappings]
    """
    Defines the mappings between OpenID Connect (OIDC) claims and local claims used by your application for 
    authentication.
    
    """

    client_id: typing_extensions.Required[str]
    """
    The client ID assigned to your application by the identity provider.
    """

    client_secret: typing_extensions.NotRequired[str]
    """
    The Client Secret assigned to your application by the identity provider.
    """

    issuer_url: typing_extensions.Required[str]
    """
    The issuer URI of the identity provider. This is the URL where the provider's metadata can be obtained.
    """

    scopes: typing_extensions.NotRequired[typing.List[str]]
    """
    The scopes requested by your application when authenticating with the identity provider.
    """


class _SerializerConfigureOidcIdentityProviderConfig(pydantic.BaseModel):
    """
    Serializer for ConfigureOidcIdentityProviderConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    claim_mappings: typing.Optional[_SerializerOidcIdentityProviderClaimMappings] = (
        pydantic.Field(alias="claim_mappings", default=None)
    )
    client_id: str = pydantic.Field(
        alias="client_id",
    )
    client_secret: typing.Optional[str] = pydantic.Field(
        alias="client_secret", default=None
    )
    issuer_url: str = pydantic.Field(
        alias="issuer_url",
    )
    scopes: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="scopes", default=None
    )
