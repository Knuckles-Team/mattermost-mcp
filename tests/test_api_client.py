import pytest


@pytest.mark.concept("MM-001")
def test_api_client_basic_mock(mock_ctx):
    """CONCEPT:MM-001 Test basic mock initialization of client facade."""
    assert mock_ctx is not None
    assert hasattr(mock_ctx, "info")


@pytest.mark.concept("MM-001")
def test_api_client_endpoints(mock_ctx):
    """CONCEPT:MM-001 Verify endpoint configuration on dynamic client."""
    from mattermost_mcp.auth import get_client

    client = get_client()
    assert client is not None
    assert hasattr(client, "request")
    assert hasattr(client, "get_users")
    assert hasattr(client, "get_all_channels")
    assert hasattr(client, "get_emoji_list")
