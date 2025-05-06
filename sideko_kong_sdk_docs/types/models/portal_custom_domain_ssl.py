import pydantic
import typing
import typing_extensions


class PortalCustomDomainSsl(pydantic.BaseModel):
    """
    PortalCustomDomainSsl
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    domain_verification_method: typing_extensions.Literal["http"] = pydantic.Field(
        alias="domain_verification_method",
    )
    validation_errors: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="validation_errors", default=None
    )
    verification_status: typing_extensions.Literal["error", "pending", "verified"] = (
        pydantic.Field(
            alias="verification_status",
        )
    )
