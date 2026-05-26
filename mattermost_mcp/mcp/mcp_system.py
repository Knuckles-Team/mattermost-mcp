"""
This file was automatically generated. Do not edit manually.
"""
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_system_tools(mcp: FastMCP):
    """Register Mattermost MCP system tools."""

    @mcp.tool(tags=["system"])
    async def mattermost_mcp_system(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_supported_timezone', 'get_ping', 'connect_web_socket', 'manual_test', 'get_notices', 'mark_notices_viewed', 'get_onboarding_complete', 'complete_onboarding', 'get_a_i_bridge_test_helper', 'set_a_i_bridge_test_helper', 'delete_a_i_bridge_test_helper', 'database_recycle', 'test_email', 'test_notification', 'test_site_u_r_l', 'test_s3_connection', 'get_config', 'update_config', 'reload_config', 'migrate_config', 'get_client_config', 'get_environment_config', 'patch_config', 'upload_license_file', 'remove_license_file', 'get_client_license', 'get_license_load_metric', 'request_trial_license', 'get_prev_trial_license', 'get_audits', 'invalidate_caches', 'get_logs', 'post_log', 'query_logs', 'get_analytics_old', 'get_latest_version', 'get_applied_schema_migrations', 'get_server_busy_expires', 'set_server_busy', 'clear_server_busy', 'acknowledge_notification', 'get_redirect_location', 'get_image_by_url', 'upgrade_to_enterprise', 'upgrade_to_enterprise_status', 'is_allowed_to_upgrade_to_enterprise', 'restart_server', 'check_integrity', 'generate_support_packet'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP system operations."""
        if ctx:
            await ctx.info("Executing system operation: " + str(action) + "...")
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
