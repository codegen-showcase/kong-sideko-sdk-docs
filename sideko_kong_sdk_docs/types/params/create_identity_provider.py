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


class CreateIdentityProvider(typing_extensions.TypedDict):
    """
    The identity provider that contains configuration data for creating an authentication integration.
    """

    config: typing_extensions.NotRequired[
        typing.Union[ConfigureOidcIdentityProviderConfig, SamlIdentityProviderConfig]
    ]

    type_: typing_extensions.NotRequired[typing_extensions.Literal["oidc", "saml"]]
    """
    Specifies the type of identity provider.
    """


class _SerializerCreateIdentityProvider(pydantic.BaseModel):
    """
    Serializer for CreateIdentityProvider handling case conversions
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
    type_: typing.Optional[typing_extensions.Literal["oidc", "saml"]] = pydantic.Field(
        alias="type", default=None
    )
