"""Native epistemic-graph ingestion for Mattermost records and messages.

All writes go through the ``agent_connector_sdk.ingest`` knowledge-ingest facade.
Nodes use canonical ``node_type`` and edges use canonical ``relationship``; nodes
and edges commit in one change set. Missing engine dependencies, rejected
records, conflicts, and transaction failures propagate as ``IngestError``.
"""

from __future__ import annotations

import logging
from typing import Any

from agent_connector_sdk.ingest import (
    ChangeSet,
    Document,
    Entity,
    IngestBinding,
    IngestError,
    KnowledgeIngest,
    Relationship,
    current_ingest,
)

logger = logging.getLogger("mattermost_mcp.kg")

_SOURCE = "mattermost-mcp"
_DOMAIN = "mattermost"
_BINDING = IngestBinding(connector=_SOURCE, stream=_DOMAIN)


def _to_entity(record: dict[str, Any]) -> Entity:
    return Entity(
        id=record.get("id"),
        node_type=record.get("node_type"),
        properties={
            k: v for k, v in record.items() if k not in ("id", "node_type")
        },
    )


def _to_relationship(record: dict[str, Any]) -> Relationship:
    properties = {
        k: v
        for k, v in record.items()
        if k not in ("source", "target", "relationship")
    }
    return Relationship(
        source=record["source"],
        target=record["target"],
        relationship=record["relationship"],
        properties=properties or None,
    )


async def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Write canonical typed nodes and relationships in one change set."""
    if not entities:
        raise IngestError("ingest_entities needs at least one entity")
    change_set = ChangeSet(
        entities=tuple(_to_entity(e) for e in entities),
        relationships=tuple(_to_relationship(r) for r in relationships or ()),
    )
    service = ingest or current_ingest()
    receipt = await service.submit(_BINDING, change_set)
    return {"nodes": receipt.affected_count, "edges": receipt.relationship_count}


def _to_document(record: dict[str, Any]) -> Document | None:
    text = record.get("text")
    if not text:
        return None
    return Document(
        id=record["id"],
        text=text,
        title=record.get("title"),
        source_uri=record.get("source_uri"),
        properties={
            k: v
            for k, v in record.items()
            if k not in ("id", "text", "title", "source_uri")
        },
    )


async def ingest_documents(
    documents: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Write text records as canonical Document nodes. A textless record is skipped."""
    mapped = [doc for doc in (_to_document(d) for d in documents) if doc is not None]
    if not mapped:
        raise IngestError("ingest_documents needs at least one document with text")
    change_set = ChangeSet(
        documents=tuple(mapped),
        relationships=tuple(_to_relationship(r) for r in relationships or ()),
    )
    service = ingest or current_ingest()
    receipt = await service.submit(_BINDING, change_set)
    return {"nodes": receipt.affected_count, "edges": receipt.relationship_count}


# --- domain mappers (records -> entity/document dicts) ---------------------------------


async def ingest_teams(
    teams: list[dict[str, Any]],
    *,
    ingest: KnowledgeIngest | None = None,
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
    return await ingest_entities(entities, ingest=ingest)


async def ingest_channels(
    channels: list[dict[str, Any]],
    *,
    ingest: KnowledgeIngest | None = None,
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
    return await ingest_entities(entities, relationships, ingest=ingest)


async def ingest_users(
    users: list[dict[str, Any]],
    *,
    ingest: KnowledgeIngest | None = None,
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
    return await ingest_entities(entities, ingest=ingest)


def _post_document(pid: str, message: str, cid: str | None, uid: str | None) -> dict[str, Any]:
    return {
        "id": f"mattermost:post:{pid}",
        "text": message,
        "title": message[:80],
        "messageType": "",
        "source_uri": f"mattermost:post:{pid}",
        "channel_id": cid,
        "user_id": uid,
        "externalToolId": str(pid),
    }


def _post_relationships(
    pid: str, cid: str | None, uid: str | None, root_id: str | None
) -> list[dict[str, Any]]:
    relationships: list[dict[str, Any]] = []
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
    if root_id and root_id != pid:
        relationships.append(
            {
                "source": f"mattermost:post:{pid}",
                "target": f"mattermost:post:{root_id}",
                "relationship": "repliesTo",
            }
        )
    return relationships


def _post_to_document(
    post: dict[str, Any], channel_id: str | None
) -> tuple[dict[str, Any], list[dict[str, Any]]] | None:
    pid = post.get("id")
    message = post.get("message")
    if not pid or not message:
        return None
    cid = post.get("channel_id") or channel_id
    uid = post.get("user_id")
    document = _post_document(pid, message, cid, uid)
    document["messageType"] = post.get("type") or ""
    relationships = _post_relationships(pid, cid, uid, post.get("root_id"))
    return document, relationships


async def ingest_posts(
    posts: list[dict[str, Any]],
    *,
    channel_id: str | None = None,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Map Mattermost post records → ``:Document`` message nodes (+ channel/author links).

    Accepts either a list of post dicts or the raw ``get_posts_for_channel`` payload
    shape (``{"order":[...], "posts":{id: post}}``) unwrapped by the caller. Empty /
    system-only messages are skipped.
    """
    documents: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for post in posts or []:
        mapped = _post_to_document(post, channel_id)
        if mapped is None:
            continue
        document, post_relationships = mapped
        documents.append(document)
        relationships.extend(post_relationships)
    return await ingest_documents(documents, relationships, ingest=ingest)
