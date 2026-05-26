"""
This file was automatically generated. Do not edit manually.
"""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_channels_tools(mcp: FastMCP):
    """Register Mattermost MCP channels tools."""

    @mcp.tool(tags=["channels"])
    async def mattermost_mcp_channels(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_all_channels', 'create_channel', 'create_direct_channel', 'create_group_channel', 'search_all_channels', 'search_group_channels', 'get_public_channels_by_ids_for_team', 'get_channel_members_timezones', 'get_channel', 'update_channel', 'delete_channel', 'patch_channel', 'update_channel_privacy', 'restore_channel', 'move_channel', 'get_channel_stats', 'get_pinned_posts', 'get_public_channels_for_team', 'get_private_channels_for_team', 'get_recommended_channels_for_team', 'get_deleted_channels_for_team', 'autocomplete_channels_for_team', 'autocomplete_channels_for_team_for_search', 'get_managed_categories', 'search_channels', 'get_channel_by_name', 'get_channel_by_name_for_team_name', 'get_channel_members', 'add_channel_member', 'set_channel_members', 'get_channel_members_by_ids', 'get_channel_member', 'remove_user_from_channel', 'update_channel_roles', 'update_channel_member_scheme_roles', 'update_channel_notify_props', 'update_channel_member_autotranslation', 'mark_channels_read_for_user', 'get_channels_member_count', 'view_channel', 'mark_all_direct_messages_read', 'get_channel_members_for_user', 'get_channels_for_team_for_user', 'get_channels_for_user', 'get_channel_unread', 'update_channel_scheme', 'channel_members_minus_group_members', 'get_channel_member_counts_by_group', 'get_channel_moderations', 'patch_channel_moderations', 'get_sidebar_categories_for_team_for_user', 'create_sidebar_category_for_team_for_user', 'update_sidebar_categories_for_team_for_user', 'get_sidebar_category_order_for_team_for_user', 'update_sidebar_category_order_for_team_for_user', 'get_sidebar_category_for_team_for_user', 'update_sidebar_category_for_team_for_user', 'remove_sidebar_category_for_team_for_user', 'get_group_message_members_common_teams', 'convert_group_message_to_channel'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP channels operations."""
        if ctx:
            await ctx.info("Executing channels operation: " + str(action) + "...")
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
