import pydantic
import typing
import typing_extensions


class AuthStrategyKeyAuth(pydantic.BaseModel):
    """
    KeyAuth Auth strategy that the application uses.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    credential_type: typing_extensions.Literal["key_auth"] = pydantic.Field(
        alias="credential_type",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    The Application Auth Strategy ID.
    """
    key_names: typing.List[str] = pydantic.Field(
        alias="key_names",
    )
    name: str = pydantic.Field(
        alias="name",
    )
