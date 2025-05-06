import pydantic
import typing


class PortalTeamResponse(pydantic.BaseModel):
    """
    Details about a developer team.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
