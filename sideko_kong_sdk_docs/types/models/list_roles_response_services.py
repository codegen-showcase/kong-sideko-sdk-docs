import pydantic
import typing_extensions

from .list_roles_response_services_roles import ListRolesResponseServicesRoles


class ListRolesResponseServices(pydantic.BaseModel):
    """
    ListRolesResponseServices
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing_extensions.Literal["Services"] = pydantic.Field(
        alias="name",
    )
    roles: ListRolesResponseServicesRoles = pydantic.Field(
        alias="roles",
    )
