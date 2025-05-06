import pydantic
import typing


class PortalCustomizationThemeColors(pydantic.BaseModel):
    """
    PortalCustomizationThemeColors
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    primary: typing.Optional[str] = pydantic.Field(alias="primary", default=None)
