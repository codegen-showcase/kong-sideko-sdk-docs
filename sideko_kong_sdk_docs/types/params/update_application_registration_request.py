import pydantic
import typing
import typing_extensions


class UpdateApplicationRegistrationRequest(typing_extensions.TypedDict, total=False):
    """
    UpdateApplicationRegistrationRequest
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["approved", "pending", "rejected", "revoked"]
    ]
    """
    The status of an application registration request. Each registration is linked to a single API, and application credentials will not grant access to the API until the registration is approved.
    Pending, revoked, and rejected registrations will not provide access to the API.
    """


class _SerializerUpdateApplicationRegistrationRequest(pydantic.BaseModel):
    """
    Serializer for UpdateApplicationRegistrationRequest handling case conversions
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
