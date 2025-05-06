import pydantic
import typing

from .paginated_meta import PaginatedMeta
from .portal_assigned_role_response import PortalAssignedRoleResponse


class AssignedPortalRoleCollectionResponse(pydantic.BaseModel):
    """
    A paginated list of roles assigned to a team.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[PortalAssignedRoleResponse] = pydantic.Field(
        alias="data",
    )
    meta: PaginatedMeta = pydantic.Field(
        alias="meta",
    )
    """
    returns the pagination information
    """
