
### init <a name="init"></a>
Initialize an SDK configuration with all defaults applied

Creates a sdk config with default configurations for the api/api version

**API Endpoint**: `POST /sdk/config/init`

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
res = client.sideko.sdk.config.init(api_name="my-project")
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
res = await client.sideko.sdk.config.init(api_name="my-project")
```

### sync <a name="sync"></a>
Sync an SDK configuration with the latest state of the API

Updates provided config with missing default configurations for the api version

**API Endpoint**: `POST /sdk/config/sync`

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
res = client.sideko.sdk.config.sync(
    config=open("uploads/config.yaml", "rb"), openapi=open("uploads/openapi.yaml", "rb")
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
res = await client.sideko.sdk.config.sync(
    config=open("uploads/config.yaml", "rb"), openapi=open("uploads/openapi.yaml", "rb")
)
```
