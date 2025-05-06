
### delete <a name="delete"></a>
Delete an API Specification and it's associated metadata



**API Endpoint**: `DELETE /api/{api_name}/spec/{api_version}`

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
res = client.sideko.api.spec.delete(api_name="my-project", api_version="latest")
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
res = await client.sideko.api.spec.delete(api_name="my-project", api_version="latest")
```

### list <a name="list"></a>
List specs of a collection



**API Endpoint**: `GET /api/{api_name}/spec`

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
res = client.sideko.api.spec.list(api_name="my-project")
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
res = await client.sideko.api.spec.list(api_name="my-project")
```

### get <a name="get"></a>
Get API specification metadata



**API Endpoint**: `GET /api/{api_name}/spec/{api_version}`

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
res = client.sideko.api.spec.get(api_name="my-project", api_version="latest")
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
res = await client.sideko.api.spec.get(api_name="my-project", api_version="latest")
```

### get_openapi <a name="get_openapi"></a>
Get OpenAPI specification



**API Endpoint**: `GET /api/{api_name}/spec/{api_version}/openapi`

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
res = client.sideko.api.spec.get_openapi(api_name="my-project", api_version="latest")
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
res = await client.sideko.api.spec.get_openapi(
    api_name="my-project", api_version="latest"
)
```

### get_stats <a name="get_stats"></a>
Get Stats about the specification



**API Endpoint**: `GET /api/{api_name}/spec/{api_version}/stats`

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
res = client.sideko.api.spec.get_stats(api_name="my-project", api_version="latest")
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
res = await client.sideko.api.spec.get_stats(
    api_name="my-project", api_version="latest"
)
```

### patch <a name="patch"></a>
Update an API Specification and/or metadata



**API Endpoint**: `PATCH /api/{api_name}/spec/{api_version}`

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
res = client.sideko.api.spec.patch(
    api_name="my-project",
    api_version="latest",
    notes="<p>This version includes a number of excellent improvements</p>",
    openapi=open("uploads/openapi.yaml", "rb"),
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
res = await client.sideko.api.spec.patch(
    api_name="my-project",
    api_version="latest",
    notes="<p>This version includes a number of excellent improvements</p>",
    openapi=open("uploads/openapi.yaml", "rb"),
)
```

### create <a name="create"></a>
Add a new API specification



**API Endpoint**: `POST /api/{api_name}/spec`

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
res = client.sideko.api.spec.create(
    api_name="my-project",
    openapi=open("uploads/openapi.yaml", "rb"),
    version="major",
    notes="<p>This version includes a number of excellent improvements</p>",
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
res = await client.sideko.api.spec.create(
    api_name="my-project",
    openapi=open("uploads/openapi.yaml", "rb"),
    version="major",
    notes="<p>This version includes a number of excellent improvements</p>",
)
```
