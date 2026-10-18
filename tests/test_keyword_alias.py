"""A body field named after a Python keyword keeps its wire name end to end."""

from __future__ import annotations

import sys
from unittest.mock import patch

import pytest
from fastmcp import Client


@pytest.mark.anyio
async def test_from_is_exposed_and_sent_as_from(monkeypatch) -> None:
    monkeypatch.setattr(sys, "argv", ["mattermost-mcp"])
    from mattermost_mcp.api import api_client_base
    from mattermost_mcp.mcp_server import get_mcp_instance

    mcp = get_mcp_instance()[0]
    for middleware in list(mcp.middleware):
        mcp.middleware.remove(middleware)
    tools = {t.name: t for t in await mcp.list_tools()}
    schema = tools["mattermost_migrate_config"].parameters["properties"]
    assert "from" in schema
    assert "from_" not in schema

    sent: dict = {}

    def capture(self, method, endpoint, params=None, data=None):
        sent["wire"] = api_client_base._wire_names(data)
        return {"status": "success"}

    with patch.object(api_client_base.ApiClientBase, "request", capture):
        async with Client(mcp) as client:
            await client.call_tool(
                "mattermost_migrate_config", {"from": "a.json", "to": "b.json"}
            )
    assert sent["wire"] == {"from": "a.json", "to": "b.json"}
