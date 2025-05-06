import pydantic
import typing


class BasicDeveloper(pydantic.BaseModel):
    """
    Basic information about a developer.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    full_name: typing.Optional[str] = pydantic.Field(alias="full_name", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
