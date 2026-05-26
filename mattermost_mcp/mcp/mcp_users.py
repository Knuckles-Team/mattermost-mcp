"""
This file was automatically generated. Do not edit manually.
"""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_users_tools(mcp: FastMCP):
    """Register Mattermost MCP users tools."""

    @mcp.tool(tags=["users"])
    async def mattermost_mcp_users(
        action: str = Field(
            description="Action to perform. Must be one of: 'login', 'login_with_desktop_token', 'login_by_cws_token', 'login_s_s_o_code_exchange', 'login_intune', 'logout', 'notify_admin', 'trigger_notify_admin_posts', 'get_users', 'create_user', 'permanent_delete_all_users', 'get_users_by_ids', 'get_users_by_group_channel_ids', 'get_users_by_usernames', 'search_users', 'autocomplete_users', 'get_known_users', 'get_total_users_stats', 'get_total_users_stats_filtered', 'get_user', 'update_user', 'delete_user', 'patch_user', 'update_user_roles', 'update_user_active', 'get_profile_image', 'set_profile_image', 'set_default_profile_image', 'get_default_profile_image', 'get_user_by_username', 'get_user_by_auth_data', 'reset_password', 'update_user_mfa', 'generate_mfa_secret', 'demote_user_to_guest', 'promote_guest_to_user', 'convert_user_to_bot', 'update_user_password', 'send_password_reset_email', 'get_user_by_email', 'get_sessions', 'revoke_session', 'revoke_all_sessions', 'attach_device_extra_props', 'get_user_audits', 'verify_user_email_without_token', 'verify_user_email', 'send_verification_email', 'switch_account_type', 'get_login_type', 'get_user_access_tokens_for_user', 'create_user_access_token', 'get_user_access_tokens', 'revoke_user_access_token', 'get_user_access_token', 'disable_user_access_token', 'enable_user_access_token', 'search_user_access_tokens', 'update_user_auth', 'get_user_terms_of_service', 'register_terms_of_service_action', 'revoke_sessions_from_all_users', 'publish_user_typing', 'get_uploads_for_user', 'get_channel_members_with_team_data_for_user', 'migrate_auth_to_ldap', 'migrate_auth_to_saml', 'get_user_threads', 'mark_all_team_channels_read', 'update_threads_read_for_user', 'update_thread_read_for_user', 'set_thread_unread_by_post_id', 'start_following_thread', 'stop_following_thread', 'get_user_thread', 'upsert_draft', 'get_drafts', 'delete_draft', 'delete_draft_for_thread', 'get_team_policies_for_user', 'get_channel_policies_for_user', 'get_users_with_invalid_emails', 'reset_password_failed_attempts'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP users operations."""
        if ctx:
            await ctx.info("Executing users operation: " + str(action) + "...")
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
