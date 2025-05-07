import pydantic
import typing
import typing_extensions


class ApisSpecificationsGetResponse(pydantic.BaseModel):
    """
    ApisSpecificationsGetResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    content: str = pydantic.Field(
        alias="content",
    )
    """
    The raw content of your API specification.
    
    """
    created_at: str = pydantic.Field(
        alias="created_at",
    )
    """
    An ISO-8601 timestamp representation of entity creation date.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    The API specification identifier.
    """
    type_: typing_extensions.Literal["asyncapi", "oas3"] = pydantic.Field(
        alias="type",
    )
    """
    The type of specification being stored. This allows us to render the specification correctly.
    
    If this field is not set, it will be autodetected from `content`
    
    """
    updated_at: str = pydantic.Field(
        alias="updated_at",
    )
    """
    An ISO-8601 timestamp representation of entity update date.
    """
