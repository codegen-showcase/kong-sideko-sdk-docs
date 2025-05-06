import pydantic
import typing
import typing_extensions


class PortalCustomizationSpecRenderer(typing_extensions.TypedDict, total=False):
    """
    PortalCustomizationSpecRenderer
    """

    infinite_scroll: typing_extensions.NotRequired[bool]

    show_schemas: typing_extensions.NotRequired[bool]

    try_it_insomnia: typing_extensions.NotRequired[bool]

    try_it_ui: typing_extensions.NotRequired[bool]


class _SerializerPortalCustomizationSpecRenderer(pydantic.BaseModel):
    """
    Serializer for PortalCustomizationSpecRenderer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    infinite_scroll: typing.Optional[bool] = pydantic.Field(
        alias="infinite_scroll", default=None
    )
    show_schemas: typing.Optional[bool] = pydantic.Field(
        alias="show_schemas", default=None
    )
    try_it_insomnia: typing.Optional[bool] = pydantic.Field(
        alias="try_it_insomnia", default=None
    )
    try_it_ui: typing.Optional[bool] = pydantic.Field(alias="try_it_ui", default=None)
