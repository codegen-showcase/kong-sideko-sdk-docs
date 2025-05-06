import pydantic
import typing


class PortalCustomizationSpecRenderer(pydantic.BaseModel):
    """
    PortalCustomizationSpecRenderer
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
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
