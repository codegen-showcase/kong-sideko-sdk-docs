import pydantic
import typing

from .portal_footer_menu_section import PortalFooterMenuSection
from .portal_menu_item import PortalMenuItem


class PortalCustomizationMenu(pydantic.BaseModel):
    """
    PortalCustomizationMenu
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    footer_bottom: typing.Optional[typing.List[PortalMenuItem]] = pydantic.Field(
        alias="footer_bottom", default=None
    )
    footer_sections: typing.Optional[typing.List[PortalFooterMenuSection]] = (
        pydantic.Field(alias="footer_sections", default=None)
    )
    main: typing.Optional[typing.List[PortalMenuItem]] = pydantic.Field(
        alias="main", default=None
    )
