
### delete <a name="delete"></a>
Delete Team

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Deletes a developer team from a portal. Deleting a team also deletes its assigned roles. Members of the team are not deleted, but they will lose any access provided through the team.

**API Endpoint**: `DELETE /portals/{portalId}/teams/{teamId}`

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
res = client.kong_portal.portals.teams.delete(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
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
res = await client.kong_portal.portals.teams.delete(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
)
```

### list <a name="list"></a>
List Teams

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Lists the developer teams in a portal. Each team can contain any developer and developers can be part of multiple teams.

**API Endpoint**: `GET /portals/{portalId}/teams`

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
res = client.kong_portal.portals.teams.list(
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
res = await client.kong_portal.portals.teams.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", page_number=1, page_size=10
)
```

### get <a name="get"></a>
Get Team

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Get an individual team.

**API Endpoint**: `GET /portals/{portalId}/teams/{teamId}`

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
res = client.kong_portal.portals.teams.get(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
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
res = await client.kong_portal.portals.teams.get(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
)
```

### patch <a name="patch"></a>
Update Team

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Updates an individual developer team for a portal.

**API Endpoint**: `PATCH /portals/{portalId}/teams/{teamId}`

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
res = client.kong_portal.portals.teams.patch(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    description="The Identity Management (IDM) API team.",
    name="IDM - Developers",
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
res = await client.kong_portal.portals.teams.patch(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    description="The Identity Management (IDM) API team.",
    name="IDM - Developers",
)
```

### create <a name="create"></a>
Create Team

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Creates a developer team in a portal. Developers can be added to teams to provide RBAC access to API products. Teams can be assigned roles that grant permissions to perform an action on a resource.

**API Endpoint**: `POST /portals/{portalId}/teams`

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
res = client.kong_portal.portals.teams.create(
    name="IDM - Developers",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    description="The Identity Management (IDM) API team.",
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
res = await client.kong_portal.portals.teams.create(
    name="IDM - Developers",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    description="The Identity Management (IDM) API team.",
)
```
