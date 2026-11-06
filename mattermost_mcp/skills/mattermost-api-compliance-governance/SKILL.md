---
name: mattermost-api-compliance-governance
skill_type: skill
description: >-
  Mattermost compliance, retention, access control and governance API. Compliance reports, data retention, attribute-based access control policies, content flagging review, audit logs and legal holds. Do NOT use for the task skills that already cover a workflow (mattermost-channel-messaging, mattermost-team-administration, mattermost-kg-ingestion).
license: MIT
tags: [mattermost, api-reference]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Mattermost compliance, retention, access control and governance API

Compliance reports, data retention, attribute-based access control policies, content flagging review, audit logs and legal holds.

Every operation is its own typed tool; arguments follow the upstream API (path parameters are required,
filters are optional arguments). Read first (get, list, search), change second, and obtain approval before
any delete, disable, revoke or reset.

| Tool | Summary |
|---|---|
| `mattermost_add_audit_log_certificate` | Upload audit log certificate |
| `mattermost_add_channels_to_retention_policy` | Add channels to a granular data retention policy |
| `mattermost_add_teams_to_retention_policy` | Add teams to a granular data retention policy |
| `mattermost_assign_access_control_policy_to_channels` | Assign an access control policy to channels or teams |
| `mattermost_check_access_control_policy_expression` | Check an access control policy expression |
| `mattermost_create_access_control_policy` | Create an access control policy |
| `mattermost_create_compliance_report` | Create report |
| `mattermost_create_data_retention_policy` | Create a new granular data retention policy |
| `mattermost_create_scheme` | Create a scheme |
| `mattermost_delete_access_control_policy` | Delete an access control policy |
| `mattermost_delete_data_retention_policy` | Delete a granular data retention policy |
| `mattermost_delete_export` | Delete an export file |
| `mattermost_delete_import` | Delete an import file |
| `mattermost_delete_scheme` | Delete a scheme |
| `mattermost_download_compliance_report` | Download a report |
| `mattermost_download_export` | Download an export file |
| `mattermost_generate_c_f_post_exposure_report` | Generate and download a post exposure report |
| `mattermost_generate_c_f_post_report` | Generate and download a flagged post report |
| `mattermost_get_access_control_policy` | Get an access control policy |
| `mattermost_get_access_control_policy_autocomplete_fields` | Get autocomplete fields for access control policies |
| `mattermost_get_ancillary_permissions_post` | Return all system console subsection ancillary permissions |
| `mattermost_get_audits` | Get audits |
| `mattermost_get_c_f_config` | Get the system content flagging configuration |
| `mattermost_get_c_f_fields` | Get content flagging property fields |
| `mattermost_get_c_f_flag_config` | Get content flagging configuration |
| `mattermost_get_c_f_post` | Get a flagged post with all its content. |
| `mattermost_get_c_f_post_field_values` | Get content flagging property field values for a post |
| `mattermost_get_c_f_team_status` | Get content flagging status for a team |
| `mattermost_get_channel_access_control_attributes` | Get access control attributes for a channel |
| `mattermost_get_channels_for_access_control_policy` | Get channels for an access control policy |
| `mattermost_get_channels_for_retention_policy` | Get the channels for a granular data retention policy |
| `mattermost_get_channels_for_scheme` | Get a page of channels which use this scheme. |
| `mattermost_get_compliance_report` | Get a report |
| `mattermost_get_compliance_reports` | Get reports |
| `mattermost_get_data_retention_policies` | Get the granular data retention policies |
| `mattermost_get_data_retention_policies_count` | Get the number of granular data retention policies |
| `mattermost_get_data_retention_policy` | Get the global data retention policy |
| `mattermost_get_data_retention_policy_by_i_d` | Get a granular data retention policy |
| `mattermost_get_flagged_posts_for_user` | Get a list of flagged posts |
| `mattermost_get_posts_for_reporting` | Get posts for reporting and compliance purposes using cursor-based pagination |
| `mattermost_get_scheme` | Get a scheme |
| `mattermost_get_schemes` | Get the schemes. |
| `mattermost_get_team_access_control_attributes` | Get the access control attributes governing a team |
| `mattermost_get_team_access_control_policy` | Get the access control policy for a team |
| `mattermost_get_teams_for_retention_policy` | Get the teams for a granular data retention policy |
| `mattermost_get_teams_for_scheme` | Get a page of teams which use this scheme. |
| `mattermost_get_user_audits` | Get user's audits |
| `mattermost_get_user_count_for_reporting` | Gets the full count of users that match the filter. |
| `mattermost_get_users_for_reporting` | Get a list of paged and sorted users for admin reporting purposes |
| `mattermost_import_team` | Import a Team from other application |
| `mattermost_keep_c_f_post` | Keep a flagged post |
| `mattermost_list_exports` | List export files |
| `mattermost_list_imports` | List import files |
| `mattermost_patch_data_retention_policy` | Patch a granular data retention policy |
| `mattermost_patch_scheme` | Patch a scheme |
| `mattermost_post_c_f_post_flag` | Flag a post |
| `mattermost_post_c_f_post_reviewer` | Assign a content reviewer to a flagged post |
| `mattermost_presign_export` | Create a presigned URL for export download |
| `mattermost_remove_audit_log_certificate` | Remove audit log certificate |
| `mattermost_remove_c_f_post` | Remove a flagged post |
| `mattermost_remove_channels_from_retention_policy` | Delete channels from a granular data retention policy |
| `mattermost_remove_teams_from_retention_policy` | Delete teams from a granular data retention policy |
| `mattermost_search_access_control_policies` | Search access control policies |
| `mattermost_search_c_f_team_reviewers` | Search content reviewers in a team |
| `mattermost_search_channels_for_access_control_policy` | Search channels for an access control policy |
| `mattermost_search_channels_for_retention_policy` | Search for the channels in a granular data retention policy |
| `mattermost_search_teams_for_retention_policy` | Search for the teams in a granular data retention policy |
| `mattermost_simulate_access_control_policy_for_users` | Simulate an access control policy decision for an explicit user list |
| `mattermost_start_batch_users_export` | Starts a job to export the users to a report file. |
| `mattermost_submit_performance_report` | Report client performance metrics |
| `mattermost_test_access_control_policy_expression` | Test an access control policy expression |
| `mattermost_unassign_access_control_policy_from_channels` | Unassign an access control policy from channels or teams |
| `mattermost_update_access_control_policies_active` | Activate or deactivate access control policies |
| `mattermost_update_access_control_policy_active_status` | Activate or deactivate an access control policy |
| `mattermost_update_c_f_config` | Update the system content flagging configuration |
| `mattermost_update_channel_member_scheme_roles` | Update the scheme-derived roles of a channel member. |
| `mattermost_update_channel_scheme` | Set a channel's scheme |
| `mattermost_update_team_member_scheme_roles` | Update the scheme-derived roles of a team member. |
| `mattermost_update_team_scheme` | Set a team's scheme |
