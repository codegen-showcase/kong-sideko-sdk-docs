import pydantic
import typing_extensions


class AddDeveloperToTeamRequest(typing_extensions.TypedDict):
    """
    Add a developer to a team by specifying the developer ID.
    """

    id: typing_extensions.Required[str]


class _SerializerAddDeveloperToTeamRequest(pydantic.BaseModel):
    """
    Serializer for AddDeveloperToTeamRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
