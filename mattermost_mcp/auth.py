"""CONCEPT:MM-003 Identity credentials loader and session manager."""

import os

from agent_utilities.base_utilities import get_logger, to_boolean

from mattermost_mcp.api_client import Api

logger = get_logger(__name__)


def get_client() -> Api:
    """Get authenticated client for mattermost_mcp."""
    base_url = os.getenv("MATTERMOST_URL") or os.getenv("MATTERMOST_MCP_BASE_URL", "")
    token = os.getenv("MATTERMOST_TOKEN", "")
    username = os.getenv("MATTERMOST_MCP_USERNAME", "")
    password = os.getenv("MATTERMOST_MCP_PASSWORD", "")
    verify = to_boolean(os.getenv("MATTERMOST_MCP_SSL_VERIFY", "True"))

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
