
### delete <a name="delete"></a>
Remove Developer from Team

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Removes a developer from a team. This removes the association of the team's roles from the developer.

**API Endpoint**: `DELETE /portals/{portalId}/teams/{teamId}/developers/{developerId}`

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
res = client.kong_portal.portals.teams.developers.delete(
    developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
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
res = await client.kong_portal.portals.teams.developers.delete(
    developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
)
```

### list <a name="list"></a>
List Team Developers

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

List a team's developers.

**API Endpoint**: `GET /portals/{portalId}/teams/{teamId}/developers`

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
res = client.kong_portal.portals.teams.developers.list(
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
res = await client.kong_portal.portals.teams.developers.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    page_number=1,
    page_size=10,
)
```

### create <a name="create"></a>
Add Developer to Team

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Adds a developer to a team. This associates them with all of the roles that have been assigned to the team, providing specific permissions to perform actions on resources.

**API Endpoint**: `POST /portals/{portalId}/teams/{teamId}/developers`

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
res = client.kong_portal.portals.teams.developers.create(
    id="df120cb4-f60b-47bc-a2f8-6a28e6a3c63b",
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
res = await client.kong_portal.portals.teams.developers.create(
    id="df120cb4-f60b-47bc-a2f8-6a28e6a3c63b",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    team_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
)
```
