"""
This file was automatically generated. Do not edit manually.
"""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_preferences_tools(mcp: FastMCP):
    """Register Mattermost MCP preferences tools."""

    @mcp.tool(tags=["preferences"])
    async def mattermost_mcp_preferences(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_preferences', 'update_preferences', 'delete_preferences', 'get_preferences_by_category', 'get_preferences_by_category_by_name'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP preferences operations."""
        if ctx:
            await ctx.info("Executing preferences operation: " + str(action) + "...")
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
            return {
                "error": "Failed to execute operation " + str(action) + ": " + str(e)
            }
