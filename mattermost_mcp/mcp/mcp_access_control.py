"""
This file was automatically generated. Do not edit manually.
"""
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_access_control_tools(mcp: FastMCP):
    """Register Mattermost MCP access_control tools."""

    @mcp.tool(tags=["access_control"])
    async def mattermost_mcp_access_control(
        action: str = Field(
            description="Action to perform. Must be one of: 'create_access_control_policy', 'check_access_control_policy_expression', 'validate_expression_against_requester', 'test_access_control_policy_expression', 'simulate_access_control_policy_for_users', 'search_access_control_policies', 'get_access_control_policy_autocomplete_fields', 'get_access_control_policy', 'delete_access_control_policy', 'update_access_control_policy_active_status', 'assign_access_control_policy_to_channels', 'unassign_access_control_policy_from_channels', 'get_channels_for_access_control_policy', 'search_channels_for_access_control_policy', 'get_channel_access_control_attributes', 'get_c_e_l_visual_a_s_t', 'update_access_control_policies_active'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP access_control operations."""
        if ctx:
            await ctx.info("Executing access_control operation: " + str(action) + "...")
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
