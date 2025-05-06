
### delete <a name="delete"></a>
Delete a service account



**API Endpoint**: `DELETE /service_account/{id}`

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
res = client.sideko.service_account.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
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
res = await client.sideko.service_account.delete(
    id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

### list <a name="list"></a>
List all service accounts in organization



**API Endpoint**: `GET /service_account`

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
res = client.sideko.service_account.list()
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
res = await client.sideko.service_account.list()
```

### get <a name="get"></a>
Get service account by the ID



**API Endpoint**: `GET /service_account/{id}`

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
res = client.sideko.service_account.get(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
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
res = await client.sideko.service_account.get(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
```

### create <a name="create"></a>
Create a new service account with a set of project permissions



**API Endpoint**: `POST /service_account`

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
res = client.sideko.service_account.create(
    name="Documentation Publisher Service Account",
    object_roles=[
        {
            "object_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "object_type": "api_project",
            "role_definition_id": "ApiProjectAdmin",
        }
    ],
    expiration="2025-01-01T00:00:00",
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
res = await client.sideko.service_account.create(
    name="Documentation Publisher Service Account",
    object_roles=[
        {
            "object_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "object_type": "api_project",
            "role_definition_id": "ApiProjectAdmin",
        }
    ],
    expiration="2025-01-01T00:00:00",
)
```
