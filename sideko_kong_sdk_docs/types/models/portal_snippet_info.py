import pydantic
import typing
import typing_extensions


class PortalSnippetInfo(pydantic.BaseModel):
    """
    Information about a snippet in a portal.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

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
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The unique name of a snippet in a portal.
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
    The display title of a snippet in a portal.
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
