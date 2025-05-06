import pydantic
import typing
import typing_extensions


class UpdatePortalSnippetRequest(typing_extensions.TypedDict, total=False):
    """
    Update a snippet in a portal.
    """

    content: typing_extensions.NotRequired[str]
    """
    The renderable markdown content of a page in a portal.
    """

    description: typing_extensions.NotRequired[str]

    name: typing_extensions.NotRequired[str]
    """
    The unique name of a snippet in a portal.
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["published", "unpublished"]
    ]
    """
    Whether the resource is visible on a given portal. Defaults to false.
    """

    title: typing_extensions.NotRequired[str]
    """
    The display title of a snippet in a portal.
    """

    visibility: typing_extensions.NotRequired[
        typing_extensions.Literal["private", "public"]
    ]
    """
    Whether the resource is publicly accessible to non-authenticated users. Defaults to private.
    """


class _SerializerUpdatePortalSnippetRequest(pydantic.BaseModel):
    """
    Serializer for UpdatePortalSnippetRequest handling case conversions
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
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    status: typing.Optional[typing_extensions.Literal["published", "unpublished"]] = (
        pydantic.Field(alias="status", default=None)
    )
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    visibility: typing.Optional[typing_extensions.Literal["private", "public"]] = (
        pydantic.Field(alias="visibility", default=None)
    )
