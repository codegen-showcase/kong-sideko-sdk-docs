
### delete <a name="delete"></a>
Delete a specific guide for a specific version of a documentation project



**API Endpoint**: `DELETE /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id}`

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
res = client.sideko.doc.version.guide.delete(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.sideko.doc.version.guide.delete(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### list <a name="list"></a>
List guides for a specific version of a documentation project



**API Endpoint**: `GET /doc_project/{doc_name}/version/{doc_version}/guide`

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
res = client.sideko.doc.version.guide.list(
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
res = await client.sideko.doc.version.guide.list(
    doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

### get <a name="get"></a>
Get a specific guide for a specific version of a documentation project



**API Endpoint**: `GET /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id}`

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
res = client.sideko.doc.version.guide.get(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.sideko.doc.version.guide.get(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### get_content <a name="get_content"></a>
Get content for a specific guide for a specific version of a documentation project



**API Endpoint**: `GET /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id}/content`

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
res = client.sideko.doc.version.guide.get_content(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.sideko.doc.version.guide.get_content(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### patch <a name="patch"></a>
Update a specific guide for a specific version of a documentation project



**API Endpoint**: `PATCH /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id}`

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
res = client.sideko.doc.version.guide.patch(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    icon="house",
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
res = await client.sideko.doc.version.guide.patch(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    icon="house",
)
```

### create <a name="create"></a>
Create a guide for a specific version of a documentation project



**API Endpoint**: `POST /doc_project/{doc_name}/version/{doc_version}/guide`

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
res = client.sideko.doc.version.guide.create(
    content="string",
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    is_parent=True,
    nav_label="string",
    slug="string",
    icon="house",
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
res = await client.sideko.doc.version.guide.create(
    content="string",
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    is_parent=True,
    nav_label="string",
    slug="string",
    icon="house",
)
```

### reorder <a name="reorder"></a>
Reorder guides for a specific version of a documentation project



**API Endpoint**: `POST /doc_project/{doc_name}/version/{doc_version}/guide/reorder`

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
res = client.sideko.doc.version.guide.reorder(
    data=[
        {
            "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "order": 123,
            "parent_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        }
    ],
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.sideko.doc.version.guide.reorder(
    data=[
        {
            "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "order": 123,
            "parent_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        }
    ],
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```
