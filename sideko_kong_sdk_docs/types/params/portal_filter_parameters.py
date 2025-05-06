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


class PortalFilterParameters(typing_extensions.TypedDict):
    """
    Filter portals returned in the response.
    """

    authentication_enabled: typing_extensions.NotRequired[bool]
    """
    Filter by a boolean value (true/false).
    """

    auto_approve_applications: typing_extensions.NotRequired[bool]
    """
    Filter by a boolean value (true/false).
    """

    auto_approve_developers: typing_extensions.NotRequired[bool]
    """
    Filter by a boolean value (true/false).
    """

    canonical_domain: typing_extensions.NotRequired[
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

    default_api_visibility: typing_extensions.NotRequired[
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

    default_application_auth_strategy_id: typing_extensions.NotRequired[
        typing.Union[
            typing.Union[str, StringFieldEqualsFilterObj1],
            StringFieldOeqFilter,
            StringFieldNeqFilter,
        ]
    ]
    """
    Filters on the given UUID field value by exact match.
    """

    default_domain: typing_extensions.NotRequired[
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

    default_page_visibility: typing_extensions.NotRequired[
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

    description: typing_extensions.NotRequired[
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

    rbac_enabled: typing_extensions.NotRequired[bool]
    """
    Filter by a boolean value (true/false).
    """


class _SerializerPortalFilterParameters(pydantic.BaseModel):
    """
    Serializer for PortalFilterParameters handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    authentication_enabled: typing.Optional[bool] = pydantic.Field(
        alias="authentication_enabled", default=None
    )
    auto_approve_applications: typing.Optional[bool] = pydantic.Field(
        alias="auto_approve_applications", default=None
    )
    auto_approve_developers: typing.Optional[bool] = pydantic.Field(
        alias="auto_approve_developers", default=None
    )
    canonical_domain: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="canonical_domain", default=None)
    default_api_visibility: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="default_api_visibility", default=None)
    default_application_auth_strategy_id: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="default_application_auth_strategy_id", default=None)
    default_domain: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="default_domain", default=None)
    default_page_visibility: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="default_page_visibility", default=None)
    description: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="description", default=None)
    id: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="id", default=None)
    name: typing.Optional[
        typing.Union[
            typing.Union[str, _SerializerStringFieldEqualsFilterObj1],
            _SerializerStringFieldContainsFilter,
            _SerializerStringFieldOContainsFilter,
            _SerializerStringFieldOeqFilter,
            _SerializerStringFieldNeqFilter,
        ]
    ] = pydantic.Field(alias="name", default=None)
    rbac_enabled: typing.Optional[bool] = pydantic.Field(
        alias="rbac_enabled", default=None
    )
