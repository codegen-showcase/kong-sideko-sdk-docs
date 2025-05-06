import pydantic

from .page_meta import PageMeta


class PaginatedMeta(pydantic.BaseModel):
    """
    returns the pagination information
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    page: PageMeta = pydantic.Field(
        alias="page",
    )
    """
    Contains pagination query parameters and the total number of objects returned.
    """
