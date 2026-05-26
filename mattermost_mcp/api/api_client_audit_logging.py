"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def add_audit_log_certificate(self, **kwargs) -> Any:
        """Upload audit log certificate
        
        Path: /api/v4/audit_logs/certificate
        Method: POST
        """
        url = "/api/v4/audit_logs/certificate"
        return self.request("POST", url, data=kwargs)

    def remove_audit_log_certificate(self, **kwargs) -> Any:
        """Remove audit log certificate
        
        Path: /api/v4/audit_logs/certificate
        Method: DELETE
        """
        url = "/api/v4/audit_logs/certificate"
        return self.request("DELETE", url, params=kwargs)
