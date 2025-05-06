
### list <a name="list"></a>
List Team Group Mappings

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Lists mappings between Konnect portal teams and Identity Provider (IdP) groups. Returns a 400 error if an IdP has not yet been configured.

**API Endpoint**: `GET /portals/{portalId}/identity-provider/team-group-mappings`

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
res = client.kong_portal.portals.identity_provider.team_group_mappings.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", page_number=1, page_size=10
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
res = await client.kong_portal.portals.identity_provider.team_group_mappings.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", page_number=1, page_size=10
)
```

### patch <a name="patch"></a>
Update Team Group Mappings

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Allows partial updates to the mappings between Konnect portal teams and Identity Provider (IdP) groups. The request body must be keyed on team ID. For a given team ID, the given group list is a complete replacement. To remove all mappings for a given team, provide an empty group list.
Returns a 400 error if an IdP has not yet been configured, or if a team ID in the request body is not found or is not a UUID.

**API Endpoint**: `PATCH /portals/{portalId}/identity-provider/team-group-mappings`

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
res = client.kong_portal.portals.identity_provider.team_group_mappings.patch(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    data=[
        {
            "groups": ["Service Developer"],
            "team_id": "af91db4c-6e51-403e-a2bf-33d27ae50c0a",
        },
        {
            "groups": ["Service Owner"],
            "team_id": "bc11db4c-6e51-403e-a2bf-33d27ae50c0a",
        },
    ],
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
res = await client.kong_portal.portals.identity_provider.team_group_mappings.patch(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    data=[
        {
            "groups": ["Service Developer"],
            "team_id": "af91db4c-6e51-403e-a2bf-33d27ae50c0a",
        },
        {
            "groups": ["Service Owner"],
            "team_id": "bc11db4c-6e51-403e-a2bf-33d27ae50c0a",
        },
    ],
)
```
