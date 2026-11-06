---
name: mattermost-api-channels
skill_type: skill
description: >-
  Mattermost channels API. Channel records, members, moderation, views, categories and sidebar, shared channels and direct and group messages. Do NOT use for the task skills that already cover a workflow (mattermost-channel-messaging, mattermost-team-administration, mattermost-kg-ingestion).
license: MIT
tags: [mattermost, api-reference]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Mattermost channels API

Channel records, members, moderation, views, categories and sidebar, shared channels and direct and group messages.

Every operation is its own typed tool; arguments follow the upstream API (path parameters are required,
filters are optional arguments). Read first (get, list, search), change second, and obtain approval before
any delete, disable, revoke or reset.

| Tool | Summary |
|---|---|
| `mattermost_add_channel_member` | Add user(s) to channel |
| `mattermost_autocomplete_channels_for_team` | Autocomplete channels |
| `mattermost_autocomplete_channels_for_team_for_search` | Autocomplete channels for search |
| `mattermost_can_user_direct_message` | Check if user can DM another user in shared channels context |
| `mattermost_channel_members_minus_group_members` | Channel members minus group members. |
| `mattermost_convert_group_message_to_channel` | Convert group message to private channel |
| `mattermost_create_channel` | Create a channel |
| `mattermost_create_channel_view` | Create channel view |
| `mattermost_create_direct_channel` | Create a direct message channel |
| `mattermost_create_group_channel` | Create a group message channel |
| `mattermost_create_sidebar_category_for_team_for_user` | Create user's sidebar category |
| `mattermost_delete_channel` | Delete a channel |
| `mattermost_delete_channel_view` | Delete a channel view |
| `mattermost_get_all_channels` | Get a list of all channels |
| `mattermost_get_all_shared_channels` | Get all shared channels for team. |
| `mattermost_get_channel` | Get a channel |
| `mattermost_get_channel_by_name` | Get a channel by name |
| `mattermost_get_channel_by_name_for_team_name` | Get a channel by name and team name |
| `mattermost_get_channel_member` | Get channel member |
| `mattermost_get_channel_member_counts_by_group` | Channel members counts for each group that has at least one member in the channel |
| `mattermost_get_channel_members` | Get channel members |
| `mattermost_get_channel_members_by_ids` | Get channel members by ids |
| `mattermost_get_channel_members_for_user` | Get channel memberships and roles for a user |
| `mattermost_get_channel_members_timezones` | Get timezones in a channel |
| `mattermost_get_channel_members_with_team_data_for_user` | Get all channel members from all teams for a user |
| `mattermost_get_channel_moderations` | Get information about channel's moderation. |
| `mattermost_get_channel_policies_for_user` | Get the policies which are applied to a user's channels |
| `mattermost_get_channel_stats` | Get channel statistics |
| `mattermost_get_channel_view` | Get a channel view |
| `mattermost_get_channels_for_team_for_user` | Get channels for user |
| `mattermost_get_channels_for_user` | Get all channels from all teams |
| `mattermost_get_channels_member_count` | Get member counts for multiple channels |
| `mattermost_get_deleted_channels_for_team` | Get deleted channels |
| `mattermost_get_group_message_members_common_teams` | Get common teams for members of a Group Message. |
| `mattermost_get_group_syncable_for_channel_id` | Get a channel syncable for a group |
| `mattermost_get_group_syncables_channels` | Get channel syncables for a group |
| `mattermost_get_groups_associated_to_channels_by_team` | Get team groups by channels |
| `mattermost_get_groups_by_channel` | Get channel groups |
| `mattermost_get_private_channels_for_team` | Get private channels |
| `mattermost_get_public_channels_by_ids_for_team` | Get a list of channels by ids |
| `mattermost_get_public_channels_for_team` | Get public channels |
| `mattermost_get_recommended_channels_for_team` | Get recommended public channels for the current user |
| `mattermost_get_redirect_location` | Get redirect location |
| `mattermost_get_shared_channel_remotes` | Get remote clusters for a shared channel |
| `mattermost_get_shared_channel_remotes_by_remote_cluster` | Get shared channel remotes by remote cluster. |
| `mattermost_get_sidebar_categories_for_team_for_user` | Get user's sidebar categories |
| `mattermost_get_sidebar_category_for_team_for_user` | Get sidebar category |
| `mattermost_get_sidebar_category_order_for_team_for_user` | Get user's sidebar category order |
| `mattermost_get_users_by_group_channel_ids` | Get users by group channels ids |
| `mattermost_ingest_channels` | Ingest a team's channels as typed :Channel nodes (+ :inTeam links). |
| `mattermost_invite_remote_cluster_to_channel` | Invites a remote cluster to a channel. |
| `mattermost_link_group_syncable_for_channel` | Link a channel to a group |
| `mattermost_list_channel_views` | List channel views |
| `mattermost_mark_all_direct_messages_read` | Mark all direct and group messages as read |
| `mattermost_mark_all_team_channels_read` | Mark all channels and threads in a team as read |
| `mattermost_mark_channels_read_for_user` | Mark multiple channels as read |
| `mattermost_move_channel` | Move a channel |
| `mattermost_patch_channel` | Patch a channel |
| `mattermost_patch_channel_moderations` | Update a channel's moderation settings. |
| `mattermost_patch_group_syncable_for_channel` | Patch a channel syncable for a group |
| `mattermost_remove_sidebar_category_for_team_for_user` | Delete sidebar category |
| `mattermost_remove_user_from_channel` | Remove user from channel |
| `mattermost_restore_channel` | Restore a channel |
| `mattermost_search_all_channels` | Search all private and open type channels across all teams |
| `mattermost_search_channels` | Search channels |
| `mattermost_search_group_channels` | Search Group Channels |
| `mattermost_set_channel_members` | Set channel members |
| `mattermost_uninvite_remote_cluster_to_channel` | Uninvites a remote cluster to a channel. |
| `mattermost_unlink_group_syncable_for_channel` | Unlink a channel from a group |
| `mattermost_update_channel` | Update a channel |
| `mattermost_update_channel_member_autotranslation` | Update channel member autotranslation setting |
| `mattermost_update_channel_notify_props` | Update channel notifications |
| `mattermost_update_channel_privacy` | Update channel's privacy |
| `mattermost_update_channel_roles` | Update channel roles |
| `mattermost_update_channel_view` | Update a channel view |
| `mattermost_update_channel_view_sort_order` | Update a channel view's sort order |
| `mattermost_update_sidebar_categories_for_team_for_user` | Update user's sidebar categories |
| `mattermost_update_sidebar_category_for_team_for_user` | Update sidebar category |
| `mattermost_update_sidebar_category_order_for_team_for_user` | Update user's sidebar category order |
| `mattermost_view_channel` | View channel |
