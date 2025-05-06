import pydantic
import typing
import typing_extensions


class CreatePortalSnippetRequest(typing_extensions.TypedDict, total=False):
    """
    Create a snippet in a portal.
    """

    content: typing_extensions.Required[str]
    """
    The renderable markdown content of a page in a portal.
    """

    description: typing_extensions.NotRequired[str]

    name: typing_extensions.Required[str]
    """
    The unique name of a snippet in a portal.
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["published", "unpublished"]
    ]
    """
    Whether the resource is visible on a given portal. Defaults to false.
    """

    title: typing_extensions.Required[str]
    """
    The display title of a snippet in a portal.
    """

    visibility: typing_extensions.NotRequired[str]
    """
    Whether a page is publicly accessible to non-authenticated users.
    """


class _SerializerCreatePortalSnippetRequest(pydantic.BaseModel):
    """
    Serializer for CreatePortalSnippetRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    content: str = pydantic.Field(
        alias="content",
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
    status: typing.Optional[typing_extensions.Literal["published", "unpublished"]] = (
        pydantic.Field(alias="status", default=None)
    )
    title: str = pydantic.Field(
        alias="title",
    )
    visibility: typing.Optional[str] = pydantic.Field(alias="visibility", default=None)
