import pydantic
import typing
import typing_extensions


class LabelsUpdate(typing_extensions.TypedDict, total=False):
    """
    Labels store metadata of an entity that can be used for filtering an entity list or for searching across entity types.

    Labels are intended to store **INTERNAL** metadata.

    Keys must be of length 1-63 characters, and cannot start with "kong", "konnect", "mesh", "kic", or "_".

    """


class _SerializerLabelsUpdate(pydantic.BaseModel):
    """
    Serializer for LabelsUpdate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Optional[str]]
