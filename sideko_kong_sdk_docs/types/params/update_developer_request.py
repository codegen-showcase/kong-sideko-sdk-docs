import pydantic
import typing
import typing_extensions


class UpdateDeveloperRequest(typing_extensions.TypedDict, total=False):
    """
    UpdateDeveloperRequest
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["approved", "pending", "rejected", "revoked"]
    ]
    """
    The status of a developer in a portal. Approved developers can log in, create applications, and view and register for products they have access to. Pending, revoked, and rejected developers cannot login or view any non-public portal information, or create or modify applications or registrations.
    """


class _SerializerUpdateDeveloperRequest(pydantic.BaseModel):
    """
    Serializer for UpdateDeveloperRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    status: typing.Optional[
        typing_extensions.Literal["approved", "pending", "rejected", "revoked"]
    ] = pydantic.Field(alias="status", default=None)
