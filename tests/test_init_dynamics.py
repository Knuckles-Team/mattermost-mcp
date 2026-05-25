import pytest
@pytest.mark.concept("MM-001")
def test_init_dynamics():
    import mattermost_mcp

    assert mattermost_mcp._MCP_AVAILABLE is True
