"""
This file was automatically generated. Do not edit manually.
"""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_posts_tools(mcp: FastMCP):
    """Register Mattermost MCP posts tools."""

    @mcp.tool(tags=["posts"])
    async def mattermost_mcp_posts(
        action: str = Field(
            description="Action to perform. Must be one of: 'create_post', 'create_post_ephemeral', 'search_posts_in_all_teams', 'get_post', 'update_post', 'delete_post', 'set_post_unread', 'patch_post', 'get_post_thread', 'get_flagged_posts_for_user', 'get_file_infos_for_post', 'get_post_info', 'get_edit_history_for_post', 'get_posts_for_channel', 'get_posts_around_last_unread', 'search_posts', 'pin_post', 'unpin_post', 'do_post_action', 'get_posts_by_ids', 'set_post_reminder', 'save_acknowledgement_for_post', 'delete_acknowledgement_for_post', 'move_thread', 'restore_post_version', 'reveal_post', 'burn_post', 'rewrite_message'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP posts operations."""
        if ctx:
            await ctx.info("Executing posts operation: " + str(action) + "...")
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
