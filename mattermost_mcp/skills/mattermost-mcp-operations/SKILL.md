---
name: mattermost-mcp-operations
skill_type: skill
description: >-
  Operate mattermost-mcp through its governed MCP and Arbora capabilities, including mattermost channel messaging, mattermost kg ingestion, mattermost team administration. Use when a request requires this provider's read, change, automation, ingestion, troubleshooting, or evidence workflows.
---

# Mattermost Mcp Operations

Every step below is one typed tool call; there is no `action` or JSON-string argument. Resolve ids by name first, read before you change, and ask for approval before anything destructive.

## Verify connection

Confirm the server answers and the credential identifies the acting user.

1. `mattermost_get_ping` (get_server_status, device_id, use_rest_semantics)
2. `mattermost_get_user` (user_id)

## Guardrails

- Never print tokens, passwords or webhook secrets.
- Public or destructive actions need the requester's confirmation of the target and text.
- Report ids (and refusal codes) for every call.

## Finding the right tool

The workflows are in mattermost-channel-messaging, mattermost-team-administration and mattermost-kg-ingestion. Every other
Mattermost operation is listed with its summary in the area skills mattermost-api-posts-and-files, mattermost-api-channels,
mattermost-api-teams-and-groups, mattermost-api-users-and-sessions, mattermost-api-compliance-governance and
mattermost-api-system-and-integrations. The full list by REST area is in [the catalog](references/catalog.md).
