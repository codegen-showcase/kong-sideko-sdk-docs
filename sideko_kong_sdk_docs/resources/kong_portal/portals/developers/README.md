
### delete <a name="delete"></a>
Delete Developer

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Deletes a developer, which will discontinue their ability to login, view any non-public resources, and delete all applications owned by them. All credentials issued to the developer will no longer provide access to any APIs. A deleted developer's unique email must be re-registered and approved to gain access again.

**API Endpoint**: `DELETE /portals/{portalId}/developers/{developerId}`

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
res = client.kong_portal.portals.developers.delete(
    developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.kong_portal.portals.developers.delete(
    developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### list <a name="list"></a>
List Developers

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Lists the developers that have registered for this portal. Each developer can be registered to one portal and must be approved to login unless using the developer auto-approve setting.

**API Endpoint**: `GET /portals/{portalId}/developers`

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
res = client.kong_portal.portals.developers.list(
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
res = await client.kong_portal.portals.developers.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", page_number=1, page_size=10
)
```

### get <a name="get"></a>
Fetch Developer

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Returns information about a single developer in this portal. Each developer manages a set applications, providing them credentials to access registered APIs. Developer registration access can be limited to specific APIs using RBAC.

**API Endpoint**: `GET /portals/{portalId}/developers/{developerId}`

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
res = client.kong_portal.portals.developers.get(
    developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.kong_portal.portals.developers.get(
    developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### patch <a name="patch"></a>
Update Developer

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Updates the status of a particular developer. Approved developers have access to login to the portal. Revoked, rejected, or pending are not allowed to login. Even if a developer's status is no longer approved, they will still be able to using any existing credentials generated while they were approved, until each application registration is revoked or deleted.

**API Endpoint**: `PATCH /portals/{portalId}/developers/{developerId}`

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
res = client.kong_portal.portals.developers.patch(
    developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    status="approved",
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
res = await client.kong_portal.portals.developers.patch(
    developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    status="approved",
)
```
