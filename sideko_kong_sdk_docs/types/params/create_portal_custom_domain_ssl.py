import pydantic
import typing
import typing_extensions


class CreatePortalCustomDomainSsl(typing_extensions.TypedDict, total=False):
    """
    CreatePortalCustomDomainSsl
    """

    domain_verification_method: typing_extensions.Required[
        typing_extensions.Literal["http"]
    ]


class _SerializerCreatePortalCustomDomainSsl(pydantic.BaseModel):
    """
    Serializer for CreatePortalCustomDomainSsl handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    domain_verification_method: typing_extensions.Literal["http"] = pydantic.Field(
        alias="domain_verification_method",
    )
