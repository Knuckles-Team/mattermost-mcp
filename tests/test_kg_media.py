"""Native epistemic-graph blob ingestion for Mattermost attachments — Wire-First coverage.

Exercises ``ingest_file_attachment`` against a fake ingest transport (no engine
required), asserting the stored blob + media-type derivation and strict input
failures.
CONCEPT:AU-KG.ingest.list-durable-media.
"""

from __future__ import annotations

import hashlib
from types import SimpleNamespace
from typing import Any

import pytest
from agent_connector_sdk.ingest import IngestError, KnowledgeIngest

from mattermost_mcp.kg_media import ingest_file_attachment


class _FakeTransport:
    def __init__(self) -> None:
        self.requests: list[Any] = []
        self.stored: list[bytes] = []

    async def source_status(self, connector: str, stream: str) -> Any:
        return SimpleNamespace(accepted_checkpoint=None)

    async def submit(self, request: Any) -> Any:
        self.requests.append(request)
        return SimpleNamespace(
            affected_count=len(request.records),
            relationship_count=len(request.relationships),
        )

    async def store_blob(self, data: bytes) -> str:
        self.stored.append(data)
        return hashlib.sha256(data).hexdigest()


class _FailingTransport(_FakeTransport):
    async def store_blob(self, data: bytes) -> str:
        raise RuntimeError("unavailable")


@pytest.fixture
def ingest():
    transport = _FakeTransport()
    return KnowledgeIngest(transport, loop=None), transport


@pytest.mark.asyncio
async def test_ingest_attachment_stores_blob_and_derives_type(ingest):
    service, transport = ingest
    data = b"\x89PNG payload"
    res = await ingest_file_attachment(
        data,
        info={
            "id": "F1",
            "name": "diagram.png",
            "mime_type": "image/png",
            "post_id": "P1",
            "size": 12,
        },
        ingest=service,
    )
    assert res is not None
    assert res["digest"] == hashlib.sha256(data).hexdigest()
    assert res["asset_id"] == f"blob:{res['digest']}"
    assert res["media_type"] == "image"
    assert res["size_bytes"] == len(data)
    assert transport.stored == [data]
    record = transport.requests[0].records[0]
    assert record.payload["mime_type"] == "image/png"
    assert record.payload["source"] == "mattermost-mcp"
    assert record.payload["name"] == "diagram.png"
    assert record.payload["post_id"] == "P1"


@pytest.mark.asyncio
async def test_ingest_attachment_defaults_to_file_type(ingest):
    service, _transport = ingest
    res = await ingest_file_attachment(
        b"data",
        info={"id": "F2", "name": "notes.txt", "mime_type": "text/plain"},
        ingest=service,
    )
    assert res["media_type"] == "file"


@pytest.mark.asyncio
async def test_ingest_attachment_rejects_empty_bytes(ingest):
    service, _transport = ingest
    with pytest.raises(IngestError, match="non-empty bytes"):
        await ingest_file_attachment(b"", info={"id": "F3"}, ingest=service)
    with pytest.raises(IngestError, match="non-empty bytes"):
        await ingest_file_attachment(None, ingest=service)


@pytest.mark.asyncio
async def test_ingest_attachment_propagates_store_failure():
    transport = _FailingTransport()
    service = KnowledgeIngest(transport, loop=None)
    with pytest.raises(IngestError, match="did not commit"):
        await ingest_file_attachment(b"data", info={"id": "F4"}, ingest=service)
