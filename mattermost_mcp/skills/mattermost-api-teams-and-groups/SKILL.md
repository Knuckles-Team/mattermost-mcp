---
name: mattermost-api-teams-and-groups
skill_type: skill
description: >-
  Mattermost teams and groups API. Teams, team members and invites, user groups and their syncables, LDAP group links. Do NOT use for the task skills that already cover a workflow (mattermost-channel-messaging, mattermost-team-administration, mattermost-kg-ingestion).
license: MIT
tags: [mattermost, api-reference]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Mattermost teams and groups API

Teams, team members and invites, user groups and their syncables, LDAP group links.

Every operation is its own typed tool; arguments follow the upstream API (path parameters are required,
filters are optional arguments). Read first (get, list, search), change second, and obtain approval before
any delete, disable, revoke or reset.

| Tool | Summary |
|---|---|
| `mattermost_accept_remote_cluster_invite` | Accept a remote cluster invite code. |
| `mattermost_add_group_members` | Adds members to a custom group |
| `mattermost_add_team_member` | Add user to team |
| `mattermost_add_team_member_from_invite` | Add user to team from invite |
| `mattermost_add_team_members` | Add multiple users to team |
| `mattermost_add_user_to_group_syncables` | Create memberships for LDAP configured channels and teams for this user |
| `mattermost_create_group` | Create a custom group |
| `mattermost_create_team` | Create a team |
| `mattermost_delete_group` | Deletes a custom group |
| `mattermost_delete_group_members` | Removes members from a custom group |
| `mattermost_generate_remote_cluster_invite` | Generate invite code. |
| `mattermost_get_all_teams` | Get teams |
| `mattermost_get_c_p_a_group` | Get Custom Profile Attribute property group data |
| `mattermost_get_group` | Get a group |
| `mattermost_get_group_stats` | Get group stats |
| `mattermost_get_group_syncable_for_team_id` | Get a team syncable for a group |
| `mattermost_get_group_syncables_teams` | Get team syncables for a group |
| `mattermost_get_group_users` | Get group users |
| `mattermost_get_groups` | Get groups |
| `mattermost_get_groups_by_names` | Get groups by name |
| `mattermost_get_groups_by_team` | Get team groups |
| `mattermost_get_groups_by_user_id` | Get groups for a userId |
| `mattermost_get_ldap_groups` | Returns a list of LDAP groups |
| `mattermost_get_team` | Get a team |
| `mattermost_get_team_by_name` | Get a team by name |
| `mattermost_get_team_icon` | Get the team icon |
| `mattermost_get_team_invite_info` | Get invite info for a team |
| `mattermost_get_team_member` | Get a team member |
| `mattermost_get_team_members` | Get team members |
| `mattermost_get_team_members_by_ids` | Get team members by ids |
| `mattermost_get_team_members_for_user` | Get team members for a user |
| `mattermost_get_team_policies_for_user` | Get the policies which are applied to a user's teams |
| `mattermost_get_team_stats` | Get a team stats |
| `mattermost_get_teams_for_user` | Get a user's teams |
| `mattermost_get_teams_usage` | Get current usage of teams |
| `mattermost_ingest_teams` | Ingest Mattermost teams into medulla as typed :Team nodes. |
| `mattermost_invalidate_email_invites` | Invalidate active email invitations |
| `mattermost_invite_guests_to_team` | Invite guests to the team by email |
| `mattermost_invite_users_to_team` | Invite users to the team by email |
| `mattermost_link_group_syncable_for_team` | Link a team to a group |
| `mattermost_link_ldap_group` | Link a LDAP group |
| `mattermost_patch_group` | Patch a group |
| `mattermost_patch_group_syncable_for_team` | Patch a team syncable for a group |
| `mattermost_patch_team` | Patch a team |
| `mattermost_regenerate_team_invite_id` | Regenerate the Invite ID from a Team |
| `mattermost_remote_cluster_confirm_invite` | Confirm an invite with a remote cluster. |
| `mattermost_remove_team_icon` | Remove the team icon |
| `mattermost_remove_team_member` | Remove user from team |
| `mattermost_restore_group` | Restore a previously deleted group. |
| `mattermost_restore_team` | Restore a team |
| `mattermost_search_teams` | Search teams |
| `mattermost_set_team_icon` | Sets the team icon |
| `mattermost_soft_delete_team` | Delete a team |
| `mattermost_team_exists` | Check if team exists |
| `mattermost_team_members_minus_group_members` | Team members minus group members. |
| `mattermost_unlink_group_syncable_for_team` | Unlink a team from a group |
| `mattermost_unlink_ldap_group` | Delete a link for LDAP group |
| `mattermost_update_team` | Update a team |
| `mattermost_update_team_member_roles` | Update a team member roles |
| `mattermost_update_team_privacy` | Update teams's privacy |
