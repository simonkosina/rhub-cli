from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_location_location_update_json_body import RhubApiLabLocationLocationUpdateJsonBody
from ...models.rhub_api_lab_location_location_update_response_default import (
    RhubApiLabLocationLocationUpdateResponseDefault,
)
from ...types import Response


def _get_kwargs(
    location_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabLocationLocationUpdateJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/location/{location_id}".format(client.base_url, location_id=location_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, RhubApiLabLocationLocationUpdateResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiLabLocationLocationUpdateResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiLabLocationLocationUpdateResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    location_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabLocationLocationUpdateJsonBody,
) -> Response[Union[Any, RhubApiLabLocationLocationUpdateResponseDefault]]:
    """Update location

    Args:
        location_id (int):
        json_body (RhubApiLabLocationLocationUpdateJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabLocationLocationUpdateResponseDefault]]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    location_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabLocationLocationUpdateJsonBody,
) -> Optional[Union[Any, RhubApiLabLocationLocationUpdateResponseDefault]]:
    """Update location

    Args:
        location_id (int):
        json_body (RhubApiLabLocationLocationUpdateJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabLocationLocationUpdateResponseDefault]]
    """

    return sync_detailed(
        location_id=location_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    location_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabLocationLocationUpdateJsonBody,
) -> Response[Union[Any, RhubApiLabLocationLocationUpdateResponseDefault]]:
    """Update location

    Args:
        location_id (int):
        json_body (RhubApiLabLocationLocationUpdateJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabLocationLocationUpdateResponseDefault]]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    location_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabLocationLocationUpdateJsonBody,
) -> Optional[Union[Any, RhubApiLabLocationLocationUpdateResponseDefault]]:
    """Update location

    Args:
        location_id (int):
        json_body (RhubApiLabLocationLocationUpdateJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabLocationLocationUpdateResponseDefault]]
    """

    return (
        await asyncio_detailed(
            location_id=location_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
