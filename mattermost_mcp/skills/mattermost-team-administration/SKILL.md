---
name: mattermost-team-administration
skill_type: skill
description: >-
  Administer Mattermost teams and channels via the mattermost-mcp MCP server —
  list/create teams, list/create/rename/archive channels, set channel privacy, and
  manage team and channel membership with its typed tools. Use when
  the agent must provision a channel, resolve a channel or team by name, add/remove
  members, or read team/channel stats. Do NOT use to read or post messages
  (mattermost-channel-messaging) or to ingest structure into the knowledge graph
  (mattermost-kg-ingestion); prefer those.
license: MIT
tags: [mattermost, teams, channels, membership, administration, mcp]
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---

# Mattermost Team Administration

Every step below is one typed tool call; there is no `action` or JSON-string argument. Resolve ids by name first, read before you change, and ask for approval before anything destructive.

## Verify connection

Confirm the server answers and the credential identifies the acting user.

1. `mattermost_get_ping` (get_server_status, device_id, use_rest_semantics)
2. `mattermost_get_user` (user_id)

## Find people

Resolve a person to a user id and see whether they are online.

1. `mattermost_get_user_by_username` (username)
2. `mattermost_get_user_by_email` (email)
3. `mattermost_search_users` (term, team_id, not_in_team_id, in_channel_id, not_in_channel_id, in_group_id, group_constrained, allow_inactive, without_team, limit)
4. `mattermost_get_users_by_usernames`
5. `mattermost_get_user_status` (user_id)

## Find channel

Resolve a channel by name or search and read its stats.

1. `mattermost_get_team_by_name` (team_name)
2. `mattermost_get_channel_by_name_for_team_name` (team_name, channel_name, include_deleted)
3. `mattermost_get_channel_by_name` (team_id, channel_name, include_deleted)
4. `mattermost_search_channels` (team_id, term)
5. `mattermost_get_channels_for_team_for_user` (user_id, team_id, include_deleted, last_delete_at)
6. `mattermost_get_public_channels_for_team` (team_id, page, per_page)
7. `mattermost_get_channel` (channel_id)
8. `mattermost_get_channel_stats` (channel_id)

## Create channel and invite

Create a channel, invite members and add a bookmark.

1. `mattermost_get_team_by_name` (team_name)
2. `mattermost_create_channel` (team_id, name, display_name, type, purpose, header, managed_category_name, default_category_name)
3. `mattermost_add_channel_member` (channel_id, user_id, user_ids, post_root_id)
4. `mattermost_get_channel_members` (channel_id, page, per_page)
5. `mattermost_create_channel_bookmark` (channel_id, display_name, type, file_id, link_url, image_url, emoji)

## Manage channel membership

Review and change who is in a channel.

1. `mattermost_get_channel_members` (channel_id, page, per_page)
2. `mattermost_get_channel_member` (channel_id, user_id)
3. `mattermost_add_channel_member` (channel_id, user_id, user_ids, post_root_id)
4. `mattermost_remove_user_from_channel` (channel_id, user_id, confirm)

## Set up team

Create a team and bring people in.

1. `mattermost_get_team_by_name` (team_name)
2. `mattermost_create_team` (name, display_name, type)
3. `mattermost_add_team_member` (team_id, user_id)
4. `mattermost_invite_users_to_team` (team_id, graceful)
5. `mattermost_get_team_members` (team_id, page, per_page, sort, exclude_deleted_users)
6. `mattermost_get_team_stats` (team_id)

## Manage bots and webhooks

Create bots and incoming or outgoing webhooks, and switch them off.

1. `mattermost_create_bot` (username, display_name, description)
2. `mattermost_get_bots` (page, per_page, include_deleted, only_orphaned)
3. `mattermost_patch_bot` (bot_user_id, username, display_name, description)
4. `mattermost_disable_bot` (bot_user_id)
5. `mattermost_enable_bot` (bot_user_id)
6. `mattermost_create_incoming_webhook` (channel_id, user_id, display_name, description, username, icon_url, channel_locked)
7. `mattermost_get_incoming_webhooks` (page, per_page, team_id, include_total_count)
8. `mattermost_delete_incoming_webhook` (hook_id, confirm)
9. `mattermost_create_outgoing_webhook` (team_id, display_name, trigger_words, callback_urls, channel_id, creator_id, description, trigger_when, content_type)
10. `mattermost_get_outgoing_webhooks` (page, per_page, team_id, channel_id)

## Manage user accounts

Create, deactivate and re-role user accounts.

1. `mattermost_get_user` (user_id)
2. `mattermost_create_user` (email, username, t, iid, first_name, last_name, nickname, position, timezone, auth_data, auth_service, password, locale, props, notify_props)
3. `mattermost_patch_user` (user_id, email, username, first_name, last_name, nickname, locale, position, timezone, props, notify_props)
4. `mattermost_update_user_active` (user_id, active)
5. `mattermost_update_user_roles` (user_id, roles)

## Compliance and audit

Create and download compliance reports and read the audit log.

1. `mattermost_create_compliance_report`
2. `mattermost_get_compliance_reports` (page, per_page)
3. `mattermost_get_compliance_report` (report_id)
4. `mattermost_download_compliance_report` (report_id)
5. `mattermost_get_audits` (page, per_page)
6. `mattermost_get_user_audits` (user_id)

## Guardrails

- Never print tokens, passwords or webhook secrets.
- Public or destructive actions need the requester's confirmation of the target and text.
- Report ids (and refusal codes) for every call.
