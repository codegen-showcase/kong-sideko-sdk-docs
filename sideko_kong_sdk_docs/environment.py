import enum
import typing
import typing_extensions


class Environment(enum.Enum):
    """Pre-defined base URLs for the API"""

    SIDEKO_PROD = "https://api.sideko.dev/v1"
    KONG_US = "https://us.api.konghq.com/v3"
    KONG_EU = "https://eu.api.konghq.com/v3"
    KONG_AU = "https://au.api.konghq.com/v3"
    KONG_ME = "https://me.api.konghq.com/v3"
    KONG_IN = "https://in.api.konghq.com/v3"
    SIDEKO_API_MOCK_SERVER = "https://api.sideko.dev/v1/mock/public/sideko-api/0.2.12"
    KONG_PORTAL_MGMT_MOCK_SERVER = (
        "https://api.sideko.dev/v1/mock/public/kong-portal-mgmt/0.1.0"
    )


class ServerGroup(typing_extensions.TypedDict):
    """Pre-defined set of base URLs for the APIs serviced by this SDK"""

    sideko: typing_extensions.NotRequired[typing.Union[Environment, str]]
    kong_portal: typing_extensions.NotRequired[typing.Union[Environment, str]]


DEFAULT: ServerGroup = {
    "sideko": Environment.SIDEKO_PROD.value,
    "kong_portal": Environment.KONG_US.value,
}

SIDEKO_MOCK_SERVER: ServerGroup = {
    "sideko": Environment.SIDEKO_API_MOCK_SERVER.value,
    "kong_portal": Environment.KONG_PORTAL_MGMT_MOCK_SERVER.value,
}


def _get_base_url(
    server_group: ServerGroup,
    api: typing.Literal["sideko", "kong_portal"],
    default: typing.Union[Environment, str],
) -> str:
    env_or_str = server_group.get(api, default)
    if isinstance(env_or_str, Environment):
        return env_or_str.value
    else:
        return str(env_or_str)
