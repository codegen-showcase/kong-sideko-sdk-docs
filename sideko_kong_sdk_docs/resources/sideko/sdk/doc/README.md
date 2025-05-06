
### create <a name="create"></a>
Retrieve SDK documentation

Get documentation for a specific SDK

**API Endpoint**: `POST /sdk/{sdk_id}/doc`

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
res = client.sideko.sdk.doc.create(sdk_id="h1jasdf123", modules_filter=["user.admin"])
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
res = await client.sideko.sdk.doc.create(
    sdk_id="h1jasdf123", modules_filter=["user.admin"]
)
```
