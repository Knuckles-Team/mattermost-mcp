"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def submit_performance_report(self, **kwargs) -> Any:
        """Report client performance metrics
        
        Path: /api/v4/client_perf
        Method: POST
        """
        url = "/api/v4/client_perf"
        return self.request("POST", url, data=kwargs)
