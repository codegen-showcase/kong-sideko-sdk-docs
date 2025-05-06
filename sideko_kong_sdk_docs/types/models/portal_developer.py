import pydantic
import typing
import typing_extensions


class PortalDeveloper(pydantic.BaseModel):
    """
    PortalDeveloper
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    application_count: float = pydantic.Field(
        alias="application_count",
    )
    created_at: str = pydantic.Field(
        alias="created_at",
    )
    """
    An ISO-8601 timestamp representation of entity creation date.
    """
    email: str = pydantic.Field(
        alias="email",
    )
    full_name: str = pydantic.Field(
        alias="full_name",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Contains a unique identifier used for this resource.
    """
    status: typing_extensions.Literal["approved", "pending", "rejected", "revoked"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    The status of a developer in a portal. Approved developers can log in, create applications, and view and register for products they have access to. Pending, revoked, and rejected developers cannot login or view any non-public portal information, or create or modify applications or registrations.
    """
    updated_at: str = pydantic.Field(
        alias="updated_at",
    )
    """
    An ISO-8601 timestamp representation of entity update date.
    """
