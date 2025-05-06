
### delete <a name="delete"></a>
Delete Page

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Deletes a single custom page for this portal.

**API Endpoint**: `DELETE /portals/{portalId}/pages/{pageId}`

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
res = client.kong_portal.portals.pages.delete(
    page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
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
res = await client.kong_portal.portals.pages.delete(
    page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### list <a name="list"></a>
List Pages

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Returns the paginated list of custom pages that have been created for this portal.

**API Endpoint**: `GET /portals/{portalId}/pages`

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
res = client.kong_portal.portals.pages.list(
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
res = await client.kong_portal.portals.pages.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", page_number=1, page_size=10
)
```

### get <a name="get"></a>
Fetch Page

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Returns the configuration of a single custom page for this portal. Custom pages can be used to display static content, documentation, or other information to developers.

**API Endpoint**: `GET /portals/{portalId}/pages/{pageId}`

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
res = client.kong_portal.portals.pages.get(
    page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
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
res = await client.kong_portal.portals.pages.get(
    page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### patch <a name="patch"></a>
Update Page

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Updates the configuration of a single custom page for this portal.

**API Endpoint**: `PATCH /portals/{portalId}/pages/{pageId}`

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
res = client.kong_portal.portals.pages.patch(
    page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    content="Welcome to the About Us page. This is where you can learn about our company.",
    slug="/about-us",
    title="About Us",
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
res = await client.kong_portal.portals.pages.patch(
    page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    content="Welcome to the About Us page. This is where you can learn about our company.",
    slug="/about-us",
    title="About Us",
)
```

### create <a name="create"></a>
Create Page

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Creates a new custom page for this portal. Custom pages can be used to display static content, documentation, or other information to developers.

**API Endpoint**: `POST /portals/{portalId}/pages`

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
res = client.kong_portal.portals.pages.create(
    content="Welcome to the Getting Started page. This is where you can learn how to use our APIs.",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    slug="/getting-started",
    title="Getting Started",
    status="published",
    visibility="public",
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
res = await client.kong_portal.portals.pages.create(
    content="Welcome to the Getting Started page. This is where you can learn how to use our APIs.",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    slug="/getting-started",
    title="Getting Started",
    status="published",
    visibility="public",
)
```
