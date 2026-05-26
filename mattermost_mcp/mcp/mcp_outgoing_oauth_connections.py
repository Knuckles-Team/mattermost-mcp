"""
This file was automatically generated. Do not edit manually.
"""
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_outgoing_oauth_connections_tools(mcp: FastMCP):
    """Register Mattermost MCP outgoing_oauth_connections tools."""

    @mcp.tool(tags=["outgoing_oauth_connections"])
    async def mattermost_mcp_outgoing_oauth_connections(
        action: str = Field(
            description="Action to perform. Must be one of: 'list_outgoing_o_auth_connections', 'create_outgoing_o_auth_connection', 'get_outgoing_o_auth_connection', 'update_outgoing_o_auth_connection', 'delete_outgoing_o_auth_connection', 'validate_outgoing_o_auth_connection'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP outgoing_oauth_connections operations."""
        if ctx:
            await ctx.info("Executing outgoing_oauth_connections operation: " + str(action) + "...")
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
