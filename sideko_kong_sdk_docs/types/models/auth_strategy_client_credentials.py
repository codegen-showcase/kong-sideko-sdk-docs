import pydantic
import typing
import typing_extensions


class AuthStrategyClientCredentials(pydantic.BaseModel):
    """
    Client Credential Auth strategy that the application uses.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    auth_methods: typing.List[str] = pydantic.Field(
        alias="auth_methods",
    )
    available_scopes: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="available_scopes", default=None
    )
    """
    Possible developer selectable scopes for an application. Only present when using DCR Provider that supports it.
    """
    credential_type: typing_extensions.Literal[
        "client_credentials", "self_managed_client_credentials"
    ] = pydantic.Field(
        alias="credential_type",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    The Application Auth Strategy ID.
    """
    name: str = pydantic.Field(
        alias="name",
    )
