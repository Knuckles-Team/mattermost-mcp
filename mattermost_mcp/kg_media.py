"""Native epistemic-graph blob ingestion for Mattermost file attachments.

CONCEPT:AU-KG.ingest.list-durable-media. Files uploaded to Mattermost posts are stored
as content-addressed **blobs** with a ``:MediaAsset`` graph node (carrying the file-info
metadata) in ONE cross-modal ACID commit, via the agent-utilities ``MediaStore``. This
makes the raw attachment bytes — not just a file id — durable, deduped and queryable
inside the knowledge graph, and lets a message ``:Document`` link to it via ``:hasAttachment``.

The authoritative ``native_ingest.media_store`` dependency is required. Missing engine
capability, empty bytes, and storage failures are explicit ``NativeIngestError`` failures.
Pairs with :mod:`mattermost_mcp.kg_ingest` (typed nodes + message documents).
"""

from __future__ import annotations

import logging
from typing import Any

from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError
from agent_utilities.knowledge_graph.memory.native_ingest import (
    media_store as _native_media_store,
)

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


def media_store() -> Any:
    """Return the authoritative native media store."""
    return _native_media_store()


def ingest_file_attachment(
    data: bytes | None,
    *,
    info: dict[str, Any] | None = None,
    source: str = _SOURCE,
    store: Any | None = None,
) -> dict[str, Any]:
    """Store a Mattermost attachment as a blob + ``:MediaAsset`` in the knowledge graph.

    ``data``: raw file bytes (e.g. from ``get_file``). ``info``: the Mattermost FileInfo
    record. Returns ``{asset_id, digest, size_bytes, media_type}``; invalid input or a
    storage failure raises :class:`NativeIngestError`. ``store`` may be injected in tests.
    """
    if not data:
        raise NativeIngestError("native media ingest requires non-empty bytes")
    st = store if store is not None else media_store()

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
    except Exception as exc:  # noqa: BLE001 - preserve retryable cause privately
        raise NativeIngestError("native media ingest transaction failed") from exc
    if stored is None:
        raise NativeIngestError("native media ingest was not committed")

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
