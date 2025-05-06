import pydantic
import typing

from .application_registration import ApplicationRegistration
from .paginated_meta import PaginatedMeta


class ListApplicationRegistrationsResponse(pydantic.BaseModel):
    """
    ListApplicationRegistrationsResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    data: typing.List[ApplicationRegistration] = pydantic.Field(
        alias="data",
    )
    meta: PaginatedMeta = pydantic.Field(
        alias="meta",
    )
    """
    returns the pagination information
    """
