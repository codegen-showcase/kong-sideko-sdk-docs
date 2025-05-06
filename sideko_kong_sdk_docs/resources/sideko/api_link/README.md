
### delete <a name="delete"></a>
Removes an API link



**API Endpoint**: `DELETE /api_link/{id}`

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
res = client.sideko.api_link.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
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
res = await client.sideko.api_link.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
```

### list <a name="list"></a>
List API links for doc version



**API Endpoint**: `GET /api_link`

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
res = client.sideko.api_link.list(
    doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
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
res = await client.sideko.api_link.list(
    doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

### get <a name="get"></a>
Retrieve single API link



**API Endpoint**: `GET /api_link/{id}`

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
res = client.sideko.api_link.get(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
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
res = await client.sideko.api_link.get(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
```

### patch <a name="patch"></a>
Updates an API link



**API Endpoint**: `PATCH /api_link/{id}`

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
res = client.sideko.api_link.patch(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
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
res = await client.sideko.api_link.patch(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
```

### create <a name="create"></a>
Links API Version to Documentation project version with a specified update policy



**API Endpoint**: `POST /api_link`

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
res = client.sideko.api_link.create(
    doc_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    group_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    nav_label="string",
    policy={"api_id": "my-api", "type_": "latest"},
    slug="string",
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
res = await client.sideko.api_link.create(
    doc_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    group_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    nav_label="string",
    policy={"api_id": "my-api", "type_": "latest"},
    slug="string",
)
```

### reorder <a name="reorder"></a>
Reorder API links and groups



**API Endpoint**: `POST /api_link/reorder`

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
res = client.sideko.api_link.reorder(
    doc_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    groups=[{"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "order": 123}],
    links=[
        {
            "group_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "order": 123,
        }
    ],
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
res = await client.sideko.api_link.reorder(
    doc_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    groups=[{"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "order": 123}],
    links=[
        {
            "group_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "order": 123,
        }
    ],
)
```
