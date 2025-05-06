import pydantic
import typing
import typing_extensions


class PortalPageInfo(pydantic.BaseModel):
    """
    Information about a page in a portal.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    children: typing.List["PortalPageInfo"] = pydantic.Field(
        alias="children",
    )
    """
    children of the page
    """
    created_at: str = pydantic.Field(
        alias="created_at",
    )
    """
    An ISO-8601 timestamp representation of entity creation date.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Contains a unique identifier used for this resource.
    """
    parent_page_id: typing.Optional[str] = pydantic.Field(
        alias="parent_page_id",
    )
    """
    Pages may be rendered as a tree of files.
    
    Specify the `id` of another page as the `parent_page_id` to add some hierarchy to your pages.
    
    """
    slug: str = pydantic.Field(
        alias="slug",
    )
    """
    The slug of a page in a portal. Is used to compute the full path /slug1/slug2/slug3.
    """
    status: typing_extensions.Literal["published", "unpublished"] = pydantic.Field(
        alias="status",
    )
    """
    Whether the resource is visible on a given portal. Defaults to false.
    """
    title: str = pydantic.Field(
        alias="title",
    )
    """
    The title of a page in a portal.
    """
    updated_at: str = pydantic.Field(
        alias="updated_at",
    )
    """
    An ISO-8601 timestamp representation of entity update date.
    """
    visibility: typing_extensions.Literal["private", "public"] = pydantic.Field(
        alias="visibility",
    )
    """
    Whether the resource is publicly accessible to non-authenticated users. Defaults to private.
    """
