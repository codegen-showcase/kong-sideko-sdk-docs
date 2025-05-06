import pydantic
import typing
import typing_extensions

from .portal_customization_theme_colors import PortalCustomizationThemeColors


class PortalCustomizationTheme(pydantic.BaseModel):
    """
    PortalCustomizationTheme
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    colors: typing.Optional[PortalCustomizationThemeColors] = pydantic.Field(
        alias="colors", default=None
    )
    mode: typing.Optional[typing_extensions.Literal["dark", "light", "system"]] = (
        pydantic.Field(alias="mode", default=None)
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
