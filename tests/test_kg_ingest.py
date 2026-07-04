"""Native epistemic-graph typed-node + document ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_documents`` seam and the Mattermost
record mappers with a fake engine client (no engine required), asserting the txn
add_node/commit + edge calls and the record→node mapping.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

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
        self.committed = False

    def begin(self, graph=None):
        self.graph = graph
        return "txn-1"

    def add_node(self, txn, node_id, props):
        self.nodes[node_id] = props

    def commit(self, txn):
        self.committed = True
        return True


class _FakeEdges:
    def __init__(self):
        self.edges = []

    def add(self, src, dst, props):
        self.edges.append((src, dst, props))


class _FakeClient:
    def __init__(self):
        self.txn = _FakeTxn()
        self.edges = _FakeEdges()


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "type": "Channel", "name": "town-square"},
            {"id": "b", "type": "Team"},
        ],
        [{"source": "a", "target": "b", "type": "inTeam"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    assert c.txn.committed is True
    assert set(c.txn.nodes) == {"a", "b"}
    # provenance is stamped
    assert c.txn.nodes["a"]["source"] == "mattermost-mcp"
    assert c.txn.nodes["a"]["domain"] == "mattermost"
    assert c.edges.edges == [("a", "b", {"type": "inTeam"})]


def test_ingest_teams_maps_team():
    c = _FakeClient()
    res = ingest_teams(
        [{"id": "T1", "name": "eng", "display_name": "Engineering", "type": "O"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.txn.nodes["mattermost:team:T1"]
    assert node["type"] == "Team"
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
    assert node["type"] == "Channel"
    assert node["channelType"] == "O"
    assert node["purpose"] == "ci/cd"
    assert c.edges.edges == [
        ("mattermost:channel:C1", "mattermost:team:T1", {"type": "inTeam"})
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
    assert c.txn.nodes["mattermost:user:U1"]["type"] == "Person"
    assert c.txn.nodes["mattermost:user:U1"]["name"] == "Alice A"
    assert c.txn.nodes["mattermost:user:B1"]["type"] == "Bot"


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
    assert doc["type"] == "Document"
    assert doc["text"] == "hello world"
    assert (
        "mattermost:post:P1",
        "mattermost:channel:C1",
        {"type": "postedInChannel"},
    ) in c.edges.edges
    assert (
        "mattermost:post:P1",
        "mattermost:user:U1",
        {"type": "authoredBy"},
    ) in c.edges.edges
    assert (
        "mattermost:post:P2",
        "mattermost:post:P1",
        {"type": "repliesTo"},
    ) in c.edges.edges


def test_ingest_documents_skips_textless():
    c = _FakeClient()
    res = ingest_documents(
        [{"id": "d1", "text": "body"}, {"id": "d2"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 0}
    assert c.txn.nodes["d1"]["type"] == "Document"


def test_ingest_noops_without_engine():
    # No injected client + no reachable engine -> clean no-op.
    assert ingest_entities([{"id": "a", "type": "Team"}]) is None


def test_ingest_empty_is_noop():
    assert ingest_entities([], client=_FakeClient()) is None
    assert ingest_teams([], client=_FakeClient()) is None
    assert ingest_posts([], client=_FakeClient()) is None
