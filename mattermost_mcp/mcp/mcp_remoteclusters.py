"""
This file was automatically generated. Do not edit manually.
"""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_remoteclusters_tools(mcp: FastMCP):
    """Register Mattermost MCP remoteclusters tools."""

    @mcp.tool(tags=["remoteclusters"])
    async def mattermost_mcp_remoteclusters(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_remote_clusters', 'create_remote_cluster', 'get_remote_cluster', 'delete_remote_cluster', 'patch_remote_cluster', 'generate_remote_cluster_invite', 'accept_remote_cluster_invite', 'remote_cluster_ping', 'remote_cluster_accept_message', 'remote_cluster_confirm_invite', 'upload_remote_cluster_data', 'remote_set_profile_image'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP remoteclusters operations."""
        if ctx:
            await ctx.info("Executing remoteclusters operation: " + str(action) + "...")
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
