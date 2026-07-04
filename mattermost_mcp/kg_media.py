"""Native epistemic-graph blob ingestion for Mattermost file attachments.

CONCEPT:AU-KG.ingest.list-durable-media. Files uploaded to Mattermost posts are stored
as content-addressed **blobs** with a ``:MediaAsset`` graph node (carrying the file-info
metadata) in ONE cross-modal ACID commit, via the agent-utilities ``MediaStore``. This
makes the raw attachment bytes — not just a file id — durable, deduped and queryable
inside the knowledge graph, and lets a message ``:Document`` link to it via ``:hasAttachment``.

Entirely best-effort and dependency-guarded: if agent-utilities' KG stack or a live engine
is absent, every entry point **no-ops** (returns ``None``), so the connector keeps working
with zero KG infrastructure. Pairs with :mod:`mattermost_mcp.kg_ingest` (typed nodes +
message documents).
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger("mattermost_mcp.kg_media")

_SOURCE = "mattermost-mcp"
_DOMAIN = "mattermost"

# Mattermost FileInfo keys worth carrying onto the :MediaAsset node.
_INFO_FIELDS = (
    "id",
    "name",
    "extension",
    "size",
    "mime_type",
    "post_id",
    "user_id",
    "channel_id",
    "create_at",
)


def media_store() -> Any | None:
    """Return a :class:`MediaStore` over a live engine, or ``None`` when unavailable."""
    # Prefer the shared native-ingest primitive when installed.
    try:
        from agent_utilities.knowledge_graph.memory.native_ingest import (
            media_store as _shared_store,
        )

        return _shared_store()
    except Exception as e:  # noqa: BLE001 — primitive absent; self-contained path
        logger.debug("native_ingest.media_store absent (%s); local resolver", e)
    try:
        from agent_utilities.knowledge_graph.core.graph_compute import (
            GraphComputeEngine,
        )
        from agent_utilities.knowledge_graph.memory.media_store import MediaStore
    except Exception as e:  # noqa: BLE001 — KG stack absent
        logger.debug("KG media ingest unavailable (import): %s", e)
        return None
    try:
        engine = GraphComputeEngine()
        if getattr(engine, "_client", None) is None:
            logger.debug("KG media ingest: no live engine client")
            return None
        return MediaStore(engine)
    except Exception as e:  # noqa: BLE001 — no reachable engine
        logger.debug("KG media ingest: engine unreachable: %s", e)
        return None


def ingest_file_attachment(
    data: bytes | None,
    *,
    info: dict[str, Any] | None = None,
    source: str = _SOURCE,
    store: Any | None = None,
) -> dict[str, Any] | None:
    """Store a Mattermost attachment as a blob + ``:MediaAsset`` in the knowledge graph.

    ``data``: raw file bytes (e.g. from ``get_file``). ``info``: the Mattermost FileInfo
    record. Returns ``{asset_id, digest, size_bytes, media_type}`` on success, or ``None``
    when there is no engine / no bytes / the store failed (never raises). ``store`` may be
    injected (tests); otherwise one is built on demand.
    """
    if not data:
        return None
    st = store if store is not None else media_store()
    if st is None:
        return None

    info = info or {}
    mime = info.get("mime_type") or "application/octet-stream"
    if mime.startswith("image"):
        media_type = "image"
    elif mime.startswith("video"):
        media_type = "video"
    elif mime.startswith("audio"):
        media_type = "audio"
    else:
        media_type = "file"

    extra = {k: info[k] for k in _INFO_FIELDS if info.get(k) is not None}
    name = info.get("name") or info.get("id") or "attachment"

    try:
        stored = st.store_media(
            data,
            media_type=media_type,
            mime_type=mime,
            source=source,
            name=name,
            extra=extra,
        )
    except Exception as e:  # noqa: BLE001 — engine/store failure is non-fatal
        logger.warning("KG media ingest: store_media failed: %s", e)
        return None
    if stored is None:
        return None

    asset_id = getattr(stored, "asset_id", None)
    digest = getattr(stored, "digest", "") or ""
    logger.info(
        "KG media ingest: stored %s (%s bytes) as asset %s digest %s",
        name,
        len(data),
        asset_id,
        digest[:16],
    )
    return {
        "asset_id": asset_id,
        "digest": digest,
        "size_bytes": len(data),
        "media_type": media_type,
    }
