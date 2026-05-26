"""
This file was automatically generated. Do not edit manually.
"""
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_sharedchannels_tools(mcp: FastMCP):
    """Register Mattermost MCP sharedchannels tools."""

    @mcp.tool(tags=["sharedchannels"])
    async def mattermost_mcp_sharedchannels(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_all_shared_channels', 'get_shared_channel_remotes_by_remote_cluster', 'get_remote_cluster_info', 'invite_remote_cluster_to_channel', 'uninvite_remote_cluster_to_channel', 'get_shared_channel_remotes', 'can_user_direct_message'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP sharedchannels operations."""
        if ctx:
            await ctx.info("Executing sharedchannels operation: " + str(action) + "...")
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
