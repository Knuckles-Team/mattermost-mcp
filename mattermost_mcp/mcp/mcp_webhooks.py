"""
This file was automatically generated. Do not edit manually.
"""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_webhooks_tools(mcp: FastMCP):
    """Register Mattermost MCP webhooks tools."""

    @mcp.tool(tags=["webhooks"])
    async def mattermost_mcp_webhooks(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_incoming_webhooks', 'create_incoming_webhook', 'get_incoming_webhook', 'update_incoming_webhook', 'delete_incoming_webhook', 'get_outgoing_webhooks', 'create_outgoing_webhook', 'get_outgoing_webhook', 'update_outgoing_webhook', 'delete_outgoing_webhook', 'regen_outgoing_hook_token'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP webhooks operations."""
        if ctx:
            await ctx.info("Executing webhooks operation: " + str(action) + "...")
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
