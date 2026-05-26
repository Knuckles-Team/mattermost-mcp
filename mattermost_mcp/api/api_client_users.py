"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def login(self, **kwargs) -> Any:
        """Login to Mattermost server

        Path: /api/v4/users/login
        Method: POST
        """
        url = "/api/v4/users/login"
        return self.request("POST", url, data=kwargs)

    def login_with_desktop_token(self, **kwargs) -> Any:
        """Login using desktop token

        Path: /api/v4/users/login/desktop_token
        Method: POST
        """
        url = "/api/v4/users/login/desktop_token"
        return self.request("POST", url, data=kwargs)

    def login_by_cws_token(self, **kwargs) -> Any:
        """Auto-Login to Mattermost server using CWS token

        Path: /api/v4/users/login/cws
        Method: POST
        """
        url = "/api/v4/users/login/cws"
        return self.request("POST", url, data=kwargs)

    def login_s_s_o_code_exchange(self, **kwargs) -> Any:
        """Exchange SSO login code for session tokens

        Path: /api/v4/users/login/sso/code-exchange
        Method: POST
        """
        url = "/api/v4/users/login/sso/code-exchange"
        return self.request("POST", url, data=kwargs)

    def login_intune(self, **kwargs) -> Any:
        """Login with Microsoft Intune MAM

        Path: /oauth/intune
        Method: POST
        """
        url = "/oauth/intune"
        return self.request("POST", url, data=kwargs)

    def logout(self, **kwargs) -> Any:
        """Logout from the Mattermost server

        Path: /api/v4/users/logout
        Method: POST
        """
        url = "/api/v4/users/logout"
        return self.request("POST", url, data=kwargs)

    def notify_admin(self, **kwargs) -> Any:
        """Save notify-admin intent

        Path: /api/v4/users/notify-admin
        Method: POST
        """
        url = "/api/v4/users/notify-admin"
        return self.request("POST", url, data=kwargs)

    def trigger_notify_admin_posts(self, **kwargs) -> Any:
        """Trigger notify-admin posts

        Path: /api/v4/users/trigger-notify-admin-posts
        Method: POST
        """
        url = "/api/v4/users/trigger-notify-admin-posts"
        return self.request("POST", url, data=kwargs)

    def get_users(self, **kwargs) -> Any:
        """Get users

        Path: /api/v4/users
        Method: GET
        """
        url = "/api/v4/users"
        return self.request("GET", url, params=kwargs)

    def create_user(self, **kwargs) -> Any:
        """Create a user

        Path: /api/v4/users
        Method: POST
        """
        url = "/api/v4/users"
        return self.request("POST", url, data=kwargs)

    def permanent_delete_all_users(self, **kwargs) -> Any:
        """Permanent delete all users

        Path: /api/v4/users
        Method: DELETE
        """
        url = "/api/v4/users"
        return self.request("DELETE", url, params=kwargs)

    def get_users_by_ids(self, **kwargs) -> Any:
        """Get users by ids

        Path: /api/v4/users/ids
        Method: POST
        """
        url = "/api/v4/users/ids"
        return self.request("POST", url, data=kwargs)

    def get_users_by_group_channel_ids(self, **kwargs) -> Any:
        """Get users by group channels ids

        Path: /api/v4/users/group_channels
        Method: POST
        """
        url = "/api/v4/users/group_channels"
        return self.request("POST", url, data=kwargs)

    def get_users_by_usernames(self, **kwargs) -> Any:
        """Get users by usernames

        Path: /api/v4/users/usernames
        Method: POST
        """
        url = "/api/v4/users/usernames"
        return self.request("POST", url, data=kwargs)

    def search_users(self, **kwargs) -> Any:
        """Search users

        Path: /api/v4/users/search
        Method: POST
        """
        url = "/api/v4/users/search"
        return self.request("POST", url, data=kwargs)

    def autocomplete_users(self, **kwargs) -> Any:
        """Autocomplete users

        Path: /api/v4/users/autocomplete
        Method: GET
        """
        url = "/api/v4/users/autocomplete"
        return self.request("GET", url, params=kwargs)

    def get_known_users(self, **kwargs) -> Any:
        """Get user IDs of known users

        Path: /api/v4/users/known
        Method: GET
        """
        url = "/api/v4/users/known"
        return self.request("GET", url, params=kwargs)

    def get_total_users_stats(self, **kwargs) -> Any:
        """Get total count of users in the system

        Path: /api/v4/users/stats
        Method: GET
        """
        url = "/api/v4/users/stats"
        return self.request("GET", url, params=kwargs)

    def get_total_users_stats_filtered(self, **kwargs) -> Any:
        """Get total count of users in the system matching the specified filters

        Path: /api/v4/users/stats/filtered
        Method: GET
        """
        url = "/api/v4/users/stats/filtered"
        return self.request("GET", url, params=kwargs)

    def get_user(self, user_id: str, **kwargs) -> Any:
        """Get a user

        Path: /api/v4/users/{user_id}
        Method: GET
        """
        url = f"/api/v4/users/{user_id}"
        return self.request("GET", url, params=kwargs)

    def update_user(self, user_id: str, **kwargs) -> Any:
        """Update a user

        Path: /api/v4/users/{user_id}
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}"
        return self.request("PUT", url, data=kwargs)

    def delete_user(self, user_id: str, **kwargs) -> Any:
        """Deactivate a user account.

        Path: /api/v4/users/{user_id}
        Method: DELETE
        """
        url = f"/api/v4/users/{user_id}"
        return self.request("DELETE", url, params=kwargs)

    def patch_user(self, user_id: str, **kwargs) -> Any:
        """Patch a user

        Path: /api/v4/users/{user_id}/patch
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/patch"
        return self.request("PUT", url, data=kwargs)

    def update_user_roles(self, user_id: str, **kwargs) -> Any:
        """Update a user's roles

        Path: /api/v4/users/{user_id}/roles
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/roles"
        return self.request("PUT", url, data=kwargs)

    def update_user_active(self, user_id: str, **kwargs) -> Any:
        """Activate or deactivate a user

        Path: /api/v4/users/{user_id}/active
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/active"
        return self.request("PUT", url, data=kwargs)

    def get_profile_image(self, user_id: str, **kwargs) -> Any:
        """Get user's profile image

        Path: /api/v4/users/{user_id}/image
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/image"
        return self.request("GET", url, params=kwargs)

    def set_profile_image(self, user_id: str, **kwargs) -> Any:
        """Set user's profile image

        Path: /api/v4/users/{user_id}/image
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/image"
        return self.request("POST", url, data=kwargs)

    def set_default_profile_image(self, user_id: str, **kwargs) -> Any:
        """Delete user's profile image

        Path: /api/v4/users/{user_id}/image
        Method: DELETE
        """
        url = f"/api/v4/users/{user_id}/image"
        return self.request("DELETE", url, params=kwargs)

    def get_default_profile_image(self, user_id: str, **kwargs) -> Any:
        """Return user's default (generated) profile image

        Path: /api/v4/users/{user_id}/image/default
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/image/default"
        return self.request("GET", url, params=kwargs)

    def get_user_by_username(self, username: str, **kwargs) -> Any:
        """Get a user by username

        Path: /api/v4/users/username/{username}
        Method: GET
        """
        url = f"/api/v4/users/username/{username}"
        return self.request("GET", url, params=kwargs)

    def get_user_by_auth_data(self, **kwargs) -> Any:
        """Get a user by auth data

        Path: /api/v4/users/auth_data
        Method: GET
        """
        url = "/api/v4/users/auth_data"
        return self.request("GET", url, params=kwargs)

    def reset_password(self, **kwargs) -> Any:
        """Reset password

        Path: /api/v4/users/password/reset
        Method: POST
        """
        url = "/api/v4/users/password/reset"
        return self.request("POST", url, data=kwargs)

    def update_user_mfa(self, user_id: str, **kwargs) -> Any:
        """Update a user's MFA

        Path: /api/v4/users/{user_id}/mfa
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/mfa"
        return self.request("PUT", url, data=kwargs)

    def generate_mfa_secret(self, user_id: str, **kwargs) -> Any:
        """Generate MFA secret

        Path: /api/v4/users/{user_id}/mfa/generate
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/mfa/generate"
        return self.request("POST", url, data=kwargs)

    def demote_user_to_guest(self, user_id: str, **kwargs) -> Any:
        """Demote a user to a guest

        Path: /api/v4/users/{user_id}/demote
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/demote"
        return self.request("POST", url, data=kwargs)

    def promote_guest_to_user(self, user_id: str, **kwargs) -> Any:
        """Promote a guest to user

        Path: /api/v4/users/{user_id}/promote
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/promote"
        return self.request("POST", url, data=kwargs)

    def convert_user_to_bot(self, user_id: str, **kwargs) -> Any:
        """Convert a user into a bot

        Path: /api/v4/users/{user_id}/convert_to_bot
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/convert_to_bot"
        return self.request("POST", url, data=kwargs)

    def update_user_password(self, user_id: str, **kwargs) -> Any:
        """Update a user's password

        Path: /api/v4/users/{user_id}/password
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/password"
        return self.request("PUT", url, data=kwargs)

    def send_password_reset_email(self, **kwargs) -> Any:
        """Send password reset email

        Path: /api/v4/users/password/reset/send
        Method: POST
        """
        url = "/api/v4/users/password/reset/send"
        return self.request("POST", url, data=kwargs)

    def get_user_by_email(self, email: str, **kwargs) -> Any:
        """Get a user by email

        Path: /api/v4/users/email/{email}
        Method: GET
        """
        url = f"/api/v4/users/email/{email}"
        return self.request("GET", url, params=kwargs)

    def get_sessions(self, user_id: str, **kwargs) -> Any:
        """Get user's sessions

        Path: /api/v4/users/{user_id}/sessions
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/sessions"
        return self.request("GET", url, params=kwargs)

    def revoke_session(self, user_id: str, **kwargs) -> Any:
        """Revoke a user session

        Path: /api/v4/users/{user_id}/sessions/revoke
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/sessions/revoke"
        return self.request("POST", url, data=kwargs)

    def revoke_all_sessions(self, user_id: str, **kwargs) -> Any:
        """Revoke all active sessions for a user

        Path: /api/v4/users/{user_id}/sessions/revoke/all
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/sessions/revoke/all"
        return self.request("POST", url, data=kwargs)

    def attach_device_extra_props(self, **kwargs) -> Any:
        """Attach mobile device and extra props to the session object

        Path: /api/v4/users/sessions/device
        Method: PUT
        """
        url = "/api/v4/users/sessions/device"
        return self.request("PUT", url, data=kwargs)

    def get_user_audits(self, user_id: str, **kwargs) -> Any:
        """Get user's audits

        Path: /api/v4/users/{user_id}/audits
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/audits"
        return self.request("GET", url, params=kwargs)

    def verify_user_email_without_token(self, user_id: str, **kwargs) -> Any:
        """Verify user email by ID

        Path: /api/v4/users/{user_id}/email/verify/member
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/email/verify/member"
        return self.request("POST", url, data=kwargs)

    def verify_user_email(self, **kwargs) -> Any:
        """Verify user email

        Path: /api/v4/users/email/verify
        Method: POST
        """
        url = "/api/v4/users/email/verify"
        return self.request("POST", url, data=kwargs)

    def send_verification_email(self, **kwargs) -> Any:
        """Send verification email

        Path: /api/v4/users/email/verify/send
        Method: POST
        """
        url = "/api/v4/users/email/verify/send"
        return self.request("POST", url, data=kwargs)

    def switch_account_type(self, **kwargs) -> Any:
        """Switch login method

        Path: /api/v4/users/login/switch
        Method: POST
        """
        url = "/api/v4/users/login/switch"
        return self.request("POST", url, data=kwargs)

    def get_login_type(self, **kwargs) -> Any:
        """Get login authentication type

        Path: /api/v4/users/login/type
        Method: POST
        """
        url = "/api/v4/users/login/type"
        return self.request("POST", url, data=kwargs)

    def get_user_access_tokens_for_user(self, user_id: str, **kwargs) -> Any:
        """Get user access tokens

        Path: /api/v4/users/{user_id}/tokens
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/tokens"
        return self.request("GET", url, params=kwargs)

    def create_user_access_token(self, user_id: str, **kwargs) -> Any:
        """Create a user access token

        Path: /api/v4/users/{user_id}/tokens
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/tokens"
        return self.request("POST", url, data=kwargs)

    def get_user_access_tokens(self, **kwargs) -> Any:
        """Get user access tokens

        Path: /api/v4/users/tokens
        Method: GET
        """
        url = "/api/v4/users/tokens"
        return self.request("GET", url, params=kwargs)

    def revoke_user_access_token(self, **kwargs) -> Any:
        """Revoke a user access token

        Path: /api/v4/users/tokens/revoke
        Method: POST
        """
        url = "/api/v4/users/tokens/revoke"
        return self.request("POST", url, data=kwargs)

    def get_user_access_token(self, token_id: str, **kwargs) -> Any:
        """Get a user access token

        Path: /api/v4/users/tokens/{token_id}
        Method: GET
        """
        url = f"/api/v4/users/tokens/{token_id}"
        return self.request("GET", url, params=kwargs)

    def disable_user_access_token(self, **kwargs) -> Any:
        """Disable personal access token

        Path: /api/v4/users/tokens/disable
        Method: POST
        """
        url = "/api/v4/users/tokens/disable"
        return self.request("POST", url, data=kwargs)

    def enable_user_access_token(self, **kwargs) -> Any:
        """Enable personal access token

        Path: /api/v4/users/tokens/enable
        Method: POST
        """
        url = "/api/v4/users/tokens/enable"
        return self.request("POST", url, data=kwargs)

    def search_user_access_tokens(self, **kwargs) -> Any:
        """Search tokens

        Path: /api/v4/users/tokens/search
        Method: POST
        """
        url = "/api/v4/users/tokens/search"
        return self.request("POST", url, data=kwargs)

    def update_user_auth(self, user_id: str, **kwargs) -> Any:
        """Update a user's authentication method

        Path: /api/v4/users/{user_id}/auth
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/auth"
        return self.request("PUT", url, data=kwargs)

    def get_user_terms_of_service(self, user_id: str, **kwargs) -> Any:
        """Fetches user's latest terms of service action if the latest action was for acceptance.

        Path: /api/v4/users/{user_id}/terms_of_service
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/terms_of_service"
        return self.request("GET", url, params=kwargs)

    def register_terms_of_service_action(self, user_id: str, **kwargs) -> Any:
        """Records user action when they accept or decline custom terms of service

        Path: /api/v4/users/{user_id}/terms_of_service
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/terms_of_service"
        return self.request("POST", url, data=kwargs)

    def revoke_sessions_from_all_users(self, **kwargs) -> Any:
        """Revoke all sessions from all users.

        Path: /api/v4/users/sessions/revoke/all
        Method: POST
        """
        url = "/api/v4/users/sessions/revoke/all"
        return self.request("POST", url, data=kwargs)

    def publish_user_typing(self, user_id: str, **kwargs) -> Any:
        """Publish a user typing websocket event.

        Path: /api/v4/users/{user_id}/typing
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/typing"
        return self.request("POST", url, data=kwargs)

    def get_uploads_for_user(self, user_id: str, **kwargs) -> Any:
        """Get uploads for a user

        Path: /api/v4/users/{user_id}/uploads
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/uploads"
        return self.request("GET", url, params=kwargs)

    def get_channel_members_with_team_data_for_user(
        self, user_id: str, **kwargs
    ) -> Any:
        """Get all channel members from all teams for a user

        Path: /api/v4/users/{user_id}/channel_members
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/channel_members"
        return self.request("GET", url, params=kwargs)

    def migrate_auth_to_ldap(self, **kwargs) -> Any:
        """Migrate user accounts authentication type to LDAP.

        Path: /api/v4/users/migrate_auth/ldap
        Method: POST
        """
        url = "/api/v4/users/migrate_auth/ldap"
        return self.request("POST", url, data=kwargs)

    def migrate_auth_to_saml(self, **kwargs) -> Any:
        """Migrate user accounts authentication type to SAML.

        Path: /api/v4/users/migrate_auth/saml
        Method: POST
        """
        url = "/api/v4/users/migrate_auth/saml"
        return self.request("POST", url, data=kwargs)

    def get_user_threads(self, user_id: str, team_id: str, **kwargs) -> Any:
        """Get all threads that user is following

        Path: /api/v4/users/{user_id}/teams/{team_id}/threads
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/threads"
        return self.request("GET", url, params=kwargs)

    def mark_all_team_channels_read(self, user_id: str, team_id: str, **kwargs) -> Any:
        """Mark all channels and threads in a team as read

        Path: /api/v4/users/{user_id}/teams/{team_id}/read
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/read"
        return self.request("PUT", url, data=kwargs)

    def update_threads_read_for_user(self, user_id: str, team_id: str, **kwargs) -> Any:
        """Mark all threads that user is following as read

        Path: /api/v4/users/{user_id}/teams/{team_id}/threads/read
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/threads/read"
        return self.request("PUT", url, data=kwargs)

    def update_thread_read_for_user(
        self, user_id: str, team_id: str, thread_id: str, timestamp: str, **kwargs
    ) -> Any:
        """Mark a thread that user is following read state to the timestamp

        Path: /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/read/{timestamp}
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/read/{timestamp}"
        return self.request("PUT", url, data=kwargs)

    def set_thread_unread_by_post_id(
        self, user_id: str, team_id: str, thread_id: str, post_id: str, **kwargs
    ) -> Any:
        """Mark a thread that user is following as unread based on a post id

        Path: /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/set_unread/{post_id}
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/set_unread/{post_id}"
        return self.request("POST", url, data=kwargs)

    def start_following_thread(
        self, user_id: str, team_id: str, thread_id: str, **kwargs
    ) -> Any:
        """Start following a thread

        Path: /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/following
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/following"
        return self.request("PUT", url, data=kwargs)

    def stop_following_thread(
        self, user_id: str, team_id: str, thread_id: str, **kwargs
    ) -> Any:
        """Stop following a thread

        Path: /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/following
        Method: DELETE
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/following"
        return self.request("DELETE", url, params=kwargs)

    def get_user_thread(
        self, user_id: str, team_id: str, thread_id: str, **kwargs
    ) -> Any:
        """Get a thread followed by the user

        Path: /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}"
        return self.request("GET", url, params=kwargs)

    def upsert_draft(self, **kwargs) -> Any:
        """Upsert synced draft

        Path: /api/v4/drafts
        Method: POST
        """
        url = "/api/v4/drafts"
        return self.request("POST", url, data=kwargs)

    def get_drafts(self, user_id: str, team_id: str, **kwargs) -> Any:
        """Get synced drafts for a team

        Path: /api/v4/users/{user_id}/teams/{team_id}/drafts
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/drafts"
        return self.request("GET", url, params=kwargs)

    def delete_draft(self, user_id: str, channel_id: str, **kwargs) -> Any:
        """Delete synced draft

        Path: /api/v4/users/{user_id}/channels/{channel_id}/drafts
        Method: DELETE
        """
        url = f"/api/v4/users/{user_id}/channels/{channel_id}/drafts"
        return self.request("DELETE", url, params=kwargs)

    def delete_draft_for_thread(
        self, user_id: str, channel_id: str, thread_id: str, **kwargs
    ) -> Any:
        """Delete synced thread draft

        Path: /api/v4/users/{user_id}/channels/{channel_id}/drafts/{thread_id}
        Method: DELETE
        """
        url = f"/api/v4/users/{user_id}/channels/{channel_id}/drafts/{thread_id}"
        return self.request("DELETE", url, params=kwargs)

    def get_team_policies_for_user(self, user_id: str, **kwargs) -> Any:
        """Get the policies which are applied to a user's teams

        Path: /api/v4/users/{user_id}/data_retention/team_policies
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/data_retention/team_policies"
        return self.request("GET", url, params=kwargs)

    def get_channel_policies_for_user(self, user_id: str, **kwargs) -> Any:
        """Get the policies which are applied to a user's channels

        Path: /api/v4/users/{user_id}/data_retention/channel_policies
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/data_retention/channel_policies"
        return self.request("GET", url, params=kwargs)

    def get_users_with_invalid_emails(self, **kwargs) -> Any:
        """Get users with invalid emails

        Path: /api/v4/users/invalid_emails
        Method: GET
        """
        url = "/api/v4/users/invalid_emails"
        return self.request("GET", url, params=kwargs)

    def reset_password_failed_attempts(self, user_id: str, **kwargs) -> Any:
        """Reset the failed password attempts for a user

        Path: /api/v4/users/{user_id}/reset_failed_attempts
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/reset_failed_attempts"
        return self.request("POST", url, data=kwargs)
