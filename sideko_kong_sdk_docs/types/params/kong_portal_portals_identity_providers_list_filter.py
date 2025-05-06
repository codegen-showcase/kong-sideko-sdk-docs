import pydantic
import typing
import typing_extensions


class KongPortalPortalsIdentityProvidersListFilter(typing_extensions.TypedDict):
    """
    Filter identity providers returned in the response.
    """

    type_: typing_extensions.NotRequired[str]
    """
    Filter a string value by exact match.
    """


class _SerializerKongPortalPortalsIdentityProvidersListFilter(pydantic.BaseModel):
    """
    Serializer for KongPortalPortalsIdentityProvidersListFilter handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
