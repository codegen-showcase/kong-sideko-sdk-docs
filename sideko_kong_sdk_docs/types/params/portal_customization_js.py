import pydantic
import typing
import typing_extensions


class PortalCustomizationJs(typing_extensions.TypedDict, total=False):
    """
    PortalCustomizationJs
    """

    custom: typing_extensions.NotRequired[typing.Optional[str]]

    scripts: typing_extensions.NotRequired[typing.List[str]]


class _SerializerPortalCustomizationJs(pydantic.BaseModel):
    """
    Serializer for PortalCustomizationJs handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    custom: typing.Optional[str] = pydantic.Field(alias="custom", default=None)
    scripts: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="scripts", default=None
    )
