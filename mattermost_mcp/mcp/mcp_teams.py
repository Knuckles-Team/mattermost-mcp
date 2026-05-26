"""
This file was automatically generated. Do not edit manually.
"""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_teams_tools(mcp: FastMCP):
    """Register Mattermost MCP teams tools."""

    @mcp.tool(tags=["teams"])
    async def mattermost_mcp_teams(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_all_teams', 'create_team', 'get_team', 'update_team', 'soft_delete_team', 'patch_team', 'update_team_privacy', 'restore_team', 'get_team_by_name', 'search_teams', 'team_exists', 'get_teams_for_user', 'get_team_members', 'add_team_member', 'add_team_member_from_invite', 'add_team_members', 'get_team_members_for_user', 'get_team_member', 'remove_team_member', 'get_team_members_by_ids', 'get_team_stats', 'regenerate_team_invite_id', 'get_team_icon', 'set_team_icon', 'remove_team_icon', 'update_team_member_roles', 'update_team_member_scheme_roles', 'get_teams_unread_for_user', 'get_team_unread', 'invite_users_to_team', 'invite_guests_to_team', 'invalidate_email_invites', 'import_team', 'get_team_invite_info', 'update_team_scheme', 'team_members_minus_group_members'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP teams operations."""
        if ctx:
            await ctx.info("Executing teams operation: " + str(action) + "...")
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
