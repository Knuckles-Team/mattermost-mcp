"""Native epistemic-graph blob ingestion for Mattermost attachments — Wire-First coverage.

Exercises ``ingest_file_attachment`` with a fake MediaStore (no engine required),
asserting the store_media call, media-type derivation, and strict input failures.
CONCEPT:AU-KG.ingest.list-durable-media.
"""

from __future__ import annotations

import pytest
from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError

from mattermost_mcp.kg_media import ingest_file_attachment


class _Stored:
    def __init__(self, asset_id, digest):
        self.asset_id = asset_id
        self.digest = digest


class _FakeStore:
    def __init__(self):
        self.calls = []

    def store_media(self, data, **kwargs):
        self.calls.append((data, kwargs))
        return _Stored("asset-1", "deadbeefcafebabe0000")


def test_ingest_attachment_stores_blob_and_derives_type():
    store = _FakeStore()
    res = ingest_file_attachment(
        b"\x89PNG payload",
        info={
            "id": "F1",
            "name": "diagram.png",
            "mime_type": "image/png",
            "post_id": "P1",
            "size": 12,
        },
        store=store,
    )
    assert res is not None
    assert res["asset_id"] == "asset-1"
    assert res["media_type"] == "image"
    assert res["size_bytes"] == len(b"\x89PNG payload")
    # store_media received the domain metadata + source
    data, kwargs = store.calls[0]
    assert kwargs["mime_type"] == "image/png"
    assert kwargs["source"] == "mattermost-mcp"
    assert kwargs["name"] == "diagram.png"
    assert kwargs["extra"]["post_id"] == "P1"


def test_ingest_attachment_defaults_to_file_type():
    store = _FakeStore()
    res = ingest_file_attachment(
        b"data",
        info={"id": "F2", "name": "notes.txt", "mime_type": "text/plain"},
        store=store,
    )
    assert res["media_type"] == "file"


def test_ingest_attachment_rejects_empty_bytes():
    with pytest.raises(NativeIngestError, match="non-empty bytes"):
        ingest_file_attachment(b"", info={"id": "F3"}, store=_FakeStore())
    with pytest.raises(NativeIngestError, match="non-empty bytes"):
        ingest_file_attachment(None, store=_FakeStore())


def test_ingest_attachment_propagates_store_failure():
    class _FailingStore:
        def store_media(self, *_args, **_kwargs):
            raise RuntimeError("unavailable")

    with pytest.raises(NativeIngestError, match="transaction failed"):
        ingest_file_attachment(b"data", info={"id": "F4"}, store=_FailingStore())
