import pydantic
import typing
import typing_extensions

from .portal_footer_menu_section import (
    PortalFooterMenuSection,
    _SerializerPortalFooterMenuSection,
)
from .portal_menu_item import PortalMenuItem, _SerializerPortalMenuItem


class PortalCustomizationMenu(typing_extensions.TypedDict, total=False):
    """
    PortalCustomizationMenu
    """

    footer_bottom: typing_extensions.NotRequired[typing.List[PortalMenuItem]]

    footer_sections: typing_extensions.NotRequired[typing.List[PortalFooterMenuSection]]

    main: typing_extensions.NotRequired[typing.List[PortalMenuItem]]


class _SerializerPortalCustomizationMenu(pydantic.BaseModel):
    """
    Serializer for PortalCustomizationMenu handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    footer_bottom: typing.Optional[typing.List[_SerializerPortalMenuItem]] = (
        pydantic.Field(alias="footer_bottom", default=None)
    )
    footer_sections: typing.Optional[
        typing.List[_SerializerPortalFooterMenuSection]
    ] = pydantic.Field(alias="footer_sections", default=None)
    main: typing.Optional[typing.List[_SerializerPortalMenuItem]] = pydantic.Field(
        alias="main", default=None
    )
