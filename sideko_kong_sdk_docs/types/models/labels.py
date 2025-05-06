import pydantic
import typing


class Labels(pydantic.BaseModel):
    """
    Labels store metadata of an entity that can be used for filtering an entity list or for searching across entity types.

    Keys must be of length 1-63 characters, and cannot start with "kong", "konnect", "mesh", "kic", or "_".

    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, str]
