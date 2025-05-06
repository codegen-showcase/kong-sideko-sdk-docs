import pydantic
import typing_extensions


class ListRolesResponseServicesRolesApiviewer(pydantic.BaseModel):
    """
    ListRolesResponseServicesRolesApiviewer
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing_extensions.Literal[
        "API Viewers have read-only access to the documentation of a service in a portal"
    ] = pydantic.Field(
        alias="description",
    )
    name: typing_extensions.Literal["API Viewer"] = pydantic.Field(
        alias="name",
    )
