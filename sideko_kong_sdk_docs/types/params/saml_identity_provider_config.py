import pydantic
import typing
import typing_extensions


class SamlIdentityProviderConfig(typing_extensions.TypedDict, total=False):
    """
    The identity provider that contains configuration data for the SAML authentication integration.
    """

    callback_url: typing_extensions.NotRequired[str]
    """
    The path URL where the SAML identity provider sends authentication responses after successful login attempts.
    """

    idp_metadata_url: typing_extensions.NotRequired[str]
    """
    The identity provider's metadata URL where the identity provider's metadata can be obtained.
    """

    idp_metadata_xml: typing_extensions.NotRequired[str]
    """
    The identity provider's SAML metadata. If the identity provider supports a metadata URL, you can use the `idp_metadata_url` field instead.
    
    """

    sp_entity_id: typing_extensions.NotRequired[str]
    """
    The entity ID of the service provider (SP).
    """

    sp_metadata_url: typing_extensions.NotRequired[str]


class _SerializerSamlIdentityProviderConfig(pydantic.BaseModel):
    """
    Serializer for SamlIdentityProviderConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    callback_url: typing.Optional[str] = pydantic.Field(
        alias="callback_url", default=None
    )
    idp_metadata_url: typing.Optional[str] = pydantic.Field(
        alias="idp_metadata_url", default=None
    )
    idp_metadata_xml: typing.Optional[str] = pydantic.Field(
        alias="idp_metadata_xml", default=None
    )
    sp_entity_id: typing.Optional[str] = pydantic.Field(
        alias="sp_entity_id", default=None
    )
    sp_metadata_url: typing.Optional[str] = pydantic.Field(
        alias="sp_metadata_url", default=None
    )
