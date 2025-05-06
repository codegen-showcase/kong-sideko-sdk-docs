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


class KongPortalPortalsTeamsDevelopersListFilter(typing_extensions.TypedDict):
    """
    Filter developers returned in the response.
    """

    active: typing_extensions.NotRequired[bool]
    """
    Filter by a boolean value (true/false).
    """

    attributes: typing_extensions.NotRequired[
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

    email: typing_extensions.NotRequired[
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

    full_name: typing_extensions.NotRequired[
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


class _SerializerKongPortalPortalsTeamsDevelopersListFilter(pydantic.BaseModel):
    """
    Serializer for KongPortalPortalsTeamsDevelopersListFilter handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    attributes: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="attributes", default=None)
    email: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="email", default=None)
    full_name: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="full_name", default=None)
