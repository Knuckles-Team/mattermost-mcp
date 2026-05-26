"""
This file was automatically generated. Do not edit manually.
"""
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_ldap_tools(mcp: FastMCP):
    """Register Mattermost MCP ldap tools."""

    @mcp.tool(tags=["ldap"])
    async def mattermost_mcp_ldap(
        action: str = Field(
            description="Action to perform. Must be one of: 'sync_ldap', 'test_ldap', 'test_ldap_connection', 'test_ldap_diagnostics', 'get_ldap_groups', 'link_ldap_group', 'unlink_ldap_group', 'migrate_id_ldap', 'upload_ldap_public_certificate', 'delete_ldap_public_certificate', 'upload_ldap_private_certificate', 'delete_ldap_private_certificate', 'add_user_to_group_syncables'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP ldap operations."""
        if ctx:
            await ctx.info("Executing ldap operation: " + str(action) + "...")
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
