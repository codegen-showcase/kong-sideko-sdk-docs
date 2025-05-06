import pydantic
import typing
import typing_extensions

from .portal_custom_domain_ssl import PortalCustomDomainSsl


class PortalCustomDomain(pydantic.BaseModel):
    """
    PortalCustomDomain
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.Any]

    cname_status: typing_extensions.Literal["pending", "verified"] = pydantic.Field(
        alias="cname_status",
    )
    created_at: str = pydantic.Field(
        alias="created_at",
    )
    """
    An ISO-8601 timestamp representation of entity creation date.
    """
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    hostname: str = pydantic.Field(
        alias="hostname",
    )
    ssl: PortalCustomDomainSsl = pydantic.Field(
        alias="ssl",
    )
    updated_at: str = pydantic.Field(
        alias="updated_at",
    )
    """
    An ISO-8601 timestamp representation of entity update date.
    """
