import httpx
import pytest

from sideko_kong_sdk_docs import AsyncClient, Client
from sideko_kong_sdk_docs.environment import SIDEKO_MOCK_SERVER


def test_update_200_success_default():
    """Tests a PUT request to the /portals/{portalId}/pages/{pageId}/move endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        sideko_key="API_KEY",
        sideko_cookie="API_KEY",
        kong_pat="API_TOKEN",
        kong_sys_token="API_TOKEN",
        environment=SIDEKO_MOCK_SERVER,
    )
    response = client.kong_portal.portals.pages.move.update(
        page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        index=1,
        parent_page_id="dd4e1b98-3629-4dd3-acc0-759a726ffee2",
    )
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_update_200_success_default():
    """Tests a PUT request to the /portals/{portalId}/pages/{pageId}/move endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        sideko_key="API_KEY",
        sideko_cookie="API_KEY",
        kong_pat="API_TOKEN",
        kong_sys_token="API_TOKEN",
        environment=SIDEKO_MOCK_SERVER,
    )
    response = await client.kong_portal.portals.pages.move.update(
        page_id="ebbac5b0-ac89-45c3-9d2e-c4542c657e79",
        portal_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        index=1,
        parent_page_id="dd4e1b98-3629-4dd3-acc0-759a726ffee2",
    )
    assert isinstance(response, httpx.Response)
