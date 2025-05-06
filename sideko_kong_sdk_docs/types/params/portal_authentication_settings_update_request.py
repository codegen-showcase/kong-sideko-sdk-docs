import pydantic
import typing
import typing_extensions

from .portal_claim_mappings import PortalClaimMappings, _SerializerPortalClaimMappings


class PortalAuthenticationSettingsUpdateRequest(typing_extensions.TypedDict):
    """
    Properties to update a portal's developer auth settings.
    """

    basic_auth_enabled: typing_extensions.NotRequired[bool]
    """
    The organization has basic auth enabled.
    """

    idp_mapping_enabled: typing_extensions.NotRequired[bool]
    """
    Whether IdP groups determine the Konnect Portal teams a developer has. This will soon replace oidc_team_mapping_enabled.
    """

    konnect_mapping_enabled: typing_extensions.NotRequired[bool]
    """
    Whether a Konnect Identity Admin assigns teams to a developer.
    """

    oidc_auth_enabled: typing_extensions.NotRequired[bool]
    """
    The organization has OIDC disabled.
    """

    oidc_claim_mappings: typing_extensions.NotRequired[PortalClaimMappings]
    """
    Mappings from a portal developer atribute to an Identity Provider claim.
    """

    oidc_client_id: typing_extensions.NotRequired[str]

    oidc_client_secret: typing_extensions.NotRequired[str]

    oidc_issuer: typing_extensions.NotRequired[str]

    oidc_scopes: typing_extensions.NotRequired[typing.List[str]]

    oidc_team_mapping_enabled: typing_extensions.NotRequired[bool]
    """
    Whether IdP groups determine the Konnect Portal teams a developer has.
    """

    saml_auth_enabled: typing_extensions.NotRequired[bool]
    """
    The portal has SAML enabled or disabled.
    """


class _SerializerPortalAuthenticationSettingsUpdateRequest(pydantic.BaseModel):
    """
    Serializer for PortalAuthenticationSettingsUpdateRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    basic_auth_enabled: typing.Optional[bool] = pydantic.Field(
        alias="basic_auth_enabled", default=None
    )
    idp_mapping_enabled: typing.Optional[bool] = pydantic.Field(
        alias="idp_mapping_enabled", default=None
    )
    konnect_mapping_enabled: typing.Optional[bool] = pydantic.Field(
        alias="konnect_mapping_enabled", default=None
    )
    oidc_auth_enabled: typing.Optional[bool] = pydantic.Field(
        alias="oidc_auth_enabled", default=None
    )
    oidc_claim_mappings: typing.Optional[_SerializerPortalClaimMappings] = (
        pydantic.Field(alias="oidc_claim_mappings", default=None)
    )
    oidc_client_id: typing.Optional[str] = pydantic.Field(
        alias="oidc_client_id", default=None
    )
    oidc_client_secret: typing.Optional[str] = pydantic.Field(
        alias="oidc_client_secret", default=None
    )
    oidc_issuer: typing.Optional[str] = pydantic.Field(
        alias="oidc_issuer", default=None
    )
    oidc_scopes: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="oidc_scopes", default=None
    )
    oidc_team_mapping_enabled: typing.Optional[bool] = pydantic.Field(
        alias="oidc_team_mapping_enabled", default=None
    )
    saml_auth_enabled: typing.Optional[bool] = pydantic.Field(
        alias="saml_auth_enabled", default=None
    )
