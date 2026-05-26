"""
This file was automatically generated. Do not edit manually.
"""
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_custom_profile_attributes_tools(mcp: FastMCP):
    """Register Mattermost MCP custom_profile_attributes tools."""

    @mcp.tool(tags=["custom_profile_attributes"])
    async def mattermost_mcp_custom_profile_attributes(
        action: str = Field(
            description="Action to perform. Must be one of: 'list_all_c_p_a_fields', 'create_c_p_a_field', 'delete_c_p_a_field', 'patch_c_p_a_field', 'patch_c_p_a_values', 'get_c_p_a_group', 'list_c_p_a_values', 'patch_c_p_a_values_for_user'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP custom_profile_attributes operations."""
        if ctx:
            await ctx.info("Executing custom_profile_attributes operation: " + str(action) + "...")
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
