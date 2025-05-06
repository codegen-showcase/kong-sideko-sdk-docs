import pydantic
import typing
import typing_extensions

from .portal_team_group_mappings_update_request_data_item import (
    PortalTeamGroupMappingsUpdateRequestDataItem,
    _SerializerPortalTeamGroupMappingsUpdateRequestDataItem,
)


class PortalTeamGroupMappingsUpdateRequest(typing_extensions.TypedDict):
    """
    A set of mappings to update from a team to their groups.
    """

    data: typing_extensions.NotRequired[
        typing.List[PortalTeamGroupMappingsUpdateRequestDataItem]
    ]
    """
    The IdP groups to map to the given team.
    """


class _SerializerPortalTeamGroupMappingsUpdateRequest(pydantic.BaseModel):
    """
    Serializer for PortalTeamGroupMappingsUpdateRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[_SerializerPortalTeamGroupMappingsUpdateRequestDataItem]
    ] = pydantic.Field(alias="data", default=None)
