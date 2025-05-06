import pydantic
import typing
import typing_extensions


class StringFieldEqualsFilterObj1(typing_extensions.TypedDict, total=False):
    """
    StringFieldEqualsFilterObj1
    """

    eq: typing_extensions.Required[str]


class _SerializerStringFieldEqualsFilterObj1(pydantic.BaseModel):
    """
    Serializer for StringFieldEqualsFilterObj1 handling case conversions
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
