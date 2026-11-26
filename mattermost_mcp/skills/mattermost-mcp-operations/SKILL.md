---
name: mattermost-mcp-operations
skill_type: skill
description: >-
  Operate mattermost-mcp through its governed MCP and Arbora capabilities, including mattermost channel messaging, mattermost kg ingestion, mattermost team administration. Use when a request requires this provider's read, change, automation, ingestion, troubleshooting, or evidence workflows.
---

# Mattermost Mcp Operations

Every step below is one typed tool call; there is no `action` or JSON-string argument. Resolve ids by name first, read before you change, and ask for approval before anything destructive.

## Steps

1. Confirm the server answers with `mattermost_get_ping`(get_server_status) and verify the response reports status OK.
2. Identify the acting user with `mattermost_get_user`(user_id) and verify the username is the account intended for this work.
3. Pick the workflow skill that covers the request (mattermost-channel-messaging, mattermost-team-administration or mattermost-kg-ingestion), or look the operation up in `references/catalog.md` and verify the tool name exists there.
4. Run the read-only tool first, for example `mattermost_get_user_by_username`(username), and verify the returned ids match the request before any change is made.
5. Read the changed object back with `mattermost_get_post`(post_id) once the requester confirmed the change, and verify the new content is visible.

## Failure recovery

| Failure | Cause | Recovery |
|---|---|---|
| Request answers 401 or 403 | The credential is missing, expired or lacks the permission for this area | Confirm the acting identity with `mattermost_get_user`, then supply a token whose role covers the call and send it again with the corrected credential |
| The tool name is not found | The operation belongs to a different area skill or the name is misspelled | Search `references/catalog.md` for the operation and load the area skill that lists it |
| A destructive tool is refused | confirm=true was not supplied | Obtain the requester's approval of the target and call the tool again with confirm=true |

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
