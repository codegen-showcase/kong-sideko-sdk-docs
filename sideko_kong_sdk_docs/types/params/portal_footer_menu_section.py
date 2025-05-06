import pydantic
import typing
import typing_extensions

from .portal_menu_item import PortalMenuItem, _SerializerPortalMenuItem


class PortalFooterMenuSection(typing_extensions.TypedDict, total=False):
    """
    PortalFooterMenuSection
    """

    items: typing_extensions.Required[typing.List[PortalMenuItem]]

    title: typing_extensions.Required[str]
    """
    The footer menu section title
    """


class _SerializerPortalFooterMenuSection(pydantic.BaseModel):
    """
    Serializer for PortalFooterMenuSection handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    items: typing.List[_SerializerPortalMenuItem] = pydantic.Field(
        alias="items",
    )
    title: str = pydantic.Field(
        alias="title",
    )
