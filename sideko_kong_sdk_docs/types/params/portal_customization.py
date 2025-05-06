import pydantic
import typing
import typing_extensions

from .portal_customization_js import (
    PortalCustomizationJs,
    _SerializerPortalCustomizationJs,
)
from .portal_customization_menu import (
    PortalCustomizationMenu,
    _SerializerPortalCustomizationMenu,
)
from .portal_customization_spec_renderer import (
    PortalCustomizationSpecRenderer,
    _SerializerPortalCustomizationSpecRenderer,
)
from .portal_customization_theme import (
    PortalCustomizationTheme,
    _SerializerPortalCustomizationTheme,
)


class PortalCustomization(typing_extensions.TypedDict, total=False):
    """
    The custom settings of this portal
    """

    css: typing_extensions.NotRequired[typing.Optional[str]]

    js: typing_extensions.NotRequired[PortalCustomizationJs]

    layout: typing_extensions.NotRequired[str]

    menu: typing_extensions.NotRequired[PortalCustomizationMenu]

    robots: typing_extensions.NotRequired[typing.Optional[str]]

    spec_renderer: typing_extensions.NotRequired[PortalCustomizationSpecRenderer]

    theme: typing_extensions.NotRequired[PortalCustomizationTheme]


class _SerializerPortalCustomization(pydantic.BaseModel):
    """
    Serializer for PortalCustomization handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    css: typing.Optional[str] = pydantic.Field(alias="css", default=None)
    js: typing.Optional[_SerializerPortalCustomizationJs] = pydantic.Field(
        alias="js", default=None
    )
    layout: typing.Optional[str] = pydantic.Field(alias="layout", default=None)
    menu: typing.Optional[_SerializerPortalCustomizationMenu] = pydantic.Field(
        alias="menu", default=None
    )
    robots: typing.Optional[str] = pydantic.Field(alias="robots", default=None)
    spec_renderer: typing.Optional[_SerializerPortalCustomizationSpecRenderer] = (
        pydantic.Field(alias="spec_renderer", default=None)
    )
    theme: typing.Optional[_SerializerPortalCustomizationTheme] = pydantic.Field(
        alias="theme", default=None
    )
