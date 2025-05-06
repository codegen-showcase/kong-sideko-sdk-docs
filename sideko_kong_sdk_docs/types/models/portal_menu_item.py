import pydantic
import typing
import typing_extensions


class PortalMenuItem(pydantic.BaseModel):
    """
    PortalMenuItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    external: bool = pydantic.Field(
        alias="external",
    )
    """
    When clicked, open the link in a new window
    """
    path: str = pydantic.Field(
        alias="path",
    )
    """
    The absolute path of a page in a portal with a leading slash.
    """
    title: str = pydantic.Field(
        alias="title",
    )
    """
    The link display text
    """
    visibility: typing_extensions.Literal["private", "public"] = pydantic.Field(
        alias="visibility",
    )
    """
    Whether a menu item is public or private. Private menu items are only accessible to authenticated users.
    """
