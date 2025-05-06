
### delete <a name="delete"></a>
Delete Registration

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Deletes an application registration, which if currently approved will immediately block API traffic to the API.
Note: Developers can request a new application registration for the given API as long as they have RBAC access to consume.

**API Endpoint**: `DELETE /portals/{portalId}/applications/{applicationId}/registrations/{registrationId}`

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
res = client.kong_portal.portals.applications.registrations.delete(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    registration_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.kong_portal.portals.applications.registrations.delete(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    registration_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### list <a name="list"></a>
List Registrations by Application

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Lists each API that this application is registered for and their current status (e.g., pending, approved, rejected, revoked).

**API Endpoint**: `GET /portals/{portalId}/applications/{applicationId}/registrations`

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
res = client.kong_portal.portals.applications.registrations.list(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.kong_portal.portals.applications.registrations.list(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    page_number=1,
    page_size=10,
)
```

### get <a name="get"></a>
Fetch Registration

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Returns information about an application's registration status for a particular API.

**API Endpoint**: `GET /portals/{portalId}/applications/{applicationId}/registrations/{registrationId}`

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
res = client.kong_portal.portals.applications.registrations.get(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    registration_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.kong_portal.portals.applications.registrations.get(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    registration_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### patch <a name="patch"></a>
Update Registration

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Updates the status of a particular application registration to an API. Approved application registrations will allow API traffic to the corresponding API. Revoked, rejected, or pending will not allow API traffic.

**API Endpoint**: `PATCH /portals/{portalId}/applications/{applicationId}/registrations/{registrationId}`

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
res = client.kong_portal.portals.applications.registrations.patch(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    registration_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.kong_portal.portals.applications.registrations.patch(
    application_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    registration_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    status="approved",
)
```
