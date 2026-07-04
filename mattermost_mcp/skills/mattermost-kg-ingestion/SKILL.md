---
name: mattermost-kg-ingestion
description: >-
  Natively ingest Mattermost into the epistemic-graph knowledge graph via the
  mattermost-mcp MCP server — push teams, channels and users as typed
  :Team/:Channel/:Person nodes, messages as :Document nodes, and file attachments
  as :MediaAsset blobs, in one ACID path. Use when the agent must make a Mattermost
  workspace searchable/queryable in the KG, or refresh its mirror. Do NOT use to
  read or post messages (mattermost-channel-messaging) or to provision teams and
  channels (mattermost-team-administration); prefer those.
license: MIT
tags: [mattermost, knowledge-graph, ingestion, kg, owl, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# Mattermost Knowledge-Graph Ingestion

Push Mattermost structure and conversation into the ONE epistemic-graph engine as
typed OWL nodes, message documents, and attachment blobs. Backed by
`mattermost_mcp.kg_ingest` / `kg_media` and federated by `mattermost_mcp.ontology`
(`http://knuckles.team/kg/mattermost`).

## When to use
- Make a Mattermost workspace queryable in the KG (`:Team`, `:Channel`, `:Person`).
- Index a channel's conversation for semantic search (`:Document` messages).
- Store file attachments durably as content-addressed `:MediaAsset` blobs.
- Refresh an existing mirror (ingestion is idempotent MERGE by node id).

## When NOT to use
- Interactive read/post of messages → `mattermost-channel-messaging`.
- Creating/administering teams and channels → `mattermost-team-administration`.
- Querying the graph after ingestion → the graph-os KG query tools, not this skill.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`mattermost-mcp`** MCP server, plus a
reachable epistemic-graph engine (else the ingest legs no-op and return
`{"ingested": null}` — safe, but nothing is written).

| Variable | Required | Notes |
|----------|----------|-------|
| `MATTERMOST_URL` | ✅ | Server base URL (alias `MATTERMOST_MCP_BASE_URL`) |
| `MATTERMOST_TOKEN` | ✅* | Personal-access / bot token |
| `MATTERMOST_MCP_USERNAME` / `MATTERMOST_MCP_PASSWORD` | ✅* | Login fallback if no token |
| `MATTERMOST_MCP_SSL_VERIFY` | optional | TLS verification toggle |

*Provide either a token or username+password.

## Tools & actions
Prefer the native Wire-First ingest tools — they list via the real client and push in
one call. Each returns `{"listed": n, "ingested": {"nodes":…, "edges":…}}`.

| Tool | What it ingests |
|------|-----------------|
| `mattermost_ingest_teams` | teams → `:Team` nodes |
| `mattermost_ingest_channels` | a team's channels → `:Channel` (+ `:inTeam`) |
| `mattermost_ingest_users` | users → shared `:Person` / `:Bot` nodes |
| `mattermost_ingest_posts` | a channel's messages → `:Document` (+ `:postedInChannel` / `:authoredBy` / `:repliesTo`) |

### Key parameters
- `mattermost_ingest_channels` — requires `team_id`.
- `mattermost_ingest_posts` — requires `channel_id`.
- `params_json` — JSON string of the underlying list-call filters (`page`, `per_page`).

## Recipes (`params_json`)
Ingest all teams:
```json
{}
```
Ingest one team's channels (tool arg `team_id` + filters):
```json
{"per_page":100}
```
Ingest a channel's recent messages (tool arg `channel_id` + filters):
```json
{"per_page":50}
```

Typical order: `mattermost_ingest_teams` → `mattermost_ingest_channels` (per team) →
`mattermost_ingest_users` → `mattermost_ingest_posts` (per channel), so the
`:inTeam` / `:postedInChannel` / `:authoredBy` links resolve to nodes that exist.

## Gotchas
- Node ids are stable: `mattermost:team:<id>`, `mattermost:channel:<id>`,
  `mattermost:user:<id>`, `mattermost:post:<id>` — re-ingest MERGEs, never duplicates.
- Empty / system-only posts (no `message`) are skipped by design.
- No reachable engine ⇒ `{"ingested": null}` and a clean no-op — check for a live
  graph-os if you expected writes.
- Edges are best-effort: a link to a not-yet-ingested node is silently skipped, so
  ingest teams/channels/users **before** posts.
- Attachment bytes go through `kg_media.ingest_file_attachment` (`:MediaAsset` blob);
  fetch the bytes with `mattermost_mcp_files` action `get_file` first.

## Related
- `mattermost-channel-messaging` — read the messages this skill indexes.
- `mattermost-team-administration` — the teams/channels this skill mirrors.
