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


def media_store(*args: object, **kwargs: object) -> object:
    """Return the authoritative native media store.

    SDK-GAP: Always raises now; see KnowledgeGraphIngestUnavailable.
    """
    _kg_unavailable("media_store")


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


def _store_attachment(*args: object, **kwargs: object) -> object:
    """Was: _store_attachment.

    SDK-GAP: Always raises now; see KnowledgeGraphIngestUnavailable.
    """
    _kg_unavailable("_store_attachment")


def ingest_file_attachment(*args: object, **kwargs: object) -> object:
    """Store a Mattermost attachment as a blob + ``:MediaAsset`` in the knowledge graph.

    SDK-GAP: Always raises now; see KnowledgeGraphIngestUnavailable.
    """
    _kg_unavailable("ingest_file_attachment")


class KnowledgeGraphIngestUnavailable(RuntimeError):
    """Direct-to-graph ingestion is unavailable from this connector.

    SDK-GAP (EH-48x, /var/tmp/l9/finish/au-decon-G4c/SDK-GAPS.md): raised in
    place of the old ``agent_utilities.knowledge_graph`` native-ingest call --
    agent-connector-sdk has no facade over EG's typed ingestion protocol yet,
    and the fleet precedent (agents/world-reference-mcp) moves direct-to-graph
    delivery to agent_connector_sdk.runner/sinks at the deployment layer, out
    of connector scope.
    """


def _kg_unavailable(name: str) -> None:
    raise KnowledgeGraphIngestUnavailable(
        f"{name}: direct-to-graph ingestion moved out of connector code "
        "(agent-utilities removed); no agent-connector-sdk facade exists yet "
        "-- see SDK-GAPS.md"
    )
