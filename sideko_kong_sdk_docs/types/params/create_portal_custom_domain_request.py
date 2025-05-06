import pydantic
import typing
import typing_extensions

from .create_portal_custom_domain_ssl import (
    CreatePortalCustomDomainSsl,
    _SerializerCreatePortalCustomDomainSsl,
)


class CreatePortalCustomDomainRequest(typing_extensions.TypedDict, total=False):
    """
    CreatePortalCustomDomainRequest
    """

    enabled: typing_extensions.Required[bool]

    hostname: typing_extensions.Required[str]

    ssl: typing_extensions.Required[CreatePortalCustomDomainSsl]


class _SerializerCreatePortalCustomDomainRequest(pydantic.BaseModel):
    """
    Serializer for CreatePortalCustomDomainRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    hostname: str = pydantic.Field(
        alias="hostname",
    )
    ssl: _SerializerCreatePortalCustomDomainSsl = pydantic.Field(
        alias="ssl",
    )
