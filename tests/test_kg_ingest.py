"""Native epistemic-graph typed-node + document ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_documents`` seam and the Mattermost
record mappers with a fake engine client (no engine required), asserting the txn
add_node/commit + edge calls and the record→node mapping.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from typing import Any

import msgpack
import pytest
from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError
from agent_utilities.security.brain_context import ActorContext, use_actor
from agent_utilities.models.company_brain import ActorType
from agent_utilities.knowledge_graph.core.session import GraphSession, use_session

from mattermost_mcp.kg_ingest import (
    ingest_channels,
    ingest_documents,
    ingest_entities,
    ingest_posts,
    ingest_teams,
    ingest_users,
)


@pytest.fixture(autouse=True)
def _governed_session():
    actor = ActorContext(
        actor_id="subject:opaque:synthetic",
        actor_type=ActorType.AUTOMATED_SERVICE,
        roles=(),
        tenant_id="tenant:opaque:synthetic",
        authenticated=True,
    )
    session = GraphSession(
        actor=actor,
        tenant=actor.tenant_id,
        scopes=frozenset({"kg:write"}),
        graph="graph:opaque:synthetic",
        policy_version="policy:opaque:synthetic",
        audience="epistemic-graph",
    )
    with use_actor(actor), use_session(session):
        yield


class _FakeNodes:
    def __init__(self) -> None:
        self.values: dict[str, dict[str, Any]] = {}

    def properties(self, node_id: str) -> dict[str, Any] | None:
        return self.values.get(node_id)

    def list(self) -> list[tuple[str, dict[str, Any]]]:
        return list(self.values.items())


class _FakeChanges:
    def __init__(self, nodes: _FakeNodes) -> None:
        self.nodes = nodes
        self.edges: list[tuple[str, str, dict[str, Any]]] = []
        self.applied: list[dict[str, Any]] = []
        self.records: dict[str, dict[str, Any]] = {}
        self.versions: dict[str, dict[str, Any]] = {}

    def get(self, envelope_id: str) -> dict[str, Any] | None:
        return self.records.get(envelope_id)

    def content_version(self, object_id: str) -> dict[str, Any] | None:
        return self.versions.get(object_id)

    def cursor(self, _source: str, _partition: str = "") -> None:
        return None

    def apply(self, envelope: dict[str, Any]) -> dict[str, Any]:
        self.applied.append(envelope)
        mutation = envelope["mutation"]
        for operation in mutation["operations"]:
            method = operation["method"]
            params = method["params"]
            properties = msgpack.unpackb(params["properties_msgpack"], raw=False)
            if method["method"] == "AddNode":
                self.nodes.values[params["node_id"]] = properties
            elif method["method"] == "AddEdge":
                self.edges.append(
                    (params["source_id"], params["target_id"], properties)
                )
        version = envelope["content_version"]
        self.versions[version["object_id"]] = version
        self.records[envelope["envelope_id"]] = envelope
        return {
            "batch_id": mutation["batch_id"],
            "replayed": False,
            "projection_pending": False,
        }


class _FakeRdf:
    def validate_shacl(self, _shapes: str, _data_graph: str) -> dict[str, Any]:
        return {"conforms": True, "results": []}


class _FakeClient:
    def __init__(self) -> None:
        self.nodes = _FakeNodes()
        self.changes = _FakeChanges(self.nodes)
        self.rdf = _FakeRdf()

    @staticmethod
    def supports(operation: str) -> bool:
        return operation == "ApplyChangeEnvelope"


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "node_type": "Channel", "name": "town-square"},
            {"id": "b", "node_type": "Team"},
        ],
        [{"source": "a", "target": "b", "relationship": "inTeam"}],
        client=c,
    )
    assert res == {"nodes": 2, "edges": 1}
    assert len(c.changes.applied) == 1
    assert set(c.nodes.values) == {"a", "b"}
    # provenance is stamped
    assert c.nodes.values["a"]["source"] == "mattermost-mcp"
    assert c.nodes.values["a"]["domain"] == "mattermost"
    assert c.changes.edges == [("a", "b", {"relationship": "inTeam"})]


def test_ingest_teams_maps_team():
    c = _FakeClient()
    res = ingest_teams(
        [{"id": "T1", "name": "eng", "display_name": "Engineering", "type": "O"}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.nodes.values["mattermost:team:T1"]
    assert node["node_type"] == "Team"
    assert node["displayName"] == "Engineering"
    assert node["teamType"] == "O"
    assert node["externalToolId"] == "T1"


def test_ingest_channels_maps_channel_and_team_link():
    c = _FakeClient()
    res = ingest_channels(
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
        client=c,
    )
    assert res == {"nodes": 1, "edges": 1}
    node = c.nodes.values["mattermost:channel:C1"]
    assert node["node_type"] == "Channel"
    assert node["channelType"] == "O"
    assert node["purpose"] == "ci/cd"
    assert c.changes.edges == [
        ("mattermost:channel:C1", "mattermost:team:T1", {"relationship": "inTeam"})
    ]


def test_ingest_users_maps_person_and_bot():
    c = _FakeClient()
    res = ingest_users(
        [
            {"id": "U1", "username": "alice", "first_name": "Alice", "last_name": "A"},
            {"id": "B1", "username": "ci-bot", "is_bot": True},
        ],
        client=c,
    )
    assert res == {"nodes": 2, "edges": 0}
    assert c.nodes.values["mattermost:user:U1"]["node_type"] == "Person"
    assert c.nodes.values["mattermost:user:U1"]["name"] == "Alice A"
    assert c.nodes.values["mattermost:user:B1"]["node_type"] == "Bot"


def test_ingest_posts_maps_document_and_links():
    c = _FakeClient()
    res = ingest_posts(
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
        client=c,
    )
    # empty-message post skipped; 2 documents, links: 2 channel + 2 author + 1 reply
    assert res == {"nodes": 2, "edges": 5}
    doc = c.nodes.values["mattermost:post:P1"]
    assert doc["node_type"] == "Document"
    assert doc["text"] == "hello world"
    assert (
        "mattermost:post:P1",
        "mattermost:channel:C1",
        {"relationship": "postedInChannel"},
    ) in c.changes.edges
    assert (
        "mattermost:post:P1",
        "mattermost:user:U1",
        {"relationship": "authoredBy"},
    ) in c.changes.edges
    assert (
        "mattermost:post:P2",
        "mattermost:post:P1",
        {"relationship": "repliesTo"},
    ) in c.changes.edges


def test_ingest_documents_skips_textless():
    c = _FakeClient()
    res = ingest_documents(
        [{"id": "d1", "text": "body"}, {"id": "d2"}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 0}
    assert c.nodes.values["d1"]["node_type"] == "Document"


def test_retired_structural_alias_is_rejected():
    with pytest.raises(NativeIngestError, match="canonical node_type"):
        ingest_entities([{"id": "a", "type": "Team"}], client=_FakeClient())


def test_empty_native_ingest_is_rejected():
    with pytest.raises(NativeIngestError, match="at least one entity"):
        ingest_entities([], client=_FakeClient())
