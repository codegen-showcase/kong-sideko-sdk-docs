import pydantic
import typing
import typing_extensions


class UpdatePortalCustomDomainRequest(typing_extensions.TypedDict, total=False):
    """
    UpdatePortalCustomDomainRequest
    """

    enabled: typing_extensions.NotRequired[bool]


class _SerializerUpdatePortalCustomDomainRequest(pydantic.BaseModel):
    """
    Serializer for UpdatePortalCustomDomainRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
