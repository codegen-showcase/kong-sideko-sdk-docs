import pydantic
import typing
import typing_extensions


class PortalTeamGroupMappingsUpdateRequestDataItem(typing_extensions.TypedDict):
    """
    PortalTeamGroupMappingsUpdateRequestDataItem
    """

    groups: typing_extensions.NotRequired[typing.List[str]]

    team_id: typing_extensions.NotRequired[str]


class _SerializerPortalTeamGroupMappingsUpdateRequestDataItem(pydantic.BaseModel):
    """
    Serializer for PortalTeamGroupMappingsUpdateRequestDataItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    groups: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="groups", default=None
    )
    team_id: typing.Optional[str] = pydantic.Field(alias="team_id", default=None)
