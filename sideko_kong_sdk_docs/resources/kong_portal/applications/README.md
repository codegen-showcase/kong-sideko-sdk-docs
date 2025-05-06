
### get <a name="get"></a>
Fetch Application

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Returns the configuration of a single application in any portal. If an application is linked to a DCR Provider, the `dcr_provider.id` and `client_id` can be used to correlate it. An application manages a set of credentials and registrations for specific APIs.

**API Endpoint**: `GET /applications/{applicationId}`

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
res = client.kong_portal.applications.get(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
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
res = await client.kong_portal.applications.get(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```
