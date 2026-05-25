import pytest
@pytest.mark.concept("MM-002")
def test_startup():
    # Basic import test
    import mattermost_mcp

    assert mattermost_mcp.__version__ == "0.15.0"
