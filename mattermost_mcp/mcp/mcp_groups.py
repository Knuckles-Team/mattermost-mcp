"""
This file was automatically generated. Do not edit manually.
"""
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_groups_tools(mcp: FastMCP):
    """Register Mattermost MCP groups tools."""

    @mcp.tool(tags=["groups"])
    async def mattermost_mcp_groups(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_groups', 'create_group', 'get_group', 'delete_group', 'patch_group', 'restore_group', 'link_group_syncable_for_team', 'unlink_group_syncable_for_team', 'link_group_syncable_for_channel', 'unlink_group_syncable_for_channel', 'get_group_syncable_for_team_id', 'get_group_syncable_for_channel_id', 'get_group_syncables_teams', 'get_group_syncables_channels', 'patch_group_syncable_for_team', 'patch_group_syncable_for_channel', 'get_group_users', 'add_group_members', 'delete_group_members', 'get_group_stats', 'get_groups_by_channel', 'get_groups_by_team', 'get_groups_associated_to_channels_by_team', 'get_groups_by_user_id', 'get_groups_by_names'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP groups operations."""
        if ctx:
            await ctx.info("Executing groups operation: " + str(action) + "...")
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
