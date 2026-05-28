"""
This file was automatically generated. Do not edit manually.
"""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_saml_tools(mcp: FastMCP):
    """Register Mattermost MCP saml tools."""

    @mcp.tool(tags=["saml"])
    async def mattermost_mcp_saml(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_saml_metadata', 'get_saml_metadata_from_idp', 'upload_saml_idp_certificate', 'delete_saml_idp_certificate', 'upload_saml_public_certificate', 'delete_saml_public_certificate', 'upload_saml_private_certificate', 'delete_saml_private_certificate', 'get_saml_certificate_status', 'reset_saml_auth_data_to_email'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP saml operations."""
        if ctx:
            await ctx.info("Executing saml operation: " + str(action) + "...")
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
