
# Sideko REST API Python SDK

## Overview
The Sideko API unlocks features including generating SDKs, setting up API Specifications with mock servers, creating documentation projects with generated API references and custom pages, managing roles and permissions, and more.

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
```

## Module Documentation and Snippets

### [kong_portal.applications](sideko_kong_sdk_docs/resources/kong_portal/applications/README.md)

* [get](sideko_kong_sdk_docs/resources/kong_portal/applications/README.md#get) - Fetch Application

### [kong_portal.portal_roles](sideko_kong_sdk_docs/resources/kong_portal/portal_roles/README.md)

* [list](sideko_kong_sdk_docs/resources/kong_portal/portal_roles/README.md#list) - List Portal Roles

### [kong_portal.portals](sideko_kong_sdk_docs/resources/kong_portal/portals/README.md)

* [create](sideko_kong_sdk_docs/resources/kong_portal/portals/README.md#create) - Create Portal
* [delete](sideko_kong_sdk_docs/resources/kong_portal/portals/README.md#delete) - Delete Portal
* [get](sideko_kong_sdk_docs/resources/kong_portal/portals/README.md#get) - Fetch Portal
* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/README.md#list) - List Portals
* [patch](sideko_kong_sdk_docs/resources/kong_portal/portals/README.md#patch) - Update Portal

### [kong_portal.portals.application_registrations](sideko_kong_sdk_docs/resources/kong_portal/portals/application_registrations/README.md)

* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/application_registrations/README.md#list) - List Registrations by Portal

### [kong_portal.portals.applications](sideko_kong_sdk_docs/resources/kong_portal/portals/applications/README.md)

* [delete](sideko_kong_sdk_docs/resources/kong_portal/portals/applications/README.md#delete) - Delete Application by Portal
* [get](sideko_kong_sdk_docs/resources/kong_portal/portals/applications/README.md#get) - Fetch Application by Portal
* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/applications/README.md#list) - List Applications

### [kong_portal.portals.applications.registrations](sideko_kong_sdk_docs/resources/kong_portal/portals/applications/registrations/README.md)

* [delete](sideko_kong_sdk_docs/resources/kong_portal/portals/applications/registrations/README.md#delete) - Delete Registration
* [get](sideko_kong_sdk_docs/resources/kong_portal/portals/applications/registrations/README.md#get) - Fetch Registration
* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/applications/registrations/README.md#list) - List Registrations by Application
* [patch](sideko_kong_sdk_docs/resources/kong_portal/portals/applications/registrations/README.md#patch) - Update Registration

### [kong_portal.portals.assets.favicon](sideko_kong_sdk_docs/resources/kong_portal/portals/assets/favicon/README.md)

* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/assets/favicon/README.md#list) - Get Favicon
* [update](sideko_kong_sdk_docs/resources/kong_portal/portals/assets/favicon/README.md#update) - Replace Favicon

### [kong_portal.portals.assets.logo](sideko_kong_sdk_docs/resources/kong_portal/portals/assets/logo/README.md)

* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/assets/logo/README.md#list) - Get Logo
* [update](sideko_kong_sdk_docs/resources/kong_portal/portals/assets/logo/README.md#update) - Replace Logo

### [kong_portal.portals.authentication_settings](sideko_kong_sdk_docs/resources/kong_portal/portals/authentication_settings/README.md)

* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/authentication_settings/README.md#list) - Get Auth Settings
* [patch](sideko_kong_sdk_docs/resources/kong_portal/portals/authentication_settings/README.md#patch) - Update Auth Settings

### [kong_portal.portals.custom_domain](sideko_kong_sdk_docs/resources/kong_portal/portals/custom_domain/README.md)

* [create](sideko_kong_sdk_docs/resources/kong_portal/portals/custom_domain/README.md#create) - Create Custom Domain
* [delete](sideko_kong_sdk_docs/resources/kong_portal/portals/custom_domain/README.md#delete) - Remove Domain
* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/custom_domain/README.md#list) - Get Custom Domain
* [patch](sideko_kong_sdk_docs/resources/kong_portal/portals/custom_domain/README.md#patch) - Enable or Disable Domain

### [kong_portal.portals.customization](sideko_kong_sdk_docs/resources/kong_portal/portals/customization/README.md)

* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/customization/README.md#list) - Get Customization
* [patch](sideko_kong_sdk_docs/resources/kong_portal/portals/customization/README.md#patch) - Update Customization
* [update](sideko_kong_sdk_docs/resources/kong_portal/portals/customization/README.md#update) - Replace Customization

### [kong_portal.portals.default_content](sideko_kong_sdk_docs/resources/kong_portal/portals/default_content/README.md)

* [create](sideko_kong_sdk_docs/resources/kong_portal/portals/default_content/README.md#create) - Creates Default Pages

### [kong_portal.portals.developers](sideko_kong_sdk_docs/resources/kong_portal/portals/developers/README.md)

* [delete](sideko_kong_sdk_docs/resources/kong_portal/portals/developers/README.md#delete) - Delete Developer
* [get](sideko_kong_sdk_docs/resources/kong_portal/portals/developers/README.md#get) - Fetch Developer
* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/developers/README.md#list) - List Developers
* [patch](sideko_kong_sdk_docs/resources/kong_portal/portals/developers/README.md#patch) - Update Developer

### [kong_portal.portals.developers.teams](sideko_kong_sdk_docs/resources/kong_portal/portals/developers/teams/README.md)

* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/developers/teams/README.md#list) - List Developer Teams

### [kong_portal.portals.identity_provider.team_group_mappings](sideko_kong_sdk_docs/resources/kong_portal/portals/identity_provider/team_group_mappings/README.md)

* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/identity_provider/team_group_mappings/README.md#list) - List Team Group Mappings
* [patch](sideko_kong_sdk_docs/resources/kong_portal/portals/identity_provider/team_group_mappings/README.md#patch) - Update Team Group Mappings

### [kong_portal.portals.identity_providers](sideko_kong_sdk_docs/resources/kong_portal/portals/identity_providers/README.md)

* [create](sideko_kong_sdk_docs/resources/kong_portal/portals/identity_providers/README.md#create) - Create Identity Provider
* [delete](sideko_kong_sdk_docs/resources/kong_portal/portals/identity_providers/README.md#delete) - Delete Identity Provider
* [get](sideko_kong_sdk_docs/resources/kong_portal/portals/identity_providers/README.md#get) - Get Identity Provider
* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/identity_providers/README.md#list) - Retrieve Identity Providers
* [patch](sideko_kong_sdk_docs/resources/kong_portal/portals/identity_providers/README.md#patch) - Update Identity Provider

### [kong_portal.portals.pages](sideko_kong_sdk_docs/resources/kong_portal/portals/pages/README.md)

* [create](sideko_kong_sdk_docs/resources/kong_portal/portals/pages/README.md#create) - Create Page
* [delete](sideko_kong_sdk_docs/resources/kong_portal/portals/pages/README.md#delete) - Delete Page
* [get](sideko_kong_sdk_docs/resources/kong_portal/portals/pages/README.md#get) - Fetch Page
* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/pages/README.md#list) - List Pages
* [patch](sideko_kong_sdk_docs/resources/kong_portal/portals/pages/README.md#patch) - Update Page

### [kong_portal.portals.pages.move](sideko_kong_sdk_docs/resources/kong_portal/portals/pages/move/README.md)

* [update](sideko_kong_sdk_docs/resources/kong_portal/portals/pages/move/README.md#update) - Move Page

### [kong_portal.portals.snippets](sideko_kong_sdk_docs/resources/kong_portal/portals/snippets/README.md)

* [create](sideko_kong_sdk_docs/resources/kong_portal/portals/snippets/README.md#create) - Create Snippet
* [delete](sideko_kong_sdk_docs/resources/kong_portal/portals/snippets/README.md#delete) - Delete Snippet
* [get](sideko_kong_sdk_docs/resources/kong_portal/portals/snippets/README.md#get) - Fetch Snippet
* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/snippets/README.md#list) - List Snippets
* [patch](sideko_kong_sdk_docs/resources/kong_portal/portals/snippets/README.md#patch) - Update Snippet

### [kong_portal.portals.teams](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/README.md)

* [create](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/README.md#create) - Create Team
* [delete](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/README.md#delete) - Delete Team
* [get](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/README.md#get) - Get Team
* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/README.md#list) - List Teams
* [patch](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/README.md#patch) - Update Team

### [kong_portal.portals.teams.assigned_roles](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/assigned_roles/README.md)

* [create](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/assigned_roles/README.md#create) - Assign Role
* [delete](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/assigned_roles/README.md#delete) - Remove Role
* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/assigned_roles/README.md#list) - List Team Roles

### [kong_portal.portals.teams.developers](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/developers/README.md)

* [create](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/developers/README.md#create) - Add Developer to Team
* [delete](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/developers/README.md#delete) - Remove Developer from Team
* [list](sideko_kong_sdk_docs/resources/kong_portal/portals/teams/developers/README.md#list) - List Team Developers

### [sideko.api](sideko_kong_sdk_docs/resources/sideko/api/README.md)

* [create](sideko_kong_sdk_docs/resources/sideko/api/README.md#create) - Create a new API
* [delete](sideko_kong_sdk_docs/resources/sideko/api/README.md#delete) - Delete an API
* [get](sideko_kong_sdk_docs/resources/sideko/api/README.md#get) - Get one API
* [init](sideko_kong_sdk_docs/resources/sideko/api/README.md#init) - Create an API with an initial version
* [list](sideko_kong_sdk_docs/resources/sideko/api/README.md#list) - List your APIs
* [patch](sideko_kong_sdk_docs/resources/sideko/api/README.md#patch) - Update an existing API

### [sideko.api.spec](sideko_kong_sdk_docs/resources/sideko/api/spec/README.md)

* [create](sideko_kong_sdk_docs/resources/sideko/api/spec/README.md#create) - Add a new API specification
* [delete](sideko_kong_sdk_docs/resources/sideko/api/spec/README.md#delete) - Delete an API Specification and it's associated metadata
* [get](sideko_kong_sdk_docs/resources/sideko/api/spec/README.md#get) - Get API specification metadata
* [get_openapi](sideko_kong_sdk_docs/resources/sideko/api/spec/README.md#get_openapi) - Get OpenAPI specification
* [get_stats](sideko_kong_sdk_docs/resources/sideko/api/spec/README.md#get_stats) - Get Stats about the specification
* [list](sideko_kong_sdk_docs/resources/sideko/api/spec/README.md#list) - List specs of a collection
* [patch](sideko_kong_sdk_docs/resources/sideko/api/spec/README.md#patch) - Update an API Specification and/or metadata

### [sideko.api_link](sideko_kong_sdk_docs/resources/sideko/api_link/README.md)

* [create](sideko_kong_sdk_docs/resources/sideko/api_link/README.md#create) - Links API Version to Documentation project version with a specified update policy
* [delete](sideko_kong_sdk_docs/resources/sideko/api_link/README.md#delete) - Removes an API link
* [get](sideko_kong_sdk_docs/resources/sideko/api_link/README.md#get) - Retrieve single API link
* [list](sideko_kong_sdk_docs/resources/sideko/api_link/README.md#list) - List API links for doc version
* [patch](sideko_kong_sdk_docs/resources/sideko/api_link/README.md#patch) - Updates an API link
* [reorder](sideko_kong_sdk_docs/resources/sideko/api_link/README.md#reorder) - Reorder API links and groups

### [sideko.api_link.group](sideko_kong_sdk_docs/resources/sideko/api_link/group/README.md)

* [create](sideko_kong_sdk_docs/resources/sideko/api_link/group/README.md#create) - Create API group to organize API links
* [delete](sideko_kong_sdk_docs/resources/sideko/api_link/group/README.md#delete) - Deletes the api group and all its links
* [list](sideko_kong_sdk_docs/resources/sideko/api_link/group/README.md#list) - List API groups for doc version
* [patch](sideko_kong_sdk_docs/resources/sideko/api_link/group/README.md#patch) - Updates API link group

### [sideko.asset](sideko_kong_sdk_docs/resources/sideko/asset/README.md)

* [create](sideko_kong_sdk_docs/resources/sideko/asset/README.md#create) - Upload Assets
* [delete](sideko_kong_sdk_docs/resources/sideko/asset/README.md#delete) - Delete Asset
* [list](sideko_kong_sdk_docs/resources/sideko/asset/README.md#list) - List Assets
* [patch](sideko_kong_sdk_docs/resources/sideko/asset/README.md#patch) - Update Asset

### [sideko.auth](sideko_kong_sdk_docs/resources/sideko/auth/README.md)

* [exchange_code](sideko_kong_sdk_docs/resources/sideko/auth/README.md#exchange_code) - Exchange one-time auth key for api key

### [sideko.cli](sideko_kong_sdk_docs/resources/sideko/cli/README.md)

* [check_updates](sideko_kong_sdk_docs/resources/sideko/cli/README.md#check_updates) - Checks if current CLI has updates

### [sideko.doc](sideko_kong_sdk_docs/resources/sideko/doc/README.md)

* [check_preview](sideko_kong_sdk_docs/resources/sideko/doc/README.md#check_preview) - A simple check to see if the requesting user has access to the preview doc project
* [create](sideko_kong_sdk_docs/resources/sideko/doc/README.md#create) - Create a new Documentation Project
* [delete](sideko_kong_sdk_docs/resources/sideko/doc/README.md#delete) - Delete a specific Documentation Project
* [get](sideko_kong_sdk_docs/resources/sideko/doc/README.md#get) - Get a specific Documentation Project
* [list](sideko_kong_sdk_docs/resources/sideko/doc/README.md#list) - List Documentation Projects
* [patch](sideko_kong_sdk_docs/resources/sideko/doc/README.md#patch) - Update an existing Documentation Project

### [sideko.doc.deployment](sideko_kong_sdk_docs/resources/sideko/doc/deployment/README.md)

* [get](sideko_kong_sdk_docs/resources/sideko/doc/deployment/README.md#get) - Get a specific deployment for a specific documentation project
* [list](sideko_kong_sdk_docs/resources/sideko/doc/deployment/README.md#list) - List deployments for a specific documentation project
* [trigger](sideko_kong_sdk_docs/resources/sideko/doc/deployment/README.md#trigger) - Deploy a new generated version of documentation with linked guides & APIs

### [sideko.doc.preview](sideko_kong_sdk_docs/resources/sideko/doc/preview/README.md)

* [create_password](sideko_kong_sdk_docs/resources/sideko/doc/preview/README.md#create_password) - A password generator for a documentation project preview environment
* [delete_password](sideko_kong_sdk_docs/resources/sideko/doc/preview/README.md#delete_password) - Deletes a preview environment password
* [list_passwords](sideko_kong_sdk_docs/resources/sideko/doc/preview/README.md#list_passwords) - Lists generated passwords for a documentation project preview environment

### [sideko.doc.theme](sideko_kong_sdk_docs/resources/sideko/doc/theme/README.md)

* [get](sideko_kong_sdk_docs/resources/sideko/doc/theme/README.md#get) - Get the theme attached to a documentation project
* [update](sideko_kong_sdk_docs/resources/sideko/doc/theme/README.md#update) - Update a document project theme

### [sideko.doc.version](sideko_kong_sdk_docs/resources/sideko/doc/version/README.md)

* [get](sideko_kong_sdk_docs/resources/sideko/doc/version/README.md#get) - Get a specific version of an Documentation Project
* [list](sideko_kong_sdk_docs/resources/sideko/doc/version/README.md#list) - List versions of a specific Documentation Project

### [sideko.doc.version.guide](sideko_kong_sdk_docs/resources/sideko/doc/version/guide/README.md)

* [create](sideko_kong_sdk_docs/resources/sideko/doc/version/guide/README.md#create) - Create a guide for a specific version of a documentation project
* [delete](sideko_kong_sdk_docs/resources/sideko/doc/version/guide/README.md#delete) - Delete a specific guide for a specific version of a documentation project
* [get](sideko_kong_sdk_docs/resources/sideko/doc/version/guide/README.md#get) - Get a specific guide for a specific version of a documentation project
* [get_content](sideko_kong_sdk_docs/resources/sideko/doc/version/guide/README.md#get_content) - Get content for a specific guide for a specific version of a documentation project
* [list](sideko_kong_sdk_docs/resources/sideko/doc/version/guide/README.md#list) - List guides for a specific version of a documentation project
* [patch](sideko_kong_sdk_docs/resources/sideko/doc/version/guide/README.md#patch) - Update a specific guide for a specific version of a documentation project
* [reorder](sideko_kong_sdk_docs/resources/sideko/doc/version/guide/README.md#reorder) - Reorder guides for a specific version of a documentation project

### [sideko.health](sideko_kong_sdk_docs/resources/sideko/health/README.md)

* [check](sideko_kong_sdk_docs/resources/sideko/health/README.md#check) - Health Check
* [ping](sideko_kong_sdk_docs/resources/sideko/health/README.md#ping) - Ping Check

### [sideko.lint](sideko_kong_sdk_docs/resources/sideko/lint/README.md)

* [run](sideko_kong_sdk_docs/resources/sideko/lint/README.md#run) - Lint an OpenAPI spec

### [sideko.org](sideko_kong_sdk_docs/resources/sideko/org/README.md)

* [create](sideko_kong_sdk_docs/resources/sideko/org/README.md#create) - Create a new organization
* [get](sideko_kong_sdk_docs/resources/sideko/org/README.md#get) - Get Organization

### [sideko.org.theme](sideko_kong_sdk_docs/resources/sideko/org/theme/README.md)

* [get](sideko_kong_sdk_docs/resources/sideko/org/theme/README.md#get) - Get organization theme
* [update](sideko_kong_sdk_docs/resources/sideko/org/theme/README.md#update) - Update organization theme

### [sideko.role](sideko_kong_sdk_docs/resources/sideko/role/README.md)

* [create](sideko_kong_sdk_docs/resources/sideko/role/README.md#create) - Create a new role
* [delete](sideko_kong_sdk_docs/resources/sideko/role/README.md#delete) - Delete role and all associated permissions
* [list](sideko_kong_sdk_docs/resources/sideko/role/README.md#list) - List roles

### [sideko.sdk](sideko_kong_sdk_docs/resources/sideko/sdk/README.md)

* [generate](sideko_kong_sdk_docs/resources/sideko/sdk/README.md#generate) - Generate a new managed SDK from a Sideko configuration file
* [list](sideko_kong_sdk_docs/resources/sideko/sdk/README.md#list) - List all managed SDKs
* [update](sideko_kong_sdk_docs/resources/sideko/sdk/README.md#update) - Update an SDK to reflect the latest state of the API

### [sideko.sdk.config](sideko_kong_sdk_docs/resources/sideko/sdk/config/README.md)

* [init](sideko_kong_sdk_docs/resources/sideko/sdk/config/README.md#init) - Initialize an SDK configuration with all defaults applied
* [sync](sideko_kong_sdk_docs/resources/sideko/sdk/config/README.md#sync) - Sync an SDK configuration with the latest state of the API

### [sideko.sdk.doc](sideko_kong_sdk_docs/resources/sideko/sdk/doc/README.md)

* [create](sideko_kong_sdk_docs/resources/sideko/sdk/doc/README.md#create) - Retrieve SDK documentation

### [sideko.service_account](sideko_kong_sdk_docs/resources/sideko/service_account/README.md)

* [create](sideko_kong_sdk_docs/resources/sideko/service_account/README.md#create) - Create a new service account with a set of project permissions
* [delete](sideko_kong_sdk_docs/resources/sideko/service_account/README.md#delete) - Delete a service account
* [get](sideko_kong_sdk_docs/resources/sideko/service_account/README.md#get) - Get service account by the ID
* [list](sideko_kong_sdk_docs/resources/sideko/service_account/README.md#list) - List all service accounts in organization

### [sideko.user](sideko_kong_sdk_docs/resources/sideko/user/README.md)

* [invite](sideko_kong_sdk_docs/resources/sideko/user/README.md#invite) - Invite a user to an organization with a specific role

### [sideko.user.me](sideko_kong_sdk_docs/resources/sideko/user/me/README.md)

* [get](sideko_kong_sdk_docs/resources/sideko/user/me/README.md#get) - Get current user profile
* [get_key](sideko_kong_sdk_docs/resources/sideko/user/me/README.md#get_key) - Get API key for the current user

### [sideko.webhook](sideko_kong_sdk_docs/resources/sideko/webhook/README.md)

* [vercel](sideko_kong_sdk_docs/resources/sideko/webhook/README.md#vercel) - webhooks sent to sideko by vercel

<!-- MODULE DOCS END -->
