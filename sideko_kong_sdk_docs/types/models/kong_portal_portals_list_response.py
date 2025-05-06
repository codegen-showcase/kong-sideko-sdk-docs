import pydantic
import typing

from .kong_portal_portals_list_response_data_item import (
    KongPortalPortalsListResponseDataItem,
)
from .paginated_meta import PaginatedMeta


class KongPortalPortalsListResponse(pydantic.BaseModel):
    """
    KongPortalPortalsListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    data: typing.List[KongPortalPortalsListResponseDataItem] = pydantic.Field(
        alias="data",
    )
    meta: PaginatedMeta = pydantic.Field(
        alias="meta",
    )
    """
    returns the pagination information
    """
