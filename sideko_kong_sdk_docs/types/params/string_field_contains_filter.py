import pydantic
import typing
import typing_extensions


class StringFieldContainsFilter(typing_extensions.TypedDict, total=False):
    """
    Filters on the given string field value by fuzzy match.
    """

    contains: typing_extensions.Required[str]


class _SerializerStringFieldContainsFilter(pydantic.BaseModel):
    """
    Serializer for StringFieldContainsFilter handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    contains: str = pydantic.Field(
        alias="contains",
    )
