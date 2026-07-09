---
name: mattermost-channel-messaging
skill_type: skill
description: >-
  Read and post Mattermost messages via the mattermost-mcp MCP server — list a
  channel's posts and threads, search posts, create a post or a threaded reply,
  and handle file attachments with the domain-typed condensed tools. Use when the
  agent must read recent conversation in a channel, search for a message, post an
  update, or reply in a thread. Do NOT use to create/rename channels or manage
  membership (mattermost-team-administration) or to mirror conversations into the
  knowledge graph (mattermost-kg-ingestion); prefer those.
license: MIT
tags: [mattermost, messaging, posts, channels, chatops, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# Mattermost Channel Messaging

Domain-typed access to Mattermost **posts** and **files** for reading and writing
channel conversation. Prefer these tools over raw HTTP — they carry the post field
conventions and return post-shaped records.

## When to use
- Read the recent posts of a channel, or a full thread from a root post.
- Search for a message across a team.
- Create a post, or reply within a thread (`root_id`).
- Read/attach files on a post.

## When NOT to use
- Create, rename, archive, or set channel privacy → `mattermost-team-administration`.
- Add/remove channel or team members → `mattermost-team-administration`.
- Push messages/channels into the knowledge graph → `mattermost-kg-ingestion`.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`mattermost-mcp`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `MATTERMOST_URL` | ✅ | Server base URL (alias `MATTERMOST_MCP_BASE_URL`) |
| `MATTERMOST_TOKEN` | ✅* | Personal-access / bot token |
| `MATTERMOST_MCP_USERNAME` / `MATTERMOST_MCP_PASSWORD` | ✅* | Login fallback if no token |
| `MATTERMOST_MCP_SSL_VERIFY` | optional | TLS verification toggle |

*Provide either a token or username+password. `MCP_TOOL_MODE`
(`condensed`|`verbose`|`both`) selects the condensed surface used below vs. the
one-to-one verbose tools.

## Tools & actions
Prefer the **condensed** tools; each takes `action` + a `params_json` **JSON string**
whose keys are passed straight to the client method.

| Condensed tool | Key actions |
|----------------|-------------|
| `mattermost_mcp_posts` | `get_posts_for_channel`, `get_post`, `get_post_thread`, `create_post`, `search_posts`, `pin_post`, `get_file_infos_for_post` |
| `mattermost_mcp_files` | `get_file`, `get_file_info`, `upload_file` |

### Key parameters
- `channel_id` — required for `get_posts_for_channel`.
- `post_id` — required for `get_post` / `get_post_thread`.
- `team_id` — required for `search_posts`.
- `create_post` body: `channel_id`, `message`, optional `root_id` (thread reply),
  optional `file_ids`.

## Recipes (`params_json`)
Read the latest posts in a channel:
```json
{"channel_id":"<channel_id>","per_page":30}
```
Fetch a full thread from a root post:
```json
{"post_id":"<root_post_id>"}
```
Post a new message:
```json
{"channel_id":"<channel_id>","message":"Deploy finished — all green ✅"}
```
Reply in a thread:
```json
{"channel_id":"<channel_id>","message":"On it.","root_id":"<root_post_id>"}
```
Search posts in a team:
```json
{"team_id":"<team_id>","terms":"incident postmortem"}
```

## Gotchas
- `params_json` is a **string** of JSON, not an object — serialize it.
- `get_posts_for_channel` returns `{"order":[...],"posts":{id:post}}`, not a flat
  list — iterate `order` to preserve chronology.
- A threaded reply needs BOTH `channel_id` and `root_id`; omitting `root_id` posts
  to the channel root, not the thread.
- Ids are 26-char Mattermost ids; resolve a channel from its name first with
  `mattermost_mcp_channels` action `get_channel_by_name`.

## Related
- `mattermost-team-administration` — teams, channels, membership.
- `mattermost-kg-ingestion` — mirror messages/structure into the knowledge graph.
