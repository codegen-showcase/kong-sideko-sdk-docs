
### update <a name="update"></a>
Move Page

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

This api allows the user to move a page within the page tree using the parameters parent_page_id and index. If parent_page_id is not provided, the page will be placed at the top level of the page tree. index represents a zero-indexed page order relative to its siblings under the same parent. For example, if we want to put the page at top level in first position we would send parent_page_id: null and index: 0. This api also supports using a negative index to count backwards from the end of the page list, which means you can put the page in last position by using index: -1.

**API Endpoint**: `PUT /portals/{portalId}/pages/{pageId}/move`

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
res = client.kong_portal.portals.pages.move.update(
    page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    index=1,
    parent_page_id="dd4e1b98-3629-4dd3-acc0-759a726ffee2",
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
res = await client.kong_portal.portals.pages.move.update(
    page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    index=1,
    parent_page_id="dd4e1b98-3629-4dd3-acc0-759a726ffee2",
)
```
