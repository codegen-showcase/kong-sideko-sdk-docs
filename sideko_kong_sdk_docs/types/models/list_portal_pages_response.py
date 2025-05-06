import pydantic
import typing
import typing_extensions

from .paginated_meta import PaginatedMeta

if typing_extensions.TYPE_CHECKING:
    from .portal_page_info import PortalPageInfo


class ListPortalPagesResponse(pydantic.BaseModel):
    """
    A paginated list of custom pages in a portal.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    data: typing.List["PortalPageInfo"] = pydantic.Field(
        alias="data",
    )
    meta: PaginatedMeta = pydantic.Field(
        alias="meta",
    )
    """
    returns the pagination information
    """
