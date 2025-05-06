
### list <a name="list"></a>
List all managed SDKs



**API Endpoint**: `GET /sdk`

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
res = client.sideko.sdk.list()
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
res = await client.sideko.sdk.list()
```

### generate <a name="generate"></a>
Generate a new managed SDK from a Sideko configuration file



**API Endpoint**: `POST /sdk`

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
res = client.sideko.sdk.generate(
    config=open("uploads/config.yaml", "rb"), language="go", sdk_version="0.1.0"
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
res = await client.sideko.sdk.generate(
    config=open("uploads/config.yaml", "rb"), language="go", sdk_version="0.1.0"
)
```

### update <a name="update"></a>
Update an SDK to reflect the latest state of the API



**API Endpoint**: `POST /sdk/update`

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
res = client.sideko.sdk.update(
    config=open("uploads/config.yaml", "rb"),
    prev_sdk_git=open("uploads/git.tar.gz", "rb"),
    prev_sdk_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    sdk_version="major",
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
res = await client.sideko.sdk.update(
    config=open("uploads/config.yaml", "rb"),
    prev_sdk_git=open("uploads/git.tar.gz", "rb"),
    prev_sdk_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    sdk_version="major",
)
```
