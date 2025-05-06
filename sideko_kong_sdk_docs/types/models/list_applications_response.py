import pydantic
import typing

from .application_obj0 import ApplicationObj0
from .application_obj1 import ApplicationObj1
from .paginated_meta import PaginatedMeta


class ListApplicationsResponse(pydantic.BaseModel):
    """
    ListApplicationsResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    data: typing.List[typing.Union[ApplicationObj0, ApplicationObj1]] = pydantic.Field(
        alias="data",
    )
    meta: PaginatedMeta = pydantic.Field(
        alias="meta",
    )
    """
    returns the pagination information
    """
