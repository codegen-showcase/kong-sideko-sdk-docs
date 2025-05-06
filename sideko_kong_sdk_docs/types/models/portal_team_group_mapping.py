import pydantic
import typing


class PortalTeamGroupMapping(pydantic.BaseModel):
    """
    A map of portal teams to Identity Provider groups.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    groups: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="groups", default=None
    )
    """
    The IdP groups that are mapped to the specified team.
    """
    team_id: typing.Optional[str] = pydantic.Field(alias="team_id", default=None)
    """
    The Konnect team ID.
    """
