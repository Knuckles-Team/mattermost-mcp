---
name: mattermost-team-administration
skill_type: skill
description: >-
  Administer Mattermost teams and channels via the mattermost-mcp MCP server —
  list/create teams, list/create/rename/archive channels, set channel privacy, and
  manage team & channel membership with the domain-typed condensed tools. Use when
  the agent must provision a channel, resolve a channel or team by name, add/remove
  members, or read team/channel stats. Do NOT use to read or post messages
  (mattermost-channel-messaging) or to ingest structure into the knowledge graph
  (mattermost-kg-ingestion); prefer those.
license: MIT
tags: [mattermost, teams, channels, membership, administration, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# Mattermost Team Administration

Domain-typed access to Mattermost **teams**, **channels**, and their **membership**.
Prefer these tools over raw HTTP — they carry the team/channel field conventions and
return team/channel-shaped records.

## When to use
- List or create teams; look a team up by name; read team stats and members.
- List, create, rename, archive, or restore channels within a team.
- Set channel privacy (public `O` ↔ private `P`).
- Add or remove team / channel members.

## When NOT to use
- Read or post messages / threads / files → `mattermost-channel-messaging`.
- Mirror teams/channels/users into the knowledge graph → `mattermost-kg-ingestion`.
- Server-wide system/compliance/plugins config → use the corresponding condensed
  tool (`mattermost_mcp_system`, `mattermost_mcp_compliance`, …) directly.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`mattermost-mcp`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `MATTERMOST_URL` | ✅ | Server base URL (alias `MATTERMOST_MCP_BASE_URL`) |
| `MATTERMOST_TOKEN` | ✅* | Personal-access / bot token (needs admin scope for create/delete) |
| `MATTERMOST_MCP_USERNAME` / `MATTERMOST_MCP_PASSWORD` | ✅* | Login fallback if no token |
| `MATTERMOST_MCP_SSL_VERIFY` | optional | TLS verification toggle |

*Provide either a token or username+password. `MCP_TOOL_MODE` selects the condensed
vs. verbose surface.

## Tools & actions
Prefer the **condensed** tools; each takes `action` + a `params_json` **JSON string**.

| Condensed tool | Key actions |
|----------------|-------------|
| `mattermost_mcp_teams` | `get_all_teams`, `create_team`, `get_team`, `get_team_by_name`, `get_team_members`, `add_team_member`, `remove_team_member`, `get_team_stats` |
| `mattermost_mcp_channels` | `get_public_channels_for_team`, `create_channel`, `get_channel`, `get_channel_by_name`, `patch_channel`, `update_channel_privacy`, `delete_channel`, `restore_channel`, `add_channel_member`, `remove_user_from_channel`, `get_channel_members` |

### Key parameters
- `team_id` — required for team reads and channel listing.
- `channel_id` — required for channel reads/patches/membership.
- `create_channel` body: `team_id`, `name` (URL slug), `display_name`, `type`
  (`O` public / `P` private).
- `create_team` body: `name`, `display_name`, `type` (`O` open / `I` invite-only).

## Recipes (`params_json`)
List a team's public channels:
```json
{"team_id":"<team_id>","per_page":100}
```
Resolve a channel by name within a team:
```json
{"team_id":"<team_id>","channel_name":"deployments"}
```
Create a private channel:
```json
{"team_id":"<team_id>","name":"sec-incidents","display_name":"Sec Incidents","type":"P"}
```
Add a user to a channel:
```json
{"channel_id":"<channel_id>","user_id":"<user_id>"}
```

## Gotchas
- `params_json` is a **string** of JSON, not an object — serialize it.
- `name` is the URL slug (lowercase, no spaces); `display_name` is the human label —
  don't swap them.
- `delete_channel` **archives** (soft-delete); use `restore_channel` to bring it back.
- Channel `type` codes: `O`=public, `P`=private, `D`=direct, `G`=group; team `type`
  codes: `O`=open, `I`=invite-only.
- Create/delete require an admin-scoped token; a plain bot token may 403.

## Related
- `mattermost-channel-messaging` — read/post messages once a channel exists.
- `mattermost-kg-ingestion` — mirror the team/channel/user graph into the KG.
