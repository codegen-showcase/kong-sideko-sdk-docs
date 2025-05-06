import pydantic
import typing
import typing_extensions


class StringFieldNeqFilter(typing_extensions.TypedDict, total=False):
    """
    Filters on the given string field value by exact match inequality.
    """

    neq: typing_extensions.Required[str]


class _SerializerStringFieldNeqFilter(pydantic.BaseModel):
    """
    Serializer for StringFieldNeqFilter handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    neq: str = pydantic.Field(
        alias="neq",
    )
