import pydantic
import typing

from .portal_menu_item import PortalMenuItem


class PortalFooterMenuSection(pydantic.BaseModel):
    """
    PortalFooterMenuSection
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    items: typing.List[PortalMenuItem] = pydantic.Field(
        alias="items",
    )
    title: str = pydantic.Field(
        alias="title",
    )
    """
    The footer menu section title
    """
