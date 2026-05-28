"""
This file was automatically generated. Do not edit manually.
"""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_content_flagging_tools(mcp: FastMCP):
    """Register Mattermost MCP content_flagging tools."""

    @mcp.tool(tags=["content_flagging"])
    async def mattermost_mcp_content_flagging(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_c_f_flag_config', 'get_c_f_team_status', 'post_c_f_post_flag', 'get_c_f_fields', 'get_c_f_post_field_values', 'get_c_f_post', 'remove_c_f_post', 'keep_c_f_post', 'get_c_f_config', 'update_c_f_config', 'search_c_f_team_reviewers', 'post_c_f_post_reviewer', 'generate_c_f_post_report'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP content_flagging operations."""
        if ctx:
            await ctx.info(
                "Executing content_flagging operation: " + str(action) + "..."
            )
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
