import pydantic
import typing

from .portal_oidc_config import PortalOidcConfig


class PortalAuthenticationSettingsResponse(pydantic.BaseModel):
    """
    The developer authentication settings for a portal.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    basic_auth_enabled: bool = pydantic.Field(
        alias="basic_auth_enabled",
    )
    """
    The portal has basic auth enabled or disabled.
    """
    idp_mapping_enabled: typing.Optional[bool] = pydantic.Field(
        alias="idp_mapping_enabled", default=None
    )
    """
    IdP groups determine the Portal Teams a developer has. This will soon replace oidc_team_mapping_enabled.
    """
    konnect_mapping_enabled: bool = pydantic.Field(
        alias="konnect_mapping_enabled",
    )
    """
    A Konnect Identity Admin assigns teams to a developer.
    """
    oidc_auth_enabled: bool = pydantic.Field(
        alias="oidc_auth_enabled",
    )
    """
    The portal has OIDC enabled or disabled.
    """
    oidc_config: typing.Optional[PortalOidcConfig] = pydantic.Field(
        alias="oidc_config", default=None
    )
    """
    Configuration properties for an OpenID Connect Identity Provider.
    """
    oidc_team_mapping_enabled: bool = pydantic.Field(
        alias="oidc_team_mapping_enabled",
    )
    """
    IdP groups determine the Portal Teams a developer has.
    """
    saml_auth_enabled: typing.Optional[bool] = pydantic.Field(
        alias="saml_auth_enabled", default=None
    )
    """
    The portal has SAML enabled or disabled.
    """
