import pydantic
import typing
import typing_extensions


class DateTimeFieldFilterObj2(typing_extensions.TypedDict, total=False):
    """
    DateTimeFieldFilterObj2
    """

    lt: typing_extensions.Required[str]
    """
    Value is less than the given RFC-3339 formatted timestamp in UTC
    """


class _SerializerDateTimeFieldFilterObj2(pydantic.BaseModel):
    """
    Serializer for DateTimeFieldFilterObj2 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    lt: str = pydantic.Field(
        alias="lt",
    )
