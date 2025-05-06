import pydantic
import typing
import typing_extensions

from .configure_oidc_identity_provider_config import (
    ConfigureOidcIdentityProviderConfig,
    _SerializerConfigureOidcIdentityProviderConfig,
)
from .saml_identity_provider_config import (
    SamlIdentityProviderConfig,
    _SerializerSamlIdentityProviderConfig,
)


class UpdateIdentityProvider(typing_extensions.TypedDict):
    """
    The identity provider that contains configuration data for updating an authentication integration.
    """

    config: typing_extensions.NotRequired[
        typing.Union[ConfigureOidcIdentityProviderConfig, SamlIdentityProviderConfig]
    ]

    enabled: typing_extensions.NotRequired[bool]
    """
    Indicates whether the identity provider is enabled. 
    Only one identity provider can be active at a time, such as SAML or OIDC.
    
    """


class _SerializerUpdateIdentityProvider(pydantic.BaseModel):
    """
    Serializer for UpdateIdentityProvider handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    config: typing.Optional[
        typing.Union[
            _SerializerConfigureOidcIdentityProviderConfig,
            _SerializerSamlIdentityProviderConfig,
        ]
    ] = pydantic.Field(alias="config", default=None)
    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
