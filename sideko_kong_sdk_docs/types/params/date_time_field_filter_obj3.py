import pydantic
import typing
import typing_extensions


class DateTimeFieldFilterObj3(typing_extensions.TypedDict, total=False):
    """
    DateTimeFieldFilterObj3
    """

    lte: typing_extensions.Required[str]
    """
    Value is less than or equal to the given RFC-3339 formatted timestamp in UTC
    """


class _SerializerDateTimeFieldFilterObj3(pydantic.BaseModel):
    """
    Serializer for DateTimeFieldFilterObj3 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    lte: str = pydantic.Field(
        alias="lte",
    )
