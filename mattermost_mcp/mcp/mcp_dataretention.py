"""
This file was automatically generated. Do not edit manually.
"""
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_dataretention_tools(mcp: FastMCP):
    """Register Mattermost MCP dataretention tools."""

    @mcp.tool(tags=["dataretention"])
    async def mattermost_mcp_dataretention(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_data_retention_policy', 'get_data_retention_policies_count', 'get_data_retention_policies', 'create_data_retention_policy', 'get_data_retention_policy_by_i_d', 'delete_data_retention_policy', 'patch_data_retention_policy', 'get_teams_for_retention_policy', 'add_teams_to_retention_policy', 'remove_teams_from_retention_policy', 'search_teams_for_retention_policy', 'get_channels_for_retention_policy', 'add_channels_to_retention_policy', 'remove_channels_from_retention_policy', 'search_channels_for_retention_policy'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP dataretention operations."""
        if ctx:
            await ctx.info("Executing dataretention operation: " + str(action) + "...")
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
