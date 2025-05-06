import pydantic
import typing


class SamlIdentityProviderConfig(pydantic.BaseModel):
    """
    The identity provider that contains configuration data for the SAML authentication integration.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    callback_url: typing.Optional[str] = pydantic.Field(
        alias="callback_url", default=None
    )
    """
    The path URL where the SAML identity provider sends authentication responses after successful login attempts.
    """
    idp_metadata_url: typing.Optional[str] = pydantic.Field(
        alias="idp_metadata_url", default=None
    )
    """
    The identity provider's metadata URL where the identity provider's metadata can be obtained.
    """
    idp_metadata_xml: typing.Optional[str] = pydantic.Field(
        alias="idp_metadata_xml", default=None
    )
    """
    The identity provider's SAML metadata. If the identity provider supports a metadata URL, you can use the `idp_metadata_url` field instead.
    
    """
    sp_entity_id: typing.Optional[str] = pydantic.Field(
        alias="sp_entity_id", default=None
    )
    """
    The entity ID of the service provider (SP).
    """
    sp_metadata_url: typing.Optional[str] = pydantic.Field(
        alias="sp_metadata_url", default=None
    )
