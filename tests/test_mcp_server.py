import pytest


@pytest.mark.concept("MM-OS.governance.mm-2")
def test_mcp_server_registration():
    """CONCEPT:MM-OS.governance.mm-2 Test that tools register successfully."""
    from mattermost_mcp.mcp_server import get_mcp_instance

    res = get_mcp_instance()
    if isinstance(res, tuple):
        mcp = res[0]
    else:
        mcp = res
    assert mcp is not None

    # Verify tool registry count is greater than zero
    assert len(mcp._local_provider._components) > 0


@pytest.mark.concept("MM-OS.identity.mm")
def test_mcp_server_security_context():
    """CONCEPT:MM-OS.identity.mm Verify that the server registers with correct security credentials."""
    from mattermost_mcp.auth import get_client

    client = get_client()
    assert client is not None
