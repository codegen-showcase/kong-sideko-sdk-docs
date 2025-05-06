import pydantic
import typing
import typing_extensions


class PortalClaimMappings(typing_extensions.TypedDict):
    """
    Mappings from a portal developer atribute to an Identity Provider claim.
    """

    email: typing_extensions.NotRequired[str]

    groups: typing_extensions.NotRequired[str]

    name: typing_extensions.NotRequired[str]


class _SerializerPortalClaimMappings(pydantic.BaseModel):
    """
    Serializer for PortalClaimMappings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    groups: typing.Optional[str] = pydantic.Field(alias="groups", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
