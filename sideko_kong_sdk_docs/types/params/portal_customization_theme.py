import pydantic
import typing
import typing_extensions

from .portal_customization_theme_colors import (
    PortalCustomizationThemeColors,
    _SerializerPortalCustomizationThemeColors,
)


class PortalCustomizationTheme(typing_extensions.TypedDict, total=False):
    """
    PortalCustomizationTheme
    """

    colors: typing_extensions.NotRequired[PortalCustomizationThemeColors]

    mode: typing_extensions.NotRequired[
        typing_extensions.Literal["dark", "light", "system"]
    ]

    name: typing_extensions.NotRequired[str]


class _SerializerPortalCustomizationTheme(pydantic.BaseModel):
    """
    Serializer for PortalCustomizationTheme handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    colors: typing.Optional[_SerializerPortalCustomizationThemeColors] = pydantic.Field(
        alias="colors", default=None
    )
    mode: typing.Optional[typing_extensions.Literal["dark", "light", "system"]] = (
        pydantic.Field(alias="mode", default=None)
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
