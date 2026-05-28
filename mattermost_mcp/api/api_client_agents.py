"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_agents(self, **kwargs) -> Any:
        """Get available agents

        Path: /api/v4/agents
        Method: GET
        """
        url = "/api/v4/agents"
        return self.request("GET", url, params=kwargs)

    def get_agents_status(self, **kwargs) -> Any:
        """Get agents bridge status

        Path: /api/v4/agents/status
        Method: GET
        """
        url = "/api/v4/agents/status"
        return self.request("GET", url, params=kwargs)

    def get_l_l_m_services(self, **kwargs) -> Any:
        """Get available LLM services

        Path: /api/v4/llmservices
        Method: GET
        """
        url = "/api/v4/llmservices"
        return self.request("GET", url, params=kwargs)
