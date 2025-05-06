import pydantic
import typing
import typing_extensions


class PortalCreateTeamRequest(typing_extensions.TypedDict):
    """
    Details about a team to create.
    """

    description: typing_extensions.NotRequired[str]

    name: typing_extensions.Required[str]


class _SerializerPortalCreateTeamRequest(pydantic.BaseModel):
    """
    Serializer for PortalCreateTeamRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
