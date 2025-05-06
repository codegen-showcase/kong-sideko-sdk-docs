import pydantic
import typing
import typing_extensions

from .string_field_contains_filter import (
    StringFieldContainsFilter,
    _SerializerStringFieldContainsFilter,
)
from .string_field_equals_filter_obj1 import (
    StringFieldEqualsFilterObj1,
    _SerializerStringFieldEqualsFilterObj1,
)
from .string_field_neq_filter import (
    StringFieldNeqFilter,
    _SerializerStringFieldNeqFilter,
)
from .string_field_o_contains_filter import (
    StringFieldOContainsFilter,
    _SerializerStringFieldOContainsFilter,
)
from .string_field_oeq_filter import (
    StringFieldOeqFilter,
    _SerializerStringFieldOeqFilter,
)


class KongPortalPortalsTeamsListFilter(typing_extensions.TypedDict):
    """
    Filter teams returned in the response.
    """

    name: typing_extensions.NotRequired[
        typing.Union[
            typing.Union[str, StringFieldEqualsFilterObj1],
            StringFieldContainsFilter,
            StringFieldOContainsFilter,
            StringFieldOeqFilter,
            StringFieldNeqFilter,
        ]
    ]
    """
    Filters on the given string field value by either exact or fuzzy match.
    """


class _SerializerKongPortalPortalsTeamsListFilter(pydantic.BaseModel):
    """
    Serializer for KongPortalPortalsTeamsListFilter handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="name", default=None)
