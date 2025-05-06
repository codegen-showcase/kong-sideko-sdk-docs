import pydantic
import typing
import typing_extensions


class StringFieldOContainsFilter(typing_extensions.TypedDict, total=False):
    """
    Returns entities that fuzzy-match any of the comma-delimited phrases in the filter string.
    """

    ocontains: typing_extensions.Required[str]


class _SerializerStringFieldOContainsFilter(pydantic.BaseModel):
    """
    Serializer for StringFieldOContainsFilter handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    ocontains: str = pydantic.Field(
        alias="ocontains",
    )
