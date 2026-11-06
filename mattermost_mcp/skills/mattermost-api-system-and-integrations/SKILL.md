---
name: mattermost-api-system-and-integrations
skill_type: skill
description: >-
  Mattermost system, plugins, jobs and integrations API. Server configuration, plugins, jobs, cluster, licence, LDAP and SAML, commands, webhooks, remote clusters, logs and diagnostics. Do NOT use for the task skills that already cover a workflow (mattermost-channel-messaging, mattermost-team-administration, mattermost-kg-ingestion).
license: MIT
tags: [mattermost, api-reference]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Mattermost system, plugins, jobs and integrations API

Server configuration, plugins, jobs, cluster, licence, LDAP and SAML, commands, webhooks, remote clusters, logs and diagnostics.

Every operation is its own typed tool; arguments follow the upstream API (path parameters are required,
filters are optional arguments). Read first (get, list, search), change second, and obtain approval before
any delete, disable, revoke or reset.

| Tool | Summary |
|---|---|
| `mattermost_apply_i_p_filters` | Get all IP filters |
| `mattermost_attach_device_extra_props` | Attach mobile device and extra props to the session object |
| `mattermost_cancel_job` | Cancel a job. |
| `mattermost_check_c_w_s_connection` | Check CWS connection |
| `mattermost_check_integrity` | Perform a database integrity check |
| `mattermost_clear_server_busy` | Clears the server busy (high load) flag |
| `mattermost_complete_onboarding` | Complete first admin onboarding |
| `mattermost_connect_web_socket` | Open a WebSocket connection |
| `mattermost_create_board` | Create a board channel |
| `mattermost_create_c_p_a_field` | Create a Custom Profile Attribute field |
| `mattermost_create_command` | Create a command |
| `mattermost_create_incoming_webhook` | Create an incoming webhook |
| `mattermost_create_job` | Create a new job. |
| `mattermost_create_outgoing_webhook` | Create an outgoing webhook |
| `mattermost_create_property_field` | Create a property field |
| `mattermost_create_remote_cluster` | Create a new remote cluster. |
| `mattermost_create_upload` | Create an upload |
| `mattermost_database_recycle` | Recycle database connections |
| `mattermost_delete_a_i_bridge_test_helper` | Reset AI bridge E2E test helper |
| `mattermost_delete_c_p_a_field` | Delete a Custom Profile Attribute field |
| `mattermost_delete_command` | Delete a command |
| `mattermost_delete_incoming_webhook` | Delete an incoming webhook |
| `mattermost_delete_ldap_private_certificate` | Remove private key |
| `mattermost_delete_ldap_public_certificate` | Remove public certificate |
| `mattermost_delete_outgoing_webhook` | Delete an outgoing webhook |
| `mattermost_delete_property_field` | Delete a property field |
| `mattermost_delete_remote_cluster` | Delete a remote cluster. |
| `mattermost_delete_saml_idp_certificate` | Remove IDP certificate |
| `mattermost_delete_saml_private_certificate` | Remove private key |
| `mattermost_delete_saml_public_certificate` | Remove public certificate |
| `mattermost_detach_plugin` | Detach a reattached plugin process |
| `mattermost_disable_plugin` | Disable plugin |
| `mattermost_download_job` | Download the results of a job. |
| `mattermost_download_system_logs` | Download system logs |
| `mattermost_enable_plugin` | Enable plugin |
| `mattermost_execute_command` | Execute a command |
| `mattermost_execute_dialog_action` | Execute a dialog action button |
| `mattermost_generate_support_packet` | Download a zip file which contains helpful and useful information for troubleshooting your mattermost instance. |
| `mattermost_get_a_i_bridge_test_helper` | Get AI bridge E2E test helper state |
| `mattermost_get_agents` | Get available agents |
| `mattermost_get_analytics_old` | Get analytics |
| `mattermost_get_applied_schema_migrations` | Get applied database schema migrations |
| `mattermost_get_c_e_l_visual_a_s_t` | Get the visual AST for a CEL expression |
| `mattermost_get_client_config` | Get client configuration |
| `mattermost_get_client_license` | Get client license |
| `mattermost_get_cloud_customer` | Get cloud customer |
| `mattermost_get_cloud_limits` | Get cloud workspace limits |
| `mattermost_get_cloud_products` | Get cloud products |
| `mattermost_get_command_by_id` | Get a command |
| `mattermost_get_config` | Get configuration |
| `mattermost_get_endpoint_for_installation_information` | GET endpoint for Installation information |
| `mattermost_get_environment_config` | Get configuration made through environment variables |
| `mattermost_get_i_p_filters` | Get all IP filters |
| `mattermost_get_incoming_webhook` | Get an incoming webhook |
| `mattermost_get_incoming_webhooks` | List incoming webhooks |
| `mattermost_get_invoice_for_subscription_as_pdf` | Get cloud invoice PDF |
| `mattermost_get_invoices_for_subscription` | Get cloud subscription invoices |
| `mattermost_get_job` | Get a job. |
| `mattermost_get_jobs` | Get the jobs. |
| `mattermost_get_jobs_by_type` | Get the jobs of the given type. |
| `mattermost_get_l_l_m_services` | Get available LLM services |
| `mattermost_get_latest_version` | Get latest public server release information |
| `mattermost_get_license_load_metric` | Get license load metric |
| `mattermost_get_logs` | Get logs |
| `mattermost_get_managed_categories` | Get managed category mappings |
| `mattermost_get_marketplace_plugins` | Gets all the marketplace plugins |
| `mattermost_get_marketplace_visited_by_admin` | Get if the Plugin Marketplace has been visited by at least an admin. |
| `mattermost_get_notices` | Get notices for logged in user in specified team |
| `mattermost_get_onboarding_complete` | Get first admin onboarding completion status |
| `mattermost_get_outgoing_webhook` | Get an outgoing webhook |
| `mattermost_get_outgoing_webhooks` | List outgoing webhooks |
| `mattermost_get_ping` | Check system health |
| `mattermost_get_plugins` | Get plugins |
| `mattermost_get_prev_trial_license` | Get last trial license used |
| `mattermost_get_preview_modal_data` | Get cloud preview modal data |
| `mattermost_get_property_fields` | Get property fields |
| `mattermost_get_property_values` | Get property values for a target |
| `mattermost_get_remote_cluster` | Get a remote cluster. |
| `mattermost_get_remote_cluster_info` | Get remote cluster info by ID for user. |
| `mattermost_get_remote_clusters` | Get a list of remote clusters. |
| `mattermost_get_saml_metadata` | Get metadata |
| `mattermost_get_saml_metadata_from_idp` | Get metadata from Identity Provider |
| `mattermost_get_server_busy_expires` | Get server busy expiry time. |
| `mattermost_get_server_limits` | Gets the server limits for the server |
| `mattermost_get_storage_usage` | Get the total file storage usage for the instance in bytes. |
| `mattermost_get_subscription` | Get cloud subscription |
| `mattermost_get_supported_timezone` | Retrieve a list of supported timezones |
| `mattermost_get_system_property_values` | Get property values for the system |
| `mattermost_get_upload` | Get an upload session |
| `mattermost_get_webapp_plugins` | Get webapp plugins |
| `mattermost_hosted_customer_signup_available` | Check hosted signup availability |
| `mattermost_install_marketplace_plugin` | Installs a marketplace plugin |
| `mattermost_install_plugin_from_url` | Install plugin from url |
| `mattermost_invalidate_caches` | Invalidate all the caches |
| `mattermost_is_allowed_to_upgrade_to_enterprise` | Check if the user is allowed to upgrade to Enterprise Edition |
| `mattermost_list_all_c_p_a_fields` | List all the Custom Profile Attributes fields |
| `mattermost_list_autocomplete_commands` | List autocomplete commands |
| `mattermost_list_c_p_a_values` | List Custom Profile Attribute values |
| `mattermost_list_command_autocomplete_suggestions` | List commands' autocomplete data |
| `mattermost_list_commands` | List commands for a team |
| `mattermost_logout` | Logout from the Mattermost server |
| `mattermost_lookup_interactive_dialog` | Lookup dialog elements |
| `mattermost_manual_test` | Run manual testing helpers |
| `mattermost_mark_notices_viewed` | Update notices as 'viewed' |
| `mattermost_migrate_config` | Migrate config storage |
| `mattermost_migrate_id_ldap` | Migrate Id LDAP |
| `mattermost_move_command` | Move a command |
| `mattermost_my_i_p` | Get all IP filters |
| `mattermost_notify_admin` | Save notify-admin intent |
| `mattermost_open_interactive_dialog` | Open a dialog |
| `mattermost_patch_c_p_a_field` | Patch a Custom Profile Attribute field |
| `mattermost_patch_c_p_a_values` | Patch Custom Profile Attribute values |
| `mattermost_patch_config` | Patch configuration |
| `mattermost_patch_remote_cluster` | Patch a remote cluster. |
| `mattermost_purge_elasticsearch_indexes` | Purge all Elasticsearch indexes |
| `mattermost_query_logs` | Query server logs with filters |
| `mattermost_reattach_plugin` | Reattach a plugin process |
| `mattermost_reload_config` | Reload configuration |
| `mattermost_remote_cluster_accept_message` | Receive a remote cluster message. |
| `mattermost_remote_cluster_ping` | Receive a ping from a remote cluster. |
| `mattermost_remove_plugin` | Remove plugin |
| `mattermost_request_trial_license` | Request and install a trial license for your server |
| `mattermost_restart_server` | Restart the system after an upgrade from Team Edition to Enterprise Edition |
| `mattermost_rewrite_message` | Rewrite a message using AI |
| `mattermost_search_property_fields` | Search property fields across multiple object types |
| `mattermost_set_a_i_bridge_test_helper` | Configure AI bridge E2E test helper |
| `mattermost_set_server_busy` | Set the server busy (high load) flag |
| `mattermost_submit_interactive_dialog` | Submit a dialog |
| `mattermost_switch_account_type` | Switch login method |
| `mattermost_sync_ldap` | Sync with LDAP |
| `mattermost_test_elasticsearch` | Test Elasticsearch configuration |
| `mattermost_test_ldap` | Test LDAP configuration |
| `mattermost_test_ldap_connection` | Test LDAP connection with specific settings |
| `mattermost_test_ldap_diagnostics` | Test LDAP diagnostics with specific settings |
| `mattermost_test_s3_connection` | Test AWS S3 connection |
| `mattermost_test_site_u_r_l` | Checks the validity of a Site URL |
| `mattermost_update_cloud_customer` | Update cloud customer |
| `mattermost_update_cloud_customer_address` | Update cloud customer address |
| `mattermost_update_command` | Update a command |
| `mattermost_update_config` | Update configuration |
| `mattermost_update_incoming_webhook` | Update an incoming webhook |
| `mattermost_update_marketplace_visited_by_admin` | Stores that the Plugin Marketplace has been visited by at least an admin. |
| `mattermost_update_outgoing_webhook` | Update an outgoing webhook |
| `mattermost_update_property_field` | Update a property field |
| `mattermost_update_property_values` | Update property values for a target |
| `mattermost_update_system_property_values` | Update property values for the system |
| `mattermost_upgrade_to_enterprise` | Executes an inplace upgrade from Team Edition to Enterprise Edition |
| `mattermost_upload_data` | Perform a file upload |
| `mattermost_upload_ldap_private_certificate` | Upload private key |
| `mattermost_upload_ldap_public_certificate` | Upload public certificate |
| `mattermost_upload_plugin` | Upload plugin |
| `mattermost_upload_remote_cluster_data` | Upload file data for a remote upload session. |
| `mattermost_upload_saml_idp_certificate` | Upload IDP certificate |
| `mattermost_upload_saml_private_certificate` | Upload private key |
| `mattermost_upload_saml_public_certificate` | Upload public certificate |
| `mattermost_validate_expression_against_requester` | Validate if the current user matches a CEL expression |
