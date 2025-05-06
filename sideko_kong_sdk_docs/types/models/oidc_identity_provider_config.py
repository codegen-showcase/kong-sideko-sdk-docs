import pydantic
import typing

from .oidc_identity_provider_claim_mappings import OidcIdentityProviderClaimMappings


class OidcIdentityProviderConfig(pydantic.BaseModel):
    """
    The identity provider that contains configuration data for the OIDC authentication integration.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    claim_mappings: typing.Optional[OidcIdentityProviderClaimMappings] = pydantic.Field(
        alias="claim_mappings", default=None
    )
    """
    Defines the mappings between OpenID Connect (OIDC) claims and local claims used by your application for 
    authentication.
    
    """
    client_id: str = pydantic.Field(
        alias="client_id",
    )
    """
    The client ID assigned to your application by the identity provider.
    """
    issuer_url: str = pydantic.Field(
        alias="issuer_url",
    )
    """
    The issuer URI of the identity provider. This is the URL where the provider's metadata can be obtained.
    """
    scopes: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="scopes", default=None
    )
    """
    The scopes requested by your application when authenticating with the identity provider.
    """
