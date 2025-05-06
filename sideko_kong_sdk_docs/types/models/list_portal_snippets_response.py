import pydantic
import typing

from .paginated_meta import PaginatedMeta
from .portal_snippet_info import PortalSnippetInfo


class ListPortalSnippetsResponse(pydantic.BaseModel):
    """
    A paginated list of custom pages in a portal.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    data: typing.List[PortalSnippetInfo] = pydantic.Field(
        alias="data",
    )
    meta: PaginatedMeta = pydantic.Field(
        alias="meta",
    )
    """
    returns the pagination information
    """
