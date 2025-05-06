import pydantic
import typing
import typing_extensions

from .date_time_field_filter_obj1 import (
    DateTimeFieldFilterObj1,
    _SerializerDateTimeFieldFilterObj1,
)
from .date_time_field_filter_obj2 import (
    DateTimeFieldFilterObj2,
    _SerializerDateTimeFieldFilterObj2,
)
from .date_time_field_filter_obj3 import (
    DateTimeFieldFilterObj3,
    _SerializerDateTimeFieldFilterObj3,
)
from .date_time_field_filter_obj4 import (
    DateTimeFieldFilterObj4,
    _SerializerDateTimeFieldFilterObj4,
)
from .date_time_field_filter_obj5 import (
    DateTimeFieldFilterObj5,
    _SerializerDateTimeFieldFilterObj5,
)
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


class PortalPagesFilterParameters(typing_extensions.TypedDict, total=False):
    """
    Filter pages returned in the response.
    """

    created_at: typing_extensions.NotRequired[
        typing.Union[
            str,
            DateTimeFieldFilterObj1,
            DateTimeFieldFilterObj2,
            DateTimeFieldFilterObj3,
            DateTimeFieldFilterObj4,
            DateTimeFieldFilterObj5,
        ]
    ]
    """
    Filters on the given datetime (RFC-3339) field value.
    """

    id: typing_extensions.NotRequired[
        typing.Union[
            typing.Union[str, StringFieldEqualsFilterObj1],
            StringFieldOeqFilter,
            StringFieldNeqFilter,
        ]
    ]
    """
    Filters on the given UUID field value by exact match.
    """

    slug: typing_extensions.NotRequired[
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

    title: typing_extensions.NotRequired[
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

    updated_at: typing_extensions.NotRequired[
        typing.Union[
            str,
            DateTimeFieldFilterObj1,
            DateTimeFieldFilterObj2,
            DateTimeFieldFilterObj3,
            DateTimeFieldFilterObj4,
            DateTimeFieldFilterObj5,
        ]
    ]
    """
    Filters on the given datetime (RFC-3339) field value.
    """

    visibility: typing_extensions.NotRequired[
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


class _SerializerPortalPagesFilterParameters(pydantic.BaseModel):
    """
    Serializer for PortalPagesFilterParameters handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    created_at: typing.Optional[
        typing.Union[
            str,
            _SerializerDateTimeFieldFilterObj1,
            _SerializerDateTimeFieldFilterObj2,
            _SerializerDateTimeFieldFilterObj3,
            _SerializerDateTimeFieldFilterObj4,
            _SerializerDateTimeFieldFilterObj5,
        ]
    ] = pydantic.Field(alias="created_at", default=None)
    id: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="id", default=None)
    slug: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="slug", default=None)
    title: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="title", default=None)
    updated_at: typing.Optional[
        typing.Union[
            str,
            _SerializerDateTimeFieldFilterObj1,
            _SerializerDateTimeFieldFilterObj2,
            _SerializerDateTimeFieldFilterObj3,
            _SerializerDateTimeFieldFilterObj4,
            _SerializerDateTimeFieldFilterObj5,
        ]
    ] = pydantic.Field(alias="updated_at", default=None)
    visibility: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="visibility", default=None)
