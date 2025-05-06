import pydantic
import typing_extensions


class ListRolesResponseServicesRolesApiconsumer(pydantic.BaseModel):
    """
    ListRolesResponseServicesRolesApiconsumer
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing_extensions.Literal[
        "API Consumers can make calls to the given service"
    ] = pydantic.Field(
        alias="description",
    )
    name: typing_extensions.Literal["API Consumer"] = pydantic.Field(
        alias="name",
    )
