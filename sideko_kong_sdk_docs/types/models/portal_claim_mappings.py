import pydantic
import typing


class PortalClaimMappings(pydantic.BaseModel):
    """
    Mappings from a portal developer atribute to an Identity Provider claim.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    groups: typing.Optional[str] = pydantic.Field(alias="groups", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
