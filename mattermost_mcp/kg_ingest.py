"""Native epistemic-graph ingestion for Mattermost records and messages.

All writes use the required ``agent_utilities.knowledge_graph.memory.native_ingest``
primitive. Nodes use canonical ``node_type`` and edges use canonical ``relationship``;
nodes and edges commit in one native transaction. Missing engine dependencies, rejected
records, conflicts, and transaction failures propagate as ``NativeIngestError``.
"""

from __future__ import annotations

import logging
from typing import Any

from agent_utilities.knowledge_graph.memory.native_ingest import (
    ingest_documents as _native_ingest_documents,
)
from agent_utilities.knowledge_graph.memory.native_ingest import (
    ingest_entities as _native_ingest_entities,
)

logger = logging.getLogger("mattermost_mcp.kg")

_SOURCE = "mattermost-mcp"
_DOMAIN = "mattermost"


def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Write canonical typed nodes and relationships in one native transaction."""
    return _native_ingest_entities(
        entities, relationships, source=source, domain=domain, client=client, graph=graph
    )


def ingest_documents(
    documents: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Write text records as canonical Document nodes."""
    return _native_ingest_documents(
        documents,
        relationships,
        source=source,
        domain=domain,
        client=client,
        graph=graph,
    )


# --- domain mappers (records -> entity/document dicts) ---------------------------------


def ingest_teams(
    teams: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map Mattermost team records → ``:Team`` nodes and ingest."""
    entities: list[dict[str, Any]] = []
    for team in teams or []:
        tid = team.get("id")
        if not tid:
            continue
        entities.append(
            {
                "id": f"mattermost:team:{tid}",
                "node_type": "Team",
                "name": team.get("name"),
                "displayName": team.get("display_name"),
                "teamType": team.get("type"),
                "description": team.get("description"),
                "externalToolId": str(tid),
            }
        )
    return ingest_entities(entities, client=client, graph=graph)


def ingest_channels(
    channels: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map Mattermost channel records → ``:Channel`` nodes (+ ``:inTeam`` links)."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for ch in channels or []:
        cid = ch.get("id")
        if not cid:
            continue
        entities.append(
            {
                "id": f"mattermost:channel:{cid}",
                "node_type": "Channel",
                "name": ch.get("name"),
                "displayName": ch.get("display_name"),
                "channelType": ch.get("type"),
                "purpose": ch.get("purpose"),
                "header": ch.get("header"),
                "externalToolId": str(cid),
            }
        )
        team_id = ch.get("team_id")
        if team_id:
            relationships.append(
                {
                    "source": f"mattermost:channel:{cid}",
                    "target": f"mattermost:team:{team_id}",
                    "relationship": "inTeam",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_users(
    users: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map Mattermost user records → shared ``:Person`` (or ``:Bot``) nodes."""
    entities: list[dict[str, Any]] = []
    for user in users or []:
        uid = user.get("id")
        if not uid:
            continue
        is_bot = bool(user.get("is_bot"))
        full = " ".join(
            p for p in (user.get("first_name"), user.get("last_name")) if p
        ).strip()
        entities.append(
            {
                "id": f"mattermost:user:{uid}",
                "node_type": "Bot" if is_bot else "Person",
                "username": user.get("username"),
                "name": full or user.get("nickname") or user.get("username"),
                "email": user.get("email"),
                "externalToolId": str(uid),
            }
        )
    return ingest_entities(entities, client=client, graph=graph)


def ingest_posts(
    posts: list[dict[str, Any]],
    *,
    channel_id: str | None = None,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map Mattermost post records → ``:Document`` message nodes (+ channel/author links).

    Accepts either a list of post dicts or the raw ``get_posts_for_channel`` payload
    shape (``{"order":[...], "posts":{id: post}}``) unwrapped by the caller. Empty /
    system-only messages are skipped.
    """
    documents: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for post in posts or []:
        pid = post.get("id")
        message = post.get("message")
        if not pid or not message:
            continue
        cid = post.get("channel_id") or channel_id
        uid = post.get("user_id")
        documents.append(
            {
                "id": f"mattermost:post:{pid}",
                "text": message,
                "title": message[:80],
                "messageType": post.get("type") or "",
                "source_uri": f"mattermost:post:{pid}",
                "channel_id": cid,
                "user_id": uid,
                "externalToolId": str(pid),
            }
        )
        if cid:
            relationships.append(
                {
                    "source": f"mattermost:post:{pid}",
                    "target": f"mattermost:channel:{cid}",
                    "relationship": "postedInChannel",
                }
            )
        if uid:
            relationships.append(
                {
                    "source": f"mattermost:post:{pid}",
                    "target": f"mattermost:user:{uid}",
                    "relationship": "authoredBy",
                }
            )
        root_id = post.get("root_id")
        if root_id and root_id != pid:
            relationships.append(
                {
                    "source": f"mattermost:post:{pid}",
                    "target": f"mattermost:post:{root_id}",
                    "relationship": "repliesTo",
                }
            )
    return ingest_documents(documents, relationships, client=client, graph=graph)
