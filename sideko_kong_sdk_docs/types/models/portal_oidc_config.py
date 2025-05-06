import pydantic
import typing

from .portal_claim_mappings import PortalClaimMappings


class PortalOidcConfig(pydantic.BaseModel):
    """
    Configuration properties for an OpenID Connect Identity Provider.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    claim_mappings: typing.Optional[PortalClaimMappings] = pydantic.Field(
        alias="claim_mappings", default=None
    )
    """
    Mappings from a portal developer atribute to an Identity Provider claim.
    """
    client_id: str = pydantic.Field(
        alias="client_id",
    )
    issuer: str = pydantic.Field(
        alias="issuer",
    )
    scopes: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="scopes", default=None
    )
