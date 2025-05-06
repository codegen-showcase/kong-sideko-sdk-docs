
### list <a name="list"></a>
List deployments for a specific documentation project

Retrieves all deployments for a doc project

**API Endpoint**: `GET /doc_project/{doc_name}/deployment`

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
res = client.sideko.doc.deployment.list(doc_name="my-project")
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
res = await client.sideko.doc.deployment.list(doc_name="my-project")
```

### get <a name="get"></a>
Get a specific deployment for a specific documentation project

Retrieves single deployment

**API Endpoint**: `GET /doc_project/{doc_name}/deployment/{deployment_id}`

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
res = client.sideko.doc.deployment.get(
    deployment_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", doc_name="my-project"
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
res = await client.sideko.doc.deployment.get(
    deployment_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", doc_name="my-project"
)
```

### trigger <a name="trigger"></a>
Deploy a new generated version of documentation with linked guides & APIs

Deploys a new generated version of documentation with linked guides & APIs

**API Endpoint**: `POST /doc_project/{doc_name}/deployment`

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
res = client.sideko.doc.deployment.trigger(doc_name="my-project", target="Preview")
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
res = await client.sideko.doc.deployment.trigger(
    doc_name="my-project", target="Preview"
)
```
