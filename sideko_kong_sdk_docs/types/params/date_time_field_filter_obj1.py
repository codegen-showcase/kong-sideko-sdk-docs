import pydantic
import typing
import typing_extensions


class DateTimeFieldFilterObj1(typing_extensions.TypedDict, total=False):
    """
    DateTimeFieldFilterObj1
    """

    eq: typing_extensions.Required[str]
    """
    Value strictly equals given RFC-3339 formatted timestamp in UTC
    """


class _SerializerDateTimeFieldFilterObj1(pydantic.BaseModel):
    """
    Serializer for DateTimeFieldFilterObj1 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    eq: str = pydantic.Field(
        alias="eq",
    )
