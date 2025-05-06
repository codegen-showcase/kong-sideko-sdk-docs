
### delete <a name="delete"></a>
Delete Identity Provider

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Deletes an existing identity provider configuration. This operation removes a specific identity provider
from the portal.

**API Endpoint**: `DELETE /portals/{portalId}/identity-providers/{id}`

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
res = client.kong_portal.portals.identity_providers.delete(
    id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.kong_portal.portals.identity_providers.delete(
    id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### list <a name="list"></a>
Retrieve Identity Providers

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Retrieves the identity providers available within the portal. This operation provides information about
various identity providers for SAML or OIDC authentication integrations.

**API Endpoint**: `GET /portals/{portalId}/identity-providers`

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
res = client.kong_portal.portals.identity_providers.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
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
res = await client.kong_portal.portals.identity_providers.list(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

### get <a name="get"></a>
Get Identity Provider

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Retrieves the configuration of a single identity provider. This operation returns information about a
specific identity provider's settings and authentication integration details.

**API Endpoint**: `GET /portals/{portalId}/identity-providers/{id}`

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
res = client.kong_portal.portals.identity_providers.get(
    id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
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
res = await client.kong_portal.portals.identity_providers.get(
    id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)
```

### patch <a name="patch"></a>
Update Identity Provider

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Updates the configuration of an existing identity provider. This operation allows modifications to be made
to an existing identity provider's configuration.

**API Endpoint**: `PATCH /portals/{portalId}/identity-providers/{id}`

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
res = client.kong_portal.portals.identity_providers.patch(
    id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    config={
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET",
        "issuer_url": "https://konghq.okta.com/oauth2/default",
    },
    enabled=True,
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
res = await client.kong_portal.portals.identity_providers.patch(
    id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    config={
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET",
        "issuer_url": "https://konghq.okta.com/oauth2/default",
    },
    enabled=True,
)
```

### create <a name="create"></a>
Create Identity Provider

**Pre-release Endpoint**
This endpoint is currently in beta and is subject to change.

Creates a new identity provider. This operation allows the creation of a new identity provider for
authentication purposes.

**API Endpoint**: `POST /portals/{portalId}/identity-providers`

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
res = client.kong_portal.portals.identity_providers.create(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    config={
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET",
        "issuer_url": "https://konghq.okta.com/oauth2/default",
    },
    type_="oidc",
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
res = await client.kong_portal.portals.identity_providers.create(
    portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    config={
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET",
        "issuer_url": "https://konghq.okta.com/oauth2/default",
    },
    type_="oidc",
)
```
