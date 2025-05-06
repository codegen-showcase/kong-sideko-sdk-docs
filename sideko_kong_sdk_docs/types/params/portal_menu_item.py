import pydantic
import typing
import typing_extensions


class PortalMenuItem(typing_extensions.TypedDict, total=False):
    """
    PortalMenuItem
    """

    external: typing_extensions.Required[bool]
    """
    When clicked, open the link in a new window
    """

    path: typing_extensions.Required[str]
    """
    The absolute path of a page in a portal with a leading slash.
    """

    title: typing_extensions.Required[str]
    """
    The link display text
    """

    visibility: typing_extensions.Required[
        typing_extensions.Literal["private", "public"]
    ]
    """
    Whether a menu item is public or private. Private menu items are only accessible to authenticated users.
    """


class _SerializerPortalMenuItem(pydantic.BaseModel):
    """
    Serializer for PortalMenuItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    external: bool = pydantic.Field(
        alias="external",
    )
    path: str = pydantic.Field(
        alias="path",
    )
    title: str = pydantic.Field(
        alias="title",
    )
    visibility: typing_extensions.Literal["private", "public"] = pydantic.Field(
        alias="visibility",
    )
