import pydantic

from .list_roles_response_services_roles_apiconsumer import (
    ListRolesResponseServicesRolesApiconsumer,
)
from .list_roles_response_services_roles_apiviewer import (
    ListRolesResponseServicesRolesApiviewer,
)


class ListRolesResponseServicesRoles(pydantic.BaseModel):
    """
    ListRolesResponseServicesRoles
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    apiconsumer: ListRolesResponseServicesRolesApiconsumer = pydantic.Field(
        alias="apiconsumer",
    )
    apiviewer: ListRolesResponseServicesRolesApiviewer = pydantic.Field(
        alias="apiviewer",
    )
