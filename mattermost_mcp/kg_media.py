"""Native epistemic-graph blob ingestion for Mattermost file attachments.

CONCEPT:AU-KG.ingest.list-durable-media. Files uploaded to Mattermost posts are stored
as content-addressed **blobs** with a ``:MediaAsset`` graph node (carrying the file-info
metadata), via the ``agent_connector_sdk.ingest`` knowledge-ingest facade. This makes the
raw attachment bytes — not just a file id — durable, deduped and queryable inside the
knowledge graph.

Missing engine capability, empty bytes, and storage failures are explicit ``IngestError``
failures. Pairs with :mod:`mattermost_mcp.kg_ingest` (typed nodes + message documents).
"""

from __future__ import annotations

import hashlib
import logging
from typing import Any

from agent_connector_sdk.ingest import (
    ChangeSet,
    IngestBinding,
    IngestError,
    KnowledgeIngest,
    MediaAsset,
    current_ingest,
)

logger = logging.getLogger("mattermost_mcp.kg_media")

_SOURCE = "mattermost-mcp"
_DOMAIN = "mattermost"
_BINDING = IngestBinding(connector=_SOURCE, stream=_DOMAIN)

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

_MIME_PREFIX_TO_MEDIA_TYPE = (
    ("image", "image"),
    ("video", "video"),
    ("audio", "audio"),
)


def _media_type_for_mime(mime: str) -> str:
    for prefix, media_type in _MIME_PREFIX_TO_MEDIA_TYPE:
        if mime.startswith(prefix):
            return media_type
    return "file"


async def ingest_file_attachment(
    data: bytes | None,
    *,
    info: dict[str, Any] | None = None,
    source: str = _SOURCE,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, Any]:
    """Store a Mattermost attachment as a blob + ``:MediaAsset`` in the knowledge graph.

    ``data``: raw file bytes (e.g. from ``get_file``). ``info``: the Mattermost FileInfo
    record. Returns ``{asset_id, digest, size_bytes, media_type}``; invalid input or a
    storage failure raises :class:`IngestError`. ``ingest`` may be injected in tests.
    """
    if not data:
        raise IngestError("native media ingest requires non-empty bytes")

    info = info or {}
    mime = info.get("mime_type") or "application/octet-stream"
    media_type = _media_type_for_mime(mime)
    name = info.get("name") or info.get("id") or "attachment"

    digest = hashlib.sha256(data).hexdigest()
    asset_id = f"blob:{digest}"
    extra = {k: info[k] for k in _INFO_FIELDS if info.get(k) is not None}
    extra["media_type"] = media_type
    extra["source"] = source

    asset = MediaAsset(data=data, mime_type=mime, id=asset_id, name=name, properties=extra)
    change_set = ChangeSet(media=(asset,))
    service = ingest or current_ingest()

    try:
        await service.submit(_BINDING, change_set)
    except IngestError:
        raise
    except Exception as exc:  # noqa: BLE001 - preserve retryable cause privately
        raise IngestError("native media ingest transaction failed") from exc

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
