import pydantic
import typing
import typing_extensions


class ReplacePortalImageAsset(typing_extensions.TypedDict, total=False):
    """
    The image data to upload, along with an optional filename. Images must be a data URL with binary image data in base 64 format. See https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs.
    """

    data: typing_extensions.Required[str]
    """
    must be a data URL with base64 image data, e.g., data:image/jpeg;base64,<BASE64_IMAGE_DATA>
    """

    filename: typing_extensions.NotRequired[str]


class _SerializerReplacePortalImageAsset(pydantic.BaseModel):
    """
    Serializer for ReplacePortalImageAsset handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    data: str = pydantic.Field(
        alias="data",
    )
    filename: typing.Optional[str] = pydantic.Field(alias="filename", default=None)
