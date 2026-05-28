"""
This file was automatically generated. Do not edit manually.
"""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_oauth_tools(mcp: FastMCP):
    """Register Mattermost MCP oauth tools."""

    @mcp.tool(tags=["oauth"])
    async def mattermost_mcp_oauth(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_o_auth_apps', 'create_o_auth_app', 'get_o_auth_app', 'update_o_auth_app', 'delete_o_auth_app', 'regenerate_o_auth_app_secret', 'get_o_auth_app_info', 'get_authorization_server_metadata', 'register_o_auth_client', 'get_authorized_o_auth_apps_for_user'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP oauth operations."""
        if ctx:
            await ctx.info("Executing oauth operation: " + str(action) + "...")
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
