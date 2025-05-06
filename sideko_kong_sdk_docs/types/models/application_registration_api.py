import pydantic
import typing


class ApplicationRegistrationApi(pydantic.BaseModel):
    """
    Details about the API the application is registered to.
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
    The name of the API the application is registered to.
    """
    version: typing.Optional[str] = pydantic.Field(
        alias="version",
    )
    """
    The version of the API the application is registered to.
    """
