"""CONCEPT:MM-003 Identity credentials loader and session manager."""

from agent_utilities.base_utilities import get_logger
from agent_utilities.core.config import setting

from mattermost_mcp.api_client import Api

logger = get_logger(__name__)


def get_client() -> Api:
    """Get authenticated client for mattermost_mcp."""
    base_url = setting("MATTERMOST_URL") or setting("MATTERMOST_MCP_BASE_URL", "")
    token = setting("MATTERMOST_TOKEN", "")
    username = setting("MATTERMOST_MCP_USERNAME", "")
    password = setting("MATTERMOST_MCP_PASSWORD", "")
    verify = setting("MATTERMOST_MCP_SSL_VERIFY", True)

    if not base_url:
        # Default fallback for testing
        base_url = "http://localhost"

    return Api(
        base_url=base_url,
        token=token,
        username=username,
        password=password,
        verify=verify,
    )
