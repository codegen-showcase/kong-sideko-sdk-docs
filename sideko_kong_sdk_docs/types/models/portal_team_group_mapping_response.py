import pydantic
import typing

from .paginated_meta import PaginatedMeta
from .portal_team_group_mapping import PortalTeamGroupMapping


class PortalTeamGroupMappingResponse(pydantic.BaseModel):
    """
    A paginated list of portal team group mappings.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[PortalTeamGroupMapping]] = pydantic.Field(
        alias="data", default=None
    )
    meta: typing.Optional[PaginatedMeta] = pydantic.Field(alias="meta", default=None)
    """
    returns the pagination information
    """
