import pydantic
import typing
import typing_extensions


class PortalAssignRoleRequest(typing_extensions.TypedDict):
    """
    An assigned role associates a service and an action to a team.
    """

    entity_id: typing_extensions.NotRequired[str]

    entity_region: typing_extensions.NotRequired[
        typing_extensions.Literal["*", "au", "eu", "in", "me", "us"]
    ]
    """
    Region of the entity.
    """

    entity_type_name: typing_extensions.NotRequired[str]

    role_name: typing_extensions.NotRequired[str]


class _SerializerPortalAssignRoleRequest(pydantic.BaseModel):
    """
    Serializer for PortalAssignRoleRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    entity_id: typing.Optional[str] = pydantic.Field(alias="entity_id", default=None)
    entity_region: typing.Optional[
        typing_extensions.Literal["*", "au", "eu", "in", "me", "us"]
    ] = pydantic.Field(alias="entity_region", default=None)
    entity_type_name: typing.Optional[str] = pydantic.Field(
        alias="entity_type_name", default=None
    )
    role_name: typing.Optional[str] = pydantic.Field(alias="role_name", default=None)
