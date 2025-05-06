
### delete <a name="delete"></a>
Remove Role

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Removes an assigned role from a developer team. This deletes the association of the role with team and each of its members.

**API Endpoint**: `DELETE /portals/{portalId}/teams/{teamId}/assigned-roles/{roleId}`

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
res = client.kong_portal.portals.teams.assigned_roles.delete(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    role_id="8350205f-a305-4e39-abe9-bc082a80091a",
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
res = await client.kong_portal.portals.teams.assigned_roles.delete(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    role_id="8350205f-a305-4e39-abe9-bc082a80091a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
)
```

### list <a name="list"></a>
List Team Roles

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Lists the roles belonging to a developer team. Each role provides permissions to perform actions on a specified resource or collection.

**API Endpoint**: `GET /portals/{portalId}/teams/{teamId}/assigned-roles`

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
res = client.kong_portal.portals.teams.assigned_roles.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    page_number=1,
    page_size=10,
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
res = await client.kong_portal.portals.teams.assigned_roles.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    page_number=1,
    page_size=10,
)
```

### create <a name="create"></a>
Assign Role

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Assign a role to a developer team. This associates the set of permissions in a role with the team, so that they will be applied to any developer who is a member of the team.

**API Endpoint**: `POST /portals/{portalId}/teams/{teamId}/assigned-roles`

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
res = client.kong_portal.portals.teams.assigned_roles.create(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    entity_id="18ee2573-dec0-4b83-be99-fa7700bcdc61",
    entity_region="us",
    entity_type_name="Services",
    page_number=1,
    page_size=10,
    role_name="API Consumer",
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
res = await client.kong_portal.portals.teams.assigned_roles.create(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    entity_id="18ee2573-dec0-4b83-be99-fa7700bcdc61",
    entity_region="us",
    entity_type_name="Services",
    page_number=1,
    page_size=10,
    role_name="API Consumer",
)
```
