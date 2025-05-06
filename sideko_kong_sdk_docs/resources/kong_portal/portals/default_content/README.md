
### create <a name="create"></a>
Creates Default Pages

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Creates the default pages for a portal if they do not already exists.

**API Endpoint**: `POST /portals/{portalId}/default-content`

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
res = client.kong_portal.portals.default_content.create(
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
res = await client.kong_portal.portals.default_content.create(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```
