import pydantic
import typing
import typing_extensions


class InitSdkConfig(typing_extensions.TypedDict):
    """
    InitSdkConfig
    """

    api_name: typing_extensions.Required[str]
    """
    Unique project name or the uuid
    """

    api_version: typing_extensions.NotRequired[
        typing.Union[typing_extensions.Literal["latest"], str]
    ]
    """
    Can be either the semantic version or a released type (like latest)
    """

    customizations: typing_extensions.NotRequired[
        typing_extensions.Literal["config", "x-field"]
    ]


class _SerializerInitSdkConfig(pydantic.BaseModel):
    """
    Serializer for InitSdkConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    api_name: str = pydantic.Field(
        alias="api_name",
    )
    api_version: typing.Optional[
        typing.Union[typing_extensions.Literal["latest"], str]
    ] = pydantic.Field(alias="api_version", default=None)
    customizations: typing.Optional[typing_extensions.Literal["config", "x-field"]] = (
        pydantic.Field(alias="customizations", default=None)
    )
