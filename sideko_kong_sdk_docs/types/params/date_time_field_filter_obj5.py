import pydantic
import typing
import typing_extensions


class DateTimeFieldFilterObj5(typing_extensions.TypedDict, total=False):
    """
    DateTimeFieldFilterObj5
    """

    gte: typing_extensions.Required[str]
    """
    Value is greater than or equal to the given RFC-3339 formatted timestamp in UTC
    """


class _SerializerDateTimeFieldFilterObj5(pydantic.BaseModel):
    """
    Serializer for DateTimeFieldFilterObj5 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    gte: str = pydantic.Field(
        alias="gte",
    )
