import pydantic
import typing
import typing_extensions


class PortalUpdateTeamRequest(typing_extensions.TypedDict):
    """
    Properties to update on a team.
    """

    description: typing_extensions.NotRequired[str]

    name: typing_extensions.NotRequired[str]


class _SerializerPortalUpdateTeamRequest(pydantic.BaseModel):
    """
    Serializer for PortalUpdateTeamRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
