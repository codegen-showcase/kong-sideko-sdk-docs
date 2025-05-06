import pydantic
import typing
import typing_extensions


class StringFieldOeqFilter(typing_extensions.TypedDict, total=False):
    """
    Returns entities that exact match any of the comma-delimited phrases in the filter string.
    """

    oeq: typing_extensions.Required[str]


class _SerializerStringFieldOeqFilter(pydantic.BaseModel):
    """
    Serializer for StringFieldOeqFilter handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    oeq: str = pydantic.Field(
        alias="oeq",
    )
