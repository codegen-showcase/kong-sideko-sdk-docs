
### list <a name="list"></a>
List Developer Teams

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Lists the teams to which a developer belongs. Each team a developer is a member of grants them various roles that provide permissions to perform actions on certain resources.

**API Endpoint**: `GET /portals/{portalId}/developers/{developerId}/teams`

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
res = client.kong_portal.portals.developers.teams.list(
    developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.kong_portal.portals.developers.teams.list(
    developer_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    page_number=1,
    page_size=10,
)
```
