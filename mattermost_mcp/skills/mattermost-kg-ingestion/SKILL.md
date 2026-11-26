---
name: mattermost-kg-ingestion
skill_type: skill
description: >-
  Natively ingest Mattermost into the medulla knowledge graph via the mattermost-mcp MCP server — push teams, channels and users as typed :Team/:Channel/:Person nodes, messages as :Document nodes, and file attachments as :MediaAsset blobs, in one ACID path. Use when the agent must make a Mattermost workspace searchable/queryable in the KG, or refresh its mirror.
license: MIT
tags: [mattermost, knowledge-graph, ingestion, kg, owl, mcp]
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---

# Mattermost Kg Ingestion

Scope: Natively ingest Mattermost into the medulla knowledge graph via the mattermost-mcp MCP server — push teams, channels and users as typed :Team/:Channel/:Person nodes, messages as :Document nodes, and file attachments as :MediaAsset blobs, in one ACID path. Use when the agent must make a Mattermost workspace searchable/queryable in the KG, or refresh its mirror. Do NOT use to read or post messages (mattermost-channel-messaging) or to provision teams and channels (mattermost-team-administration); prefer those.

Every step below is one typed tool call; there is no `action` or JSON-string argument. Resolve ids by name first, read before you change, and ask for approval before anything destructive.

## Steps

1. Confirm the server answers with `mattermost_get_ping`(get_server_status) and verify the response reports status OK.
2. Ingest the teams with `mattermost_ingest_teams`(page, per_page) and verify the response reports the number of teams written.
3. Ingest each team's channels with `mattermost_ingest_channels`(team_id, page, per_page) and verify the written count is not zero for a team that has channels.
4. Ingest the users with `mattermost_ingest_users`(page, per_page, active) and verify the written count in the response.
5. Ingest the messages with `mattermost_ingest_posts`(channel_id, page, per_page, since) and verify the written count, paging until a page returns no posts.

## Failure recovery

| Failure | Cause | Recovery |
|---|---|---|
| Request answers 401 or 403 | The credential is missing, expired or lacks the permission for this area | Confirm the acting identity with `mattermost_get_user`, then supply a token whose role covers the call and send it again with the corrected credential |
| An ingest call writes zero records | The page is past the last page, the since filter is too recent, or the team_id or channel_id is wrong | Repeat with page=0 and no since filter, and check the id with `mattermost_get_team_by_name`(team_name) or `mattermost_get_channel`(channel_id) |
| Ingest call is rejected for the graph target | The knowledge graph endpoint is not configured or not reachable from the connector | Check the connector's graph settings in its environment configuration and confirm the endpoint answers before ingesting again |

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
