---
name: mattermost-channel-messaging
skill_type: skill
description: >-
  Read and post Mattermost messages via the mattermost-mcp MCP server — list a
  channel's posts and threads, search posts, create a post or a threaded reply,
  and handle file attachments with its typed tools. Use when the
  agent must read recent conversation in a channel, search for a message, post an
  update, or reply in a thread. Do NOT use to create/rename channels or manage
  membership (mattermost-team-administration) or to mirror conversations into the
  knowledge graph (mattermost-kg-ingestion); prefer those.
license: MIT
tags: [mattermost, messaging, posts, channels, chatops, mcp]
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---

# Mattermost Channel Messaging

Every step below is one typed tool call; there is no `action` or JSON-string argument. Resolve ids by name first, read before you change, and ask for approval before anything destructive.

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

## Read channel conversation

Read recent posts, a thread and the pinned posts of a channel.

1. `mattermost_get_posts_for_channel` (channel_id, page, per_page, since, before, after, include_deleted, type)
2. `mattermost_get_post` (post_id, include_deleted)
3. `mattermost_get_post_thread` (post_id, perPage, fromPost, fromCreateAt, fromUpdateAt, direction, skipFetchThreads, collapsedThreads, collapsedThreadsExtended, updatesOnly)
4. `mattermost_get_pinned_posts` (channel_id)
5. `mattermost_get_posts_by_ids`
6. `mattermost_get_file_infos_for_post` (post_id, include_deleted)

## Search messages

Search posts and files across a team or the whole server.

1. `mattermost_search_posts` (team_id, terms, is_or_search, time_zone_offset, include_deleted_channels, page, per_page)
2. `mattermost_search_posts_in_all_teams` (terms, is_or_search, time_zone_offset, include_deleted_channels, page, per_page)
3. `mattermost_search_files` (terms, is_or_search, time_zone_offset, include_deleted_channels, page, per_page)
4. `mattermost_search_team_files` (team_id, terms, is_or_search, time_zone_offset, include_deleted_channels, page, per_page)

## Post message

Post a message, with an attachment, into a channel.

1. `mattermost_get_channel_by_name_for_team_name` (team_name, channel_name, include_deleted)
2. `mattermost_upload_file` (channel_id, filename, files, client_ids)
3. `mattermost_create_post` (channel_id, message, set_online, silent, root_id, file_ids, props, metadata)
4. `mattermost_get_post` (post_id, include_deleted)

## Reply in thread

Read a thread and reply or react in it.

1. `mattermost_get_post_thread` (post_id, perPage, fromPost, fromCreateAt, fromUpdateAt, direction, skipFetchThreads, collapsedThreads, collapsedThreadsExtended, updatesOnly)
2. `mattermost_create_post` (channel_id, message, set_online, silent, root_id, file_ids, props, metadata)
3. `mattermost_save_reaction` (user_id, post_id, emoji_name, create_at)
4. `mattermost_get_reactions` (post_id)

## Edit or retract message

Correct, pin, unpin or delete a message.

1. `mattermost_get_post` (post_id, include_deleted)
2. `mattermost_update_post` (post_id, id, is_pinned, message, has_reactions, props)
3. `mattermost_patch_post` (post_id, is_pinned, message, file_ids, has_reactions, props)
4. `mattermost_pin_post` (post_id)
5. `mattermost_unpin_post` (post_id)
6. `mattermost_delete_post` (post_id, confirm)

## Schedule message or reminder

Schedule a post for later or set a reminder on one.

1. `mattermost_create_scheduled_post` (scheduled_at, channel_id, message, root_id, file_ids, props, repeat_type, repeat_timezone)
2. `mattermost_get_user_scheduled_posts` (includeDirectChannels)
3. `mattermost_update_scheduled_post` (scheduled_post_id, id, channel_id, user_id, scheduled_at, message, repeat_type, repeat_timezone)
4. `mattermost_delete_scheduled_post` (scheduled_post_id, confirm)
5. `mattermost_set_post_reminder` (user_id, post_id, target_time)

## Rewrite draft message

Have the server's AI agent shorten or polish a draft before posting.

1. `mattermost_rewrite_message` (agent_id, message, action, custom_prompt)

## Guardrails

- Never print tokens, passwords or webhook secrets.
- Public or destructive actions need the requester's confirmation of the target and text.
- Report ids (and refusal codes) for every call.
