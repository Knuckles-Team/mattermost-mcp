---
name: mattermost-api-users-and-sessions
skill_type: skill
description: >-
  Mattermost users, sessions, tokens and roles API. User records, access tokens, sessions, preferences, status, bots, roles, authentication and multi-factor settings. Do NOT use for the task skills that already cover a workflow (mattermost-channel-messaging, mattermost-team-administration, mattermost-kg-ingestion).
license: MIT
tags: [mattermost, api-reference]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Mattermost users, sessions, tokens and roles API

User records, access tokens, sessions, preferences, status, bots, roles, authentication and multi-factor settings.

Every operation is its own typed tool; arguments follow the upstream API (path parameters are required,
filters are optional arguments). Read first (get, list, search), change second, and obtain approval before
any delete, disable, revoke or reset.

| Tool | Summary |
|---|---|
| `mattermost_assign_bot` | Assign a bot to a user |
| `mattermost_autocomplete_users` | Autocomplete users |
| `mattermost_convert_bot_to_user` | Convert a bot into a user |
| `mattermost_convert_user_to_bot` | Convert a user into a bot |
| `mattermost_create_bot` | Create a bot |
| `mattermost_create_o_auth_app` | Register OAuth app |
| `mattermost_create_outgoing_o_auth_connection` | Create a connection |
| `mattermost_create_terms_of_service` | Creates a new terms of service |
| `mattermost_create_user` | Create a user |
| `mattermost_create_user_access_token` | Create a user access token |
| `mattermost_delete_o_auth_app` | Delete an OAuth app |
| `mattermost_delete_outgoing_o_auth_connection` | Delete a connection |
| `mattermost_delete_preferences` | Delete user's preferences |
| `mattermost_delete_user` | Deactivate a user account. |
| `mattermost_demote_user_to_guest` | Demote a user to a guest |
| `mattermost_disable_bot` | Disable a bot |
| `mattermost_disable_user_access_token` | Disable personal access token |
| `mattermost_enable_bot` | Enable a bot |
| `mattermost_enable_user_access_token` | Enable personal access token |
| `mattermost_generate_mfa_secret` | Generate MFA secret |
| `mattermost_get_agents_status` | Get agents bridge status |
| `mattermost_get_all_roles` | Get a list of all the roles |
| `mattermost_get_authorization_server_metadata` | Get OAuth 2.0 Authorization Server Metadata |
| `mattermost_get_authorized_o_auth_apps_for_user` | Get authorized OAuth apps |
| `mattermost_get_bot` | Get a bot |
| `mattermost_get_bots` | Get bots |
| `mattermost_get_cluster_status` | Get cluster status |
| `mattermost_get_known_users` | Get user IDs of known users |
| `mattermost_get_login_type` | Get login authentication type |
| `mattermost_get_non_compliant_user_access_token_count` | Count non-compliant personal access tokens |
| `mattermost_get_o_auth_app` | Get an OAuth app |
| `mattermost_get_o_auth_app_info` | Get info on an OAuth app |
| `mattermost_get_o_auth_apps` | Get OAuth apps |
| `mattermost_get_outgoing_o_auth_connection` | Get a connection |
| `mattermost_get_plugin_statuses` | Get plugins status |
| `mattermost_get_preferences` | Get the user's preferences |
| `mattermost_get_preferences_by_category` | List a user's preferences by category |
| `mattermost_get_preferences_by_category_by_name` | Get a specific user preference |
| `mattermost_get_role` | Get a role |
| `mattermost_get_role_by_name` | Get a role |
| `mattermost_get_roles_by_names` | Get a list of roles by name |
| `mattermost_get_saml_certificate_status` | Get certificate status |
| `mattermost_get_session_attributes_manifest` | Get the session attributes manifest |
| `mattermost_get_sessions` | Get user's sessions |
| `mattermost_get_terms_of_service` | Get latest terms of service |
| `mattermost_get_total_users_stats` | Get total count of users in the system |
| `mattermost_get_total_users_stats_filtered` | Get total count of users in the system matching the specified filters |
| `mattermost_get_uploads_for_user` | Get uploads for a user |
| `mattermost_get_user` | Get a user |
| `mattermost_get_user_access_token` | Get a user access token |
| `mattermost_get_user_access_tokens` | Get user access tokens |
| `mattermost_get_user_access_tokens_for_user` | Get user access tokens |
| `mattermost_get_user_by_auth_data` | Get a user by auth data |
| `mattermost_get_user_by_email` | Get a user by email |
| `mattermost_get_user_by_username` | Get a user by username |
| `mattermost_get_user_status` | Get user status |
| `mattermost_get_user_terms_of_service` | Fetches user's latest terms of service action if the latest action was for acceptance. |
| `mattermost_get_users` | Get users |
| `mattermost_get_users_by_ids` | Get users by ids |
| `mattermost_get_users_by_usernames` | Get users by usernames |
| `mattermost_get_users_statuses_by_ids` | Get user statuses by id |
| `mattermost_get_users_with_invalid_emails` | Get users with invalid emails |
| `mattermost_ingest_users` | Ingest Mattermost users as shared :Person / :Bot nodes. |
| `mattermost_list_outgoing_o_auth_connections` | List all connections |
| `mattermost_login` | Login to Mattermost server |
| `mattermost_login_by_cws_token` | Auto-Login to Mattermost server using CWS token |
| `mattermost_login_intune` | Login with Microsoft Intune MAM |
| `mattermost_login_s_s_o_code_exchange` | Exchange SSO login code for session tokens |
| `mattermost_login_with_desktop_token` | Login using desktop token |
| `mattermost_migrate_auth_to_ldap` | Migrate user accounts authentication type to LDAP. |
| `mattermost_migrate_auth_to_saml` | Migrate user accounts authentication type to SAML. |
| `mattermost_patch_bot` | Patch a bot |
| `mattermost_patch_c_p_a_values_for_user` | Update custom profile attribute values for a user |
| `mattermost_patch_role` | Patch a role |
| `mattermost_patch_user` | Patch a user |
| `mattermost_permanent_delete_all_users` | Permanent delete all users |
| `mattermost_promote_guest_to_user` | Promote a guest to user |
| `mattermost_publish_user_typing` | Publish a user typing websocket event. |
| `mattermost_regen_command_token` | Generate a new token |
| `mattermost_regen_outgoing_hook_token` | Regenerate the token for the outgoing webhook. |
| `mattermost_regenerate_o_auth_app_secret` | Regenerate OAuth app secret |
| `mattermost_register_o_auth_client` | Register OAuth client using Dynamic Client Registration |
| `mattermost_register_terms_of_service_action` | Records user action when they accept or decline custom terms of service |
| `mattermost_remove_recent_custom_status` | Delete user's recent custom status |
| `mattermost_reset_password` | Reset password |
| `mattermost_reset_password_failed_attempts` | Reset the failed password attempts for a user |
| `mattermost_reset_saml_auth_data_to_email` | Reset AuthData to Email |
| `mattermost_revoke_all_sessions` | Revoke all active sessions for a user |
| `mattermost_revoke_non_compliant_user_access_tokens` | Revoke non-compliant personal access tokens |
| `mattermost_revoke_session` | Revoke a user session |
| `mattermost_revoke_sessions_from_all_users` | Revoke all sessions from all users. |
| `mattermost_revoke_user_access_token` | Revoke a user access token |
| `mattermost_rotate_user_access_token` | Rotate a personal access token |
| `mattermost_search_user_access_tokens` | Search tokens |
| `mattermost_search_users` | Search users |
| `mattermost_send_password_reset_email` | Send password reset email |
| `mattermost_send_verification_email` | Send verification email |
| `mattermost_test_email` | Send a test email |
| `mattermost_unset_user_custom_status` | Unsets user custom status |
| `mattermost_update_job_status` | Update the status of a job |
| `mattermost_update_o_auth_app` | Update an OAuth app |
| `mattermost_update_outgoing_o_auth_connection` | Update a connection |
| `mattermost_update_preferences` | Save the user's preferences |
| `mattermost_update_user` | Update a user |
| `mattermost_update_user_active` | Activate or deactivate a user |
| `mattermost_update_user_auth` | Update a user's authentication method |
| `mattermost_update_user_custom_status` | Update user custom status |
| `mattermost_update_user_mfa` | Update a user's MFA |
| `mattermost_update_user_password` | Update a user's password |
| `mattermost_update_user_roles` | Update a user's roles |
| `mattermost_update_user_status` | Update user status |
| `mattermost_upgrade_to_enterprise_status` | Get the current status for the inplace upgrade from Team Edition to Enterprise Edition |
| `mattermost_validate_business_email` | Validate business email |
| `mattermost_validate_outgoing_o_auth_connection` | Validate a connection configuration |
| `mattermost_validate_workspace_business_email` | Validate workspace business email |
| `mattermost_verify_user_email` | Verify user email |
| `mattermost_verify_user_email_without_token` | Verify user email by ID |
