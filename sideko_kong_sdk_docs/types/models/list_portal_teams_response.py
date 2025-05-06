import pydantic
import typing

from .paginated_meta import PaginatedMeta
from .portal_team_response import PortalTeamResponse


class ListPortalTeamsResponse(pydantic.BaseModel):
    """
    A paginated list of teams in a portal.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[PortalTeamResponse] = pydantic.Field(
        alias="data",
    )
    meta: PaginatedMeta = pydantic.Field(
        alias="meta",
    )
    """
    returns the pagination information
    """
