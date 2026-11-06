---
name: mattermost-kg-ingestion
skill_type: skill
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
  author: Knuckles-Team
  version: '0.1.0'
---

# Mattermost Kg Ingestion

Every step below is one typed tool call; there is no `action` or JSON-string argument. Resolve ids by name first, read before you change, and ask for approval before anything destructive.

## Mirror workspace to graph

Land teams, channels, users and posts in the knowledge graph.

1. `mattermost_ingest_teams` (page, per_page, include_total_count, exclude_policy_constrained)
2. `mattermost_ingest_channels` (team_id, page, per_page)
3. `mattermost_ingest_users` (page, per_page, in_team, not_in_team, in_channel, not_in_channel, in_group, without_team, active, inactive, role, sort)
4. `mattermost_ingest_posts` (channel_id, page, per_page, since, before, after, include_deleted)

## Guardrails

- Never print tokens, passwords or webhook secrets.
- Public or destructive actions need the requester's confirmation of the target and text.
- Report ids (and refusal codes) for every call.
