import pydantic


class PageMeta(pydantic.BaseModel):
    """
    Contains pagination query parameters and the total number of objects returned.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    number: float = pydantic.Field(
        alias="number",
    )
    size: float = pydantic.Field(
        alias="size",
    )
    total: float = pydantic.Field(
        alias="total",
    )
