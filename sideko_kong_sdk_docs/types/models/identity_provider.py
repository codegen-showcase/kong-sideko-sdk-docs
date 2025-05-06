import pydantic
import typing
import typing_extensions

from .oidc_identity_provider_config import OidcIdentityProviderConfig
from .saml_identity_provider_config import SamlIdentityProviderConfig


class IdentityProvider(pydantic.BaseModel):
    """
    The identity provider that contains configuration data for authentication integration.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    config: typing.Optional[
        typing.Union[OidcIdentityProviderConfig, SamlIdentityProviderConfig]
    ] = pydantic.Field(alias="config", default=None)
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    An ISO-8601 timestamp representation of entity creation date.
    """
    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    """
    Indicates whether the identity provider is enabled. 
    Only one identity provider can be active at a time, such as SAML or OIDC.
    
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Contains a unique identifier used for this resource.
    """
    type_: typing.Optional[typing_extensions.Literal["oidc", "saml"]] = pydantic.Field(
        alias="type", default=None
    )
    """
    Specifies the type of identity provider.
    """
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    """
    An ISO-8601 timestamp representation of entity update date.
    """
