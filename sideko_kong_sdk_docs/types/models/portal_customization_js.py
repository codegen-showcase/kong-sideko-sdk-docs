import pydantic
import typing


class PortalCustomizationJs(pydantic.BaseModel):
    """
    PortalCustomizationJs
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    custom: typing.Optional[str] = pydantic.Field(alias="custom", default=None)
    scripts: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="scripts", default=None
    )
