"""
This file was automatically generated. Do not edit manually.
"""
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_plugins_tools(mcp: FastMCP):
    """Register Mattermost MCP plugins tools."""

    @mcp.tool(tags=["plugins"])
    async def mattermost_mcp_plugins(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_plugins', 'upload_plugin', 'install_plugin_from_url', 'remove_plugin', 'enable_plugin', 'disable_plugin', 'get_webapp_plugins', 'get_plugin_statuses', 'get_marketplace_plugins', 'install_marketplace_plugin', 'get_marketplace_visited_by_admin', 'update_marketplace_visited_by_admin', 'reattach_plugin', 'detach_plugin'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP plugins operations."""
        if ctx:
            await ctx.info("Executing plugins operation: " + str(action) + "...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": "Invalid params_json: " + str(e)}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        method = getattr(client, action, None)
        if not method:
            alt_action = action.replace("-", "_").replace(" ", "_").lower()
            method = getattr(client, alt_action, None)

        if not method:
            return {"error": "Unknown action '" + str(action) + "' on client."}

        try:
            res = method(**kwargs)
            if res is None:
                return {"status": "success"}
            return res
        except Exception as e:
            return {"error": "Failed to execute operation " + str(action) + ": " + str(e)}
