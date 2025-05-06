
### list <a name="list"></a>
Get Logo

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Returns the logo of the portal.

**API Endpoint**: `GET /portals/{portalId}/assets/logo`

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
res = client.kong_portal.portals.assets.logo.list(
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
res = await client.kong_portal.portals.assets.logo.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

### update <a name="update"></a>
Replace Logo

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Replaces the logo of the portal.

**API Endpoint**: `PUT /portals/{portalId}/assets/logo`

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
res = client.kong_portal.portals.assets.logo.update(
    data="data:image/png;base64,bmljZV9sb29raW5nX3BpY3R1cmU=",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    filename="logo.png",
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
res = await client.kong_portal.portals.assets.logo.update(
    data="data:image/png;base64,bmljZV9sb29raW5nX3BpY3R1cmU=",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    filename="logo.png",
)
```
