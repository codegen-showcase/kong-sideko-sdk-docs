
### list <a name="list"></a>
List Portal Roles

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

List roles that can be assigned to teams in a portal. Each role provides a set of permissions to perform an action on a resource.

**API Endpoint**: `GET /portal-roles`

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
res = client.kong_portal.portal_roles.list()
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
res = await client.kong_portal.portal_roles.list()
```
