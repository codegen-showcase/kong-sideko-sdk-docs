import pydantic
import typing
import typing_extensions

from .application_registration_api import ApplicationRegistrationApi
from .application_registration_application import ApplicationRegistrationApplication


class ApplicationRegistration(pydantic.BaseModel):
    """
    A application's registration for a specific version of an API.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    api: ApplicationRegistrationApi = pydantic.Field(
        alias="api",
    )
    """
    Details about the API the application is registered to.
    """
    application: ApplicationRegistrationApplication = pydantic.Field(
        alias="application",
    )
    """
    Details about the application the registration is part of.
    """
    created_at: str = pydantic.Field(
        alias="created_at",
    )
    """
    An ISO-8601 timestamp representation of entity creation date.
    """
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
    The status of an application registration request. Each registration is linked to a single API, and application credentials will not grant access to the API until the registration is approved.
    Pending, revoked, and rejected registrations will not provide access to the API.
    """
    updated_at: str = pydantic.Field(
        alias="updated_at",
    )
    """
    An ISO-8601 timestamp representation of entity update date.
    """
