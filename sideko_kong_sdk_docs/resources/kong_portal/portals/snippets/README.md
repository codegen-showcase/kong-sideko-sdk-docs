
### delete <a name="delete"></a>
Delete Snippet

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Deletes a single custom snippet for this portal.

**API Endpoint**: `DELETE /portals/{portalId}/snippets/{snippetId}`

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
res = client.kong_portal.portals.snippets.delete(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
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
res = await client.kong_portal.portals.snippets.delete(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
)
```

### list <a name="list"></a>
List Snippets

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Returns the paginated list of custom snippets that have been created for this portal.

**API Endpoint**: `GET /portals/{portalId}/snippets`

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
res = client.kong_portal.portals.snippets.list(
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
res = await client.kong_portal.portals.snippets.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", page_number=1, page_size=10
)
```

### get <a name="get"></a>
Fetch Snippet

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Returns the configuration of a single custom snippet for this portal. Custom snippets can be used to display static content, documentation, or other information to developers.

**API Endpoint**: `GET /portals/{portalId}/snippets/{snippetId}`

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
res = client.kong_portal.portals.snippets.get(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
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
res = await client.kong_portal.portals.snippets.get(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
)
```

### patch <a name="patch"></a>
Update Snippet

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Updates the configuration of a single custom snippet for this portal.

**API Endpoint**: `PATCH /portals/{portalId}/snippets/{snippetId}`

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
res = client.kong_portal.portals.snippets.patch(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
    content="Welcome to the About Us page. This is where you can learn about our company.",
    name="about-us",
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
res = await client.kong_portal.portals.snippets.patch(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    snippet_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
    content="Welcome to the About Us page. This is where you can learn about our company.",
    name="about-us",
    title="About Us",
)
```

### create <a name="create"></a>
Create Snippet

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Creates a new custom snippet for this portal. Custom snippets can be used to display static content, documentation, or other information to developers.

**API Endpoint**: `POST /portals/{portalId}/snippets`

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
res = client.kong_portal.portals.snippets.create(
    content="Welcome to the Getting Started page. This is where you can learn how to use our APIs.",
    name="getting-started",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.kong_portal.portals.snippets.create(
    content="Welcome to the Getting Started page. This is where you can learn how to use our APIs.",
    name="getting-started",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    title="Getting Started",
    status="published",
    visibility="public",
)
```
