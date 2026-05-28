"""
This file was automatically generated. Do not edit manually.
"""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_cloud_tools(mcp: FastMCP):
    """Register Mattermost MCP cloud tools."""

    @mcp.tool(tags=["cloud"])
    async def mattermost_mcp_cloud(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_cloud_limits', 'get_cloud_products', 'get_cloud_customer', 'update_cloud_customer', 'update_cloud_customer_address', 'validate_business_email', 'validate_workspace_business_email', 'get_subscription', 'get_endpoint_for_installation_information', 'get_invoices_for_subscription', 'get_invoice_for_subscription_as_pdf', 'hosted_customer_signup_available', 'check_c_w_s_connection', 'post_endpoint_for_cws_webhooks', 'get_preview_modal_data'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP cloud operations."""
        if ctx:
            await ctx.info("Executing cloud operation: " + str(action) + "...")
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
