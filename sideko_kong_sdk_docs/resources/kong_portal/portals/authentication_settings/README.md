
### list <a name="list"></a>
Get Auth Settings

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Returns the developer authentication configuration for a portal, which determines how developers can log in and how they are assigned to teams.

**API Endpoint**: `GET /portals/{portalId}/authentication-settings`

#### Synchronous Client

```python
from os import getenv
from sideko_kong_sdk_docs import Client

client = Client(
    sideko_key=getenv("API_KEY"),
    sideko_cookie=getenv("API_KEY"),
    kong_pat=getenv("API_TOKEN"),
    kong_sys_token=getenv("API_TOKEN"),
)
res = client.kong_portal.portals.authentication_settings.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_kong_sdk_docs import AsyncClient

client = AsyncClient(
    sideko_key=getenv("API_KEY"),
    sideko_cookie=getenv("API_KEY"),
    kong_pat=getenv("API_TOKEN"),
    kong_sys_token=getenv("API_TOKEN"),
)
res = await client.kong_portal.portals.authentication_settings.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

### patch <a name="patch"></a>
Update Auth Settings

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Updates the developer authentication configuration for a portal. Developers can be allowed to login using basic auth (email & password) or use Single-Sign-On (SSO) through an OIDC Identity Provider (IdP). Developers can be automatically assigned to teams by mapping claims from thier IdP account.

**API Endpoint**: `PATCH /portals/{portalId}/authentication-settings`

#### Synchronous Client

```python
from os import getenv
from sideko_kong_sdk_docs import Client

client = Client(
    sideko_key=getenv("API_KEY"),
    sideko_cookie=getenv("API_KEY"),
    kong_pat=getenv("API_TOKEN"),
    kong_sys_token=getenv("API_TOKEN"),
)
res = client.kong_portal.portals.authentication_settings.patch(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    basic_auth_enabled=False,
    idp_mapping_enabled=True,
    konnect_mapping_enabled=False,
    oidc_auth_enabled=False,
    oidc_team_mapping_enabled=True,
    saml_auth_enabled=False,
)
```

#### Asynchronous Client

```python
from os import getenv
from sideko_kong_sdk_docs import AsyncClient

client = AsyncClient(
    sideko_key=getenv("API_KEY"),
    sideko_cookie=getenv("API_KEY"),
    kong_pat=getenv("API_TOKEN"),
    kong_sys_token=getenv("API_TOKEN"),
)
res = await client.kong_portal.portals.authentication_settings.patch(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    basic_auth_enabled=False,
    idp_mapping_enabled=True,
    konnect_mapping_enabled=False,
    oidc_auth_enabled=False,
    oidc_team_mapping_enabled=True,
    saml_auth_enabled=False,
)
```
