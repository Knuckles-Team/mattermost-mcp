"""Native epistemic-graph typed-node + document ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_documents`` seam and the Mattermost
record mappers with a fake engine client (no engine required), asserting the txn
add_node/commit + edge calls and the record→node mapping.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

import pytest
from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError

from mattermost_mcp.kg_ingest import (
    ingest_channels,
    ingest_documents,
    ingest_entities,
    ingest_posts,
    ingest_teams,
    ingest_users,
)


class _FakeTxn:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.committed = False

    def begin(self, graph=None):
        self.graph = graph
        return "txn-1"

    def add_node(self, txn, node_id, props):
        self.nodes[node_id] = props

    def add_edge(self, txn, source, target, props):
        self.edges.append((source, target, props))

    def commit(self, txn):
        self.committed = True
        return True


class _FakeClient:
    def __init__(self):
        self.txn = _FakeTxn()


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "node_type": "Channel", "name": "town-square"},
            {"id": "b", "node_type": "Team"},
        ],
        [{"source": "a", "target": "b", "relationship": "inTeam"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    assert c.txn.committed is True
    assert set(c.txn.nodes) == {"a", "b"}
    # provenance is stamped
    assert c.txn.nodes["a"]["source"] == "mattermost-mcp"
    assert c.txn.nodes["a"]["domain"] == "mattermost"
    assert c.txn.edges == [("a", "b", {"relationship": "inTeam"})]


def test_ingest_teams_maps_team():
    c = _FakeClient()
    res = ingest_teams(
        [{"id": "T1", "name": "eng", "display_name": "Engineering", "type": "O"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.txn.nodes["mattermost:team:T1"]
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
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 1}
    node = c.txn.nodes["mattermost:channel:C1"]
    assert node["node_type"] == "Channel"
    assert node["channelType"] == "O"
    assert node["purpose"] == "ci/cd"
    assert c.txn.edges == [
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
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 0}
    assert c.txn.nodes["mattermost:user:U1"]["node_type"] == "Person"
    assert c.txn.nodes["mattermost:user:U1"]["name"] == "Alice A"
    assert c.txn.nodes["mattermost:user:B1"]["node_type"] == "Bot"


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
        graph="__commons__",
    )
    # empty-message post skipped; 2 documents, links: 2 channel + 2 author + 1 reply
    assert res == {"nodes": 2, "edges": 5}
    doc = c.txn.nodes["mattermost:post:P1"]
    assert doc["node_type"] == "Document"
    assert doc["text"] == "hello world"
    assert (
        "mattermost:post:P1",
        "mattermost:channel:C1",
        {"relationship": "postedInChannel"},
    ) in c.txn.edges
    assert (
        "mattermost:post:P1",
        "mattermost:user:U1",
        {"relationship": "authoredBy"},
    ) in c.txn.edges
    assert (
        "mattermost:post:P2",
        "mattermost:post:P1",
        {"relationship": "repliesTo"},
    ) in c.txn.edges


def test_ingest_documents_skips_textless():
    c = _FakeClient()
    res = ingest_documents(
        [{"id": "d1", "text": "body"}, {"id": "d2"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 0}
    assert c.txn.nodes["d1"]["node_type"] == "Document"


def test_retired_structural_alias_is_rejected():
    with pytest.raises(NativeIngestError, match="canonical node_type"):
        ingest_entities([{"id": "a", "type": "Team"}], client=_FakeClient())


def test_empty_native_ingest_is_rejected():
    with pytest.raises(NativeIngestError, match="at least one entity"):
        ingest_entities([], client=_FakeClient())
