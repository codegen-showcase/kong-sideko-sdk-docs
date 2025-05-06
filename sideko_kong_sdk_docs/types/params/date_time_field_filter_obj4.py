import pydantic
import typing
import typing_extensions


class DateTimeFieldFilterObj4(typing_extensions.TypedDict, total=False):
    """
    DateTimeFieldFilterObj4
    """

    gt: typing_extensions.Required[str]
    """
    Value is greater than the given RFC-3339 formatted timestamp in UTC
    """


class _SerializerDateTimeFieldFilterObj4(pydantic.BaseModel):
    """
    Serializer for DateTimeFieldFilterObj4 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    gt: str = pydantic.Field(
        alias="gt",
    )
