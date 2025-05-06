import pydantic

from .list_roles_response_services import ListRolesResponseServices


class ListRolesResponse(pydantic.BaseModel):
    """
    The set of roles available to associate with resources and assign to teams.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    services: ListRolesResponseServices = pydantic.Field(
        alias="services",
    )
