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


class KongPortalPortalsDevelopersListFilter(typing_extensions.TypedDict):
    """
    Filter developers returned in the response.
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

    status: typing_extensions.NotRequired[
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


class _SerializerKongPortalPortalsDevelopersListFilter(pydantic.BaseModel):
    """
    Serializer for KongPortalPortalsDevelopersListFilter handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="email", default=None)
    name: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="name", default=None)
    status: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="status", default=None)
