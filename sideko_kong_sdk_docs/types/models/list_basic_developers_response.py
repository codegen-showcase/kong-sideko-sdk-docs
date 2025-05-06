import pydantic
import typing

from .basic_developer import BasicDeveloper
from .paginated_meta import PaginatedMeta


class ListBasicDevelopersResponse(pydantic.BaseModel):
    """
    A paginated list of basic information about a set of developers.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[BasicDeveloper]] = pydantic.Field(
        alias="data", default=None
    )
    meta: typing.Optional[PaginatedMeta] = pydantic.Field(alias="meta", default=None)
    """
    returns the pagination information
    """
