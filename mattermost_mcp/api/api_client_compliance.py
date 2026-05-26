"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_compliance_reports(self, **kwargs) -> Any:
        """Get reports
        
        Path: /api/v4/compliance/reports
        Method: GET
        """
        url = "/api/v4/compliance/reports"
        return self.request("GET", url, params=kwargs)

    def create_compliance_report(self, **kwargs) -> Any:
        """Create report
        
        Path: /api/v4/compliance/reports
        Method: POST
        """
        url = "/api/v4/compliance/reports"
        return self.request("POST", url, data=kwargs)

    def get_compliance_report(self, report_id: str, **kwargs) -> Any:
        """Get a report
        
        Path: /api/v4/compliance/reports/{report_id}
        Method: GET
        """
        url = "/api/v4/compliance/reports/{report_id}".format(report_id=report_id)
        return self.request("GET", url, params=kwargs)

    def download_compliance_report(self, report_id: str, **kwargs) -> Any:
        """Download a report
        
        Path: /api/v4/compliance/reports/{report_id}/download
        Method: GET
        """
        url = "/api/v4/compliance/reports/{report_id}/download".format(report_id=report_id)
        return self.request("GET", url, params=kwargs)
