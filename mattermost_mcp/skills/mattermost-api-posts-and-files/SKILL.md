---
name: mattermost-api-posts-and-files
skill_type: skill
description: >-
  Mattermost posts, threads, reactions, files and emoji API. Everything about messages beyond the basic post, read and search workflows: reactions, drafts, acknowledgements, edit history, file transfer, bookmarks, emoji and recaps. Do NOT use for the task skills that already cover a workflow (mattermost-channel-messaging, mattermost-team-administration, mattermost-kg-ingestion).
license: MIT
tags: [mattermost, api-reference]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Mattermost posts, threads, reactions, files and emoji API

Everything about messages beyond the basic post, read and search workflows: reactions, drafts, acknowledgements, edit history, file transfer, bookmarks, emoji and recaps.

Every operation is its own typed tool; arguments follow the upstream API (path parameters are required,
filters are optional arguments). Read first (get, list, search), change second, and obtain approval before
any delete, disable, revoke or reset.

| Tool | Summary |
|---|---|
| `mattermost_acknowledge_notification` | Acknowledge receiving of a notification |
| `mattermost_autocomplete_emoji` | Autocomplete custom emoji |
| `mattermost_burn_post` | Burn a burn-on-read post |
| `mattermost_create_channel_bookmark` | Create channel bookmark |
| `mattermost_create_emoji` | Create a custom emoji |
| `mattermost_create_post` | Create a post |
| `mattermost_create_post_ephemeral` | Create a ephemeral post |
| `mattermost_create_recap` | Create a channel recap |
| `mattermost_create_scheduled_post` | Creates a scheduled post |
| `mattermost_create_scheduled_recap` | Create a scheduled recap |
| `mattermost_delete_acknowledgement_for_post` | Delete a post acknowledgement |
| `mattermost_delete_brand_image` | Delete current brand image |
| `mattermost_delete_channel_bookmark` | Delete channel bookmark |
| `mattermost_delete_draft` | Delete synced draft |
| `mattermost_delete_draft_for_thread` | Delete synced thread draft |
| `mattermost_delete_emoji` | Delete a custom emoji |
| `mattermost_delete_post` | Delete a post |
| `mattermost_delete_reaction` | Remove a reaction from a post |
| `mattermost_delete_recap` | Delete a recap |
| `mattermost_delete_scheduled_post` | Delete a scheduled post |
| `mattermost_delete_scheduled_recap` | Delete a scheduled recap |
| `mattermost_do_post_action` | Perform a post action |
| `mattermost_get_brand_image` | Get brand image |
| `mattermost_get_channel_unread` | Get unread messages |
| `mattermost_get_default_profile_image` | Return user's default (generated) profile image |
| `mattermost_get_drafts` | Get synced drafts for a team |
| `mattermost_get_edit_history_for_post` | Get post edit history |
| `mattermost_get_emoji` | Get a custom emoji |
| `mattermost_get_emoji_by_name` | Get a custom emoji by name |
| `mattermost_get_emoji_image` | Get custom emoji image |
| `mattermost_get_emoji_list` | Get a list of custom emoji |
| `mattermost_get_emojis_by_names` | Get custom emojis by name |
| `mattermost_get_file` | Get a file |
| `mattermost_get_file_info` | Get metadata for a file |
| `mattermost_get_file_infos_for_post` | Get file info for post |
| `mattermost_get_file_link` | Get a public file link |
| `mattermost_get_file_preview` | Get a file's preview |
| `mattermost_get_file_public` | Get a public file |
| `mattermost_get_file_thumbnail` | Get a file's thumbnail |
| `mattermost_get_image_by_url` | Get an image by url |
| `mattermost_get_pinned_posts` | Get a channel's pinned posts |
| `mattermost_get_post` | Get a post |
| `mattermost_get_post_info` | Get post info |
| `mattermost_get_post_thread` | Get a thread |
| `mattermost_get_posts_around_last_unread` | Get posts around oldest unread |
| `mattermost_get_posts_by_ids` | Get posts by a list of ids |
| `mattermost_get_posts_for_channel` | Get posts for a channel |
| `mattermost_get_posts_for_view` | Get posts for a view |
| `mattermost_get_posts_usage` | Get current usage of posts |
| `mattermost_get_profile_image` | Get user's profile image |
| `mattermost_get_reactions` | Get a list of reactions to a post |
| `mattermost_get_recap` | Get a specific recap |
| `mattermost_get_recap_limit_status` | Get recap limit status for the current user |
| `mattermost_get_recaps_for_user` | Get current user's recaps |
| `mattermost_get_scheduled_recap` | Get a scheduled recap |
| `mattermost_get_scheduled_recaps` | Get current user's scheduled recaps |
| `mattermost_get_team_unread` | Get unreads for a team |
| `mattermost_get_teams_unread_for_user` | Get team unreads for a user |
| `mattermost_get_user_scheduled_posts` | Gets all scheduled posts for a user for the specified team.. |
| `mattermost_get_user_thread` | Get a thread followed by the user |
| `mattermost_get_user_threads` | Get all threads that user is following |
| `mattermost_ingest_posts` | Ingest a channel's messages as :Document nodes (+ channel/author links). |
| `mattermost_list_channel_bookmarks_for_channel` | Get channel bookmarks for Channel |
| `mattermost_mark_recap_as_read` | Mark a recap as read |
| `mattermost_mark_recaps_as_viewed` | Mark all of the authenticated user's finished recaps as viewed |
| `mattermost_move_thread` | Move a post (and any posts within that post's thread) |
| `mattermost_patch_post` | Patch a post |
| `mattermost_pause_scheduled_recap` | Pause a scheduled recap |
| `mattermost_pin_post` | Pin a post to the channel |
| `mattermost_post_endpoint_for_cws_webhooks` | POST endpoint for CWS Webhooks |
| `mattermost_post_log` | Add log message |
| `mattermost_post_user_recent_custom_status_delete` | Delete user's recent custom status |
| `mattermost_preview_license_file` | Preview license file |
| `mattermost_regenerate_recap` | Regenerate a recap |
| `mattermost_remote_set_profile_image` | Set profile image for a remote user. |
| `mattermost_remove_license_file` | Remove license file |
| `mattermost_restore_post_version` | Restores a past version of a post |
| `mattermost_resume_scheduled_recap` | Resume a scheduled recap |
| `mattermost_reveal_post` | Reveal a burn-on-read post |
| `mattermost_save_acknowledgement_for_post` | Acknowledge a post |
| `mattermost_save_reaction` | Create a reaction |
| `mattermost_search_emoji` | Search custom emoji |
| `mattermost_search_files` | Search files across the teams of the current user |
| `mattermost_search_posts` | Search for team posts |
| `mattermost_search_posts_in_all_teams` | Search posts across all teams |
| `mattermost_search_team_files` | Search files in a team |
| `mattermost_set_default_profile_image` | Delete user's profile image |
| `mattermost_set_post_reminder` | Set a post reminder |
| `mattermost_set_post_unread` | Mark as unread from a post. |
| `mattermost_set_profile_image` | Set user's profile image |
| `mattermost_set_thread_unread_by_post_id` | Mark a thread that user is following as unread based on a post id |
| `mattermost_start_following_thread` | Start following a thread |
| `mattermost_stop_following_thread` | Stop following a thread |
| `mattermost_test_file_store_connection` | Test the configured file storage backend |
| `mattermost_test_notification` | Send a test notification |
| `mattermost_trigger_notify_admin_posts` | Trigger notify-admin posts |
| `mattermost_unpin_post` | Unpin a post to the channel |
| `mattermost_update_channel_bookmark` | Update channel bookmark |
| `mattermost_update_channel_bookmark_sort_order` | Update channel bookmark's order |
| `mattermost_update_post` | Update a post |
| `mattermost_update_scheduled_post` | Update a scheduled post |
| `mattermost_update_scheduled_recap` | Update a scheduled recap |
| `mattermost_update_thread_read_for_user` | Mark a thread that user is following read state to the timestamp |
| `mattermost_update_threads_read_for_user` | Mark all threads that user is following as read |
| `mattermost_upload_brand_image` | Upload brand image |
| `mattermost_upload_file` | Upload a file |
| `mattermost_upload_license_file` | Upload license file |
| `mattermost_upsert_draft` | Upsert synced draft |
