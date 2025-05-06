
### get <a name="get"></a>
Get organization theme

Retrieves the documentation project theme configured at the organization level

**API Endpoint**: `GET /organization/theme`

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
res = client.sideko.org.theme.get()
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
res = await client.sideko.org.theme.get()
```

### update <a name="update"></a>
Update organization theme

Update documentation project theme configured at the organization level

**API Endpoint**: `PUT /organization/theme`

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
res = client.sideko.org.theme.update(
    api_reference_group_variant="grouped",
    dark_active_button_bg_color="#FFFFFF",
    dark_active_button_text_color="#FFFFFF",
    dark_bg_color="#FFFFFF",
    dark_navbar_color="#FFFFFF",
    dark_navbar_text_color="#FFFFFF",
    light_active_button_bg_color="#FFFFFF",
    light_active_button_text_color="#FFFFFF",
    light_bg_color="#FFFFFF",
    light_navbar_color="#FFFFFF",
    light_navbar_text_color="#FFFFFF",
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
res = await client.sideko.org.theme.update(
    api_reference_group_variant="grouped",
    dark_active_button_bg_color="#FFFFFF",
    dark_active_button_text_color="#FFFFFF",
    dark_bg_color="#FFFFFF",
    dark_navbar_color="#FFFFFF",
    dark_navbar_text_color="#FFFFFF",
    light_active_button_bg_color="#FFFFFF",
    light_active_button_text_color="#FFFFFF",
    light_bg_color="#FFFFFF",
    light_navbar_color="#FFFFFF",
    light_navbar_text_color="#FFFFFF",
)
```
