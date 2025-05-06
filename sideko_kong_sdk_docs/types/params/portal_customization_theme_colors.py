import pydantic
import typing
import typing_extensions


class PortalCustomizationThemeColors(typing_extensions.TypedDict, total=False):
    """
    PortalCustomizationThemeColors
    """

    primary: typing_extensions.NotRequired[str]


class _SerializerPortalCustomizationThemeColors(pydantic.BaseModel):
    """
    Serializer for PortalCustomizationThemeColors handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    primary: typing.Optional[str] = pydantic.Field(alias="primary", default=None)
