import pydantic
import typing
import typing_extensions


class UpdatePortalPageRequest(typing_extensions.TypedDict, total=False):
    """
    Update a page in a portal.
    """

    content: typing_extensions.NotRequired[str]
    """
    The renderable markdown content of a page in a portal.
    """

    description: typing_extensions.NotRequired[str]

    parent_page_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Pages may be rendered as a tree of files.
    
    Specify the `id` of another page as the `parent_page_id` to add some hierarchy to your pages.
    
    """

    slug: typing_extensions.NotRequired[str]
    """
    The slug of a page in a portal. Is used to compute the full path /slug1/slug2/slug3.
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["published", "unpublished"]
    ]
    """
    Whether the resource is visible on a given portal. Defaults to false.
    """

    title: typing_extensions.NotRequired[str]
    """
    The title of a page in a portal.
    """

    visibility: typing_extensions.NotRequired[
        typing_extensions.Literal["private", "public"]
    ]
    """
    Whether the resource is publicly accessible to non-authenticated users. Defaults to private.
    """


class _SerializerUpdatePortalPageRequest(pydantic.BaseModel):
    """
    Serializer for UpdatePortalPageRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    content: typing.Optional[str] = pydantic.Field(alias="content", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    parent_page_id: typing.Optional[str] = pydantic.Field(
        alias="parent_page_id", default=None
    )
    slug: typing.Optional[str] = pydantic.Field(alias="slug", default=None)
    status: typing.Optional[typing_extensions.Literal["published", "unpublished"]] = (
        pydantic.Field(alias="status", default=None)
    )
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    visibility: typing.Optional[typing_extensions.Literal["private", "public"]] = (
        pydantic.Field(alias="visibility", default=None)
    )
