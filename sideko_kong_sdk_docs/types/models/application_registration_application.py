import pydantic
import typing


class ApplicationRegistrationApplication(pydantic.BaseModel):
    """
    Details about the application the registration is part of.
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
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The name of the application the registration is part of.
    """
