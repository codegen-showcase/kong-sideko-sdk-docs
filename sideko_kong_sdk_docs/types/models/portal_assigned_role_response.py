import pydantic
import typing
import typing_extensions


class PortalAssignedRoleResponse(pydantic.BaseModel):
    """
    An assigned role associates a service and an action to a team.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    entity_id: typing.Optional[str] = pydantic.Field(alias="entity_id", default=None)
    entity_region: typing.Optional[
        typing_extensions.Literal["*", "au", "eu", "in", "me", "us"]
    ] = pydantic.Field(alias="entity_region", default=None)
    """
    Region of the entity.
    """
    entity_type_name: typing.Optional[str] = pydantic.Field(
        alias="entity_type_name", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    role_name: typing.Optional[str] = pydantic.Field(alias="role_name", default=None)
