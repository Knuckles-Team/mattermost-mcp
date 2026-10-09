"""Native epistemic-graph typed-node + document ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_documents`` seam and the Mattermost
record mappers against a fake ingest transport (no engine required), asserting the
submitted ``SourceRecord``/``SourceRelationship`` wire objects and the record→node
mapping.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import pytest
from agent_connector_sdk.ingest import IngestError, KnowledgeIngest

from mattermost_mcp.kg_ingest import (
    ingest_channels,
    ingest_documents,
    ingest_entities,
    ingest_posts,
    ingest_teams,
    ingest_users,
)


class _FakeTransport:
    def __init__(self) -> None:
        self.requests: list[Any] = []

    async def source_status(self, connector: str, stream: str) -> Any:
        return SimpleNamespace(accepted_checkpoint=None)

    async def submit(self, request: Any) -> Any:
        self.requests.append(request)
        return SimpleNamespace(
            affected_count=len(request.records),
            relationship_count=len(request.relationships),
        )

    async def store_blob(self, data: bytes) -> str:
        raise AssertionError("this connector's node/document ingestion carries no media")


@pytest.fixture
def ingest():
    transport = _FakeTransport()
    return KnowledgeIngest(transport, loop=None), transport


def _records_by_id(request: Any) -> dict[str, Any]:
    return {r.record_id: r for r in request.records}


def _node_type_of(record: Any) -> str:
    # mapping_reference: "manifest:<connector>#schema_mappings/<node_type>"
    return record.mapping_reference.rsplit("/", 1)[-1]


def _relationship_name_of(rel: Any) -> str:
    # relation_reference: "manifest:<connector>#resources/<type>/relations/<name>"
    return rel.relation_reference.rsplit("/", 1)[-1]


@pytest.mark.asyncio
async def test_ingest_entities_writes_nodes_and_edges(ingest):
    service, transport = ingest
    res = await ingest_entities(
        [
            {"id": "a", "node_type": "Channel", "name": "town-square"},
            {"id": "b", "node_type": "Team"},
        ],
        [{"source": "a", "target": "b", "relationship": "inTeam"}],
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 1}
    request = transport.requests[0]
    assert set(_records_by_id(request)) == {"a", "b"}
    rel = request.relationships[0]
    assert rel.source.record_id == "a"
    assert rel.target.record_id == "b"
    assert _relationship_name_of(rel) == "inTeam"


@pytest.mark.asyncio
async def test_ingest_teams_maps_team(ingest):
    service, transport = ingest
    res = await ingest_teams(
        [{"id": "T1", "name": "eng", "display_name": "Engineering", "type": "O"}],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 0}
    record = _records_by_id(transport.requests[0])["mattermost:team:T1"]
    assert _node_type_of(record) == "Team"
    assert record.payload["displayName"] == "Engineering"
    assert record.payload["teamType"] == "O"
    assert record.payload["externalToolId"] == "T1"


@pytest.mark.asyncio
async def test_ingest_channels_maps_channel_and_team_link(ingest):
    service, transport = ingest
    res = await ingest_channels(
        [
            {
                "id": "C1",
                "team_id": "T1",
                "name": "deploys",
                "display_name": "Deploys",
                "type": "O",
                "purpose": "ci/cd",
            }
        ],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 1}
    record = _records_by_id(transport.requests[0])["mattermost:channel:C1"]
    assert record.payload["channelType"] == "O"
    assert record.payload["purpose"] == "ci/cd"
    rel = transport.requests[0].relationships[0]
    assert rel.source.record_id == "mattermost:channel:C1"
    assert rel.target.record_id == "mattermost:team:T1"
    assert _relationship_name_of(rel) == "inTeam"


@pytest.mark.asyncio
async def test_ingest_users_maps_person_and_bot(ingest):
    service, transport = ingest
    res = await ingest_users(
        [
            {"id": "U1", "username": "alice", "first_name": "Alice", "last_name": "A"},
            {"id": "B1", "username": "ci-bot", "is_bot": True},
        ],
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 0}
    records = _records_by_id(transport.requests[0])
    assert _node_type_of(records["mattermost:user:U1"]) == "Person"
    assert records["mattermost:user:U1"].payload["name"] == "Alice A"
    assert _node_type_of(records["mattermost:user:B1"]) == "Bot"


@pytest.mark.asyncio
async def test_ingest_posts_maps_document_and_links(ingest):
    service, transport = ingest
    res = await ingest_posts(
        [
            {"id": "P1", "channel_id": "C1", "user_id": "U1", "message": "hello world"},
            {
                "id": "P2",
                "channel_id": "C1",
                "user_id": "U1",
                "message": "reply",
                "root_id": "P1",
            },
            {"id": "P3", "channel_id": "C1", "user_id": "U1", "message": ""},
        ],
        ingest=service,
    )
    # empty-message post skipped; 2 documents, links: 2 channel + 2 author + 1 reply
    assert res == {"nodes": 2, "edges": 5}
    records = _records_by_id(transport.requests[0])
    assert records["mattermost:post:P1"].payload["text"] == "hello world"
    rels = {
        (rel.source.record_id, rel.target.record_id, _relationship_name_of(rel))
        for rel in transport.requests[0].relationships
    }
    assert ("mattermost:post:P1", "mattermost:channel:C1", "postedInChannel") in rels
    assert ("mattermost:post:P1", "mattermost:user:U1", "authoredBy") in rels
    assert ("mattermost:post:P2", "mattermost:post:P1", "repliesTo") in rels


@pytest.mark.asyncio
async def test_ingest_documents_skips_textless(ingest):
    service, transport = ingest
    res = await ingest_documents(
        [{"id": "d1", "text": "body"}, {"id": "d2"}],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 0}
    assert list(_records_by_id(transport.requests[0])) == ["d1"]


@pytest.mark.asyncio
async def test_empty_entities_is_rejected(ingest):
    service, _transport = ingest
    with pytest.raises(IngestError, match="at least one entity"):
        await ingest_entities([], ingest=service)


@pytest.mark.asyncio
async def test_all_textless_documents_is_rejected(ingest):
    service, _transport = ingest
    with pytest.raises(IngestError, match="at least one document"):
        await ingest_documents([{"id": "d2"}], ingest=service)
