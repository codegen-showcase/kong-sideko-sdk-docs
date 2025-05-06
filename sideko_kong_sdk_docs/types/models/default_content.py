import pydantic
import typing


class DefaultContent(pydantic.BaseModel):
    """
    Summary of created default content
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    pages: typing.List[str] = pydantic.Field(
        alias="pages",
    )
