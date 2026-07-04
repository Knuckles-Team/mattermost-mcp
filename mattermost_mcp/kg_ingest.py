"""Native epistemic-graph ingestion for Mattermost records.

CONCEPT:AU-KG.ingest.enterprise-source-extractor. This is the record-source leg of
mattermost-mcp: the connector natively pushes its data into the ONE epistemic-graph
engine, in every modality the domain has:

* **typed nodes** — teams/channels/people → OWL ``:Team`` / ``:Channel`` / ``:Person``
  nodes + membership links (``ingest_entities`` / ``ingest_teams`` / ``ingest_channels`` /
  ``ingest_users``)
* **documents** — channel messages → ``:Document`` nodes carrying the post text +
  ``:postedInChannel`` / ``:authoredBy`` links (``ingest_posts``); the hub chunks/embeds
  them for semantic search

Blob attachments have their own leg in :mod:`mattermost_mcp.kg_media`.

Everything rides the **lightweight engine client** (``GraphComputeEngine()._client`` +
``txn``) via the shared ``agent_utilities...native_ingest`` primitive when it is present;
otherwise a self-contained txn fallback runs the same write dance. Both are entirely
dependency-/engine-guarded: with no KG stack or no reachable engine every entry point
**no-ops** (returns ``None``), so the connector keeps working with zero KG infrastructure.
Node ids follow ``mattermost:<class>:<externalId>``; ``type`` matches the classes federated
by :mod:`mattermost_mcp.ontology`.
"""

from __future__ import annotations

import logging
import time
from typing import Any

logger = logging.getLogger("mattermost_mcp.kg")

_SOURCE = "mattermost-mcp"
_DOMAIN = "mattermost"
_DEFAULT_GRAPH = "__commons__"


def _client() -> tuple[Any | None, str]:
    """Return ``(engine_client, graph_name)`` or ``(None, "")`` when unavailable."""
    # Prefer the shared native-ingest primitive's client resolver when present.
    try:
        from agent_utilities.knowledge_graph.memory.native_ingest import native_client

        return native_client()
    except Exception as e:  # noqa: BLE001 — primitive not installed yet; self-contained path
        logger.debug("native_ingest primitive absent (%s); using local resolver", e)
    try:
        from agent_utilities.knowledge_graph.core.graph_compute import (
            GraphComputeEngine,
        )
    except Exception as e:  # noqa: BLE001 — KG stack absent
        logger.debug("KG ingest unavailable (import): %s", e)
        return None, ""
    try:
        engine = GraphComputeEngine()
        client = getattr(engine, "_client", None)
        if client is None:
            return None, ""
        return client, (getattr(engine, "graph_name", None) or _DEFAULT_GRAPH)
    except Exception as e:  # noqa: BLE001 — engine unreachable
        logger.debug("KG ingest: engine unreachable: %s", e)
        return None, ""


def _write_nodes(
    client: Any,
    graph: str,
    nodes: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None,
) -> dict[str, int] | None:
    """Stamp provenance, MERGE the nodes in one txn, then add the edges."""
    nodes = [n for n in nodes if n.get("id")]
    if not nodes:
        return None
    try:
        txn = client.txn.begin(graph=graph)
        for node in nodes:
            props = {k: v for k, v in node.items() if k != "id" and v is not None}
            props.setdefault("source", _SOURCE)
            props.setdefault("domain", _DOMAIN)
            client.txn.add_node(txn, node["id"], props)
        committed = client.txn.commit(txn)
    except Exception as e:  # noqa: BLE001 — engine/txn failure is non-fatal
        logger.warning("KG ingest: txn failed: %s", e)
        return None
    if not committed:
        logger.warning("KG ingest: txn not committed (conflict)")
        return None

    edges = 0
    for rel in relationships or []:
        try:
            client.edges.add(
                rel["source"], rel["target"], {"type": rel.get("type", "RELATED")}
            )
            edges += 1
        except Exception as e:  # noqa: BLE001 — pure edge link, best-effort
            logger.debug("KG ingest: edge skipped: %s", e)

    logger.info("KG ingest: wrote %d nodes, %d edges", len(nodes), edges)
    return {"nodes": len(nodes), "edges": edges}


def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write typed OWL nodes (+ edges) into epistemic-graph via the fast engine client.

    ``entities``: ``[{"id":..., "type":<owl:Class>, ...props}]``.
    ``relationships``: ``[{"source":id, "target":id, "type":rel}]``.
    Returns ``{"nodes":n, "edges":m}`` or ``None``. ``client``/``graph`` may be
    injected (tests); otherwise resolved on demand.
    """
    entities = [e for e in (entities or []) if e.get("id")]
    if not entities:
        return None
    if client is None:
        client, graph = _client()
    if client is None:
        return None
    return _write_nodes(client, graph or _DEFAULT_GRAPH, entities, relationships)


def ingest_documents(
    documents: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write text records as ``:Document`` nodes (semantic-search fodder).

    Each doc: ``{"id":..., "text":..., "title"?:..., "source_uri"?:..., ...props}``.
    Returns ``{"nodes":n, "edges":m}`` or ``None``.
    """
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    nodes: list[dict[str, Any]] = []
    for doc in documents or []:
        did = doc.get("id")
        text = doc.get("text") or doc.get("content")
        if not did or not text:
            continue
        node = {k: v for k, v in doc.items() if k not in ("content",) and v is not None}
        node["id"] = did
        node["type"] = "Document"
        node["text"] = text
        node.setdefault("created_at", now)
        nodes.append(node)
    if not nodes:
        return None
    if client is None:
        client, graph = _client()
    if client is None:
        return None
    return _write_nodes(client, graph or _DEFAULT_GRAPH, nodes, relationships)


# --- domain mappers (records -> entity/document dicts) ---------------------------------


def ingest_teams(
    teams: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map Mattermost team records → ``:Team`` nodes and ingest."""
    entities: list[dict[str, Any]] = []
    for team in teams or []:
        tid = team.get("id")
        if not tid:
            continue
        entities.append(
            {
                "id": f"mattermost:team:{tid}",
                "type": "Team",
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
) -> dict[str, int] | None:
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
                "type": "Channel",
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
                    "type": "inTeam",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_users(
    users: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
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
                "type": "Bot" if is_bot else "Person",
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
) -> dict[str, int] | None:
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
                    "type": "postedInChannel",
                }
            )
        if uid:
            relationships.append(
                {
                    "source": f"mattermost:post:{pid}",
                    "target": f"mattermost:user:{uid}",
                    "type": "authoredBy",
                }
            )
        root_id = post.get("root_id")
        if root_id and root_id != pid:
            relationships.append(
                {
                    "source": f"mattermost:post:{pid}",
                    "target": f"mattermost:post:{root_id}",
                    "type": "repliesTo",
                }
            )
    return ingest_documents(documents, relationships, client=client, graph=graph)
