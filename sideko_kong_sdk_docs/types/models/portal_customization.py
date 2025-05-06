import pydantic
import typing

from .portal_customization_js import PortalCustomizationJs
from .portal_customization_menu import PortalCustomizationMenu
from .portal_customization_spec_renderer import PortalCustomizationSpecRenderer
from .portal_customization_theme import PortalCustomizationTheme


class PortalCustomization(pydantic.BaseModel):
    """
    The custom settings of this portal
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    css: typing.Optional[str] = pydantic.Field(alias="css", default=None)
    js: typing.Optional[PortalCustomizationJs] = pydantic.Field(
        alias="js", default=None
    )
    layout: typing.Optional[str] = pydantic.Field(alias="layout", default=None)
    menu: typing.Optional[PortalCustomizationMenu] = pydantic.Field(
        alias="menu", default=None
    )
    robots: typing.Optional[str] = pydantic.Field(alias="robots", default=None)
    spec_renderer: typing.Optional[PortalCustomizationSpecRenderer] = pydantic.Field(
        alias="spec_renderer", default=None
    )
    theme: typing.Optional[PortalCustomizationTheme] = pydantic.Field(
        alias="theme", default=None
    )
