"""No served tool carries a routing `action` input (CONN-MATTERMOST-MCP-CONNECTOR-CONTENT-R001)."""

import json
from pathlib import Path

MANIFEST = (
    Path(__file__).resolve().parents[1] / "mattermost_mcp" / "operation_manifest.json"
)


def test_no_operation_takes_an_action_parameter():
    operations = json.loads(MANIFEST.read_text(encoding="utf-8"))
    routed = [
        o["name"]
        for o in operations
        if any(p["name"] == "action" for p in o["parameters"])
    ]
    assert routed == []
