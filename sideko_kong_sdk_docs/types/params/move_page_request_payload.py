import pydantic
import typing
import typing_extensions


class MovePageRequestPayload(typing_extensions.TypedDict):
    """
    move page request payload
    """

    index: typing_extensions.NotRequired[int]
    """
    index of the document in the parent document's children
    """

    parent_page_id: typing_extensions.NotRequired[str]
    """
    parent page id
    """


class _SerializerMovePageRequestPayload(pydantic.BaseModel):
    """
    Serializer for MovePageRequestPayload handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    index: typing.Optional[int] = pydantic.Field(alias="index", default=None)
    parent_page_id: typing.Optional[str] = pydantic.Field(
        alias="parent_page_id", default=None
    )
