
### delete <a name="delete"></a>
Delete Application by Portal

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Delete a single application in this portal, along with its registrations and credentials.

**API Endpoint**: `DELETE /portals/{portalId}/applications/{applicationId}`

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
res = client.kong_portal.portals.applications.delete(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.kong_portal.portals.applications.delete(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### list <a name="list"></a>
List Applications

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Lists applications in this portal. Each application can be registered for various APIs, issuing credentials for API access. If using DCR, an application will be linked to an Identity Provider's application by its `client_id`.

**API Endpoint**: `GET /portals/{portalId}/applications`

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
res = client.kong_portal.portals.applications.list(
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
res = await client.kong_portal.portals.applications.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", page_number=1, page_size=10
)
```

### get <a name="get"></a>
Fetch Application by Portal

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Returns the configuration of a single application in this portal. If an application is linked to a DCR Provider, the `dcr_provider.id` and `client_id` can be used to correlate it. An application manages a set of credentials and registrations for specific APIs.

**API Endpoint**: `GET /portals/{portalId}/applications/{applicationId}`

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
res = client.kong_portal.portals.applications.get(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.kong_portal.portals.applications.get(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```
