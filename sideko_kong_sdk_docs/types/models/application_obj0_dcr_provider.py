import pydantic
import typing


class ApplicationObj0DcrProvider(pydantic.BaseModel):
    """
    Information about the DCR provider this application uses, if using DCR.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    id: str = pydantic.Field(
        alias="id",
    )
    """
    Contains a unique identifier used for this resource.
    """
