"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_jobs(self, **kwargs) -> Any:
        """Get the jobs.

        Path: /api/v4/jobs
        Method: GET
        """
        url = "/api/v4/jobs"
        return self.request("GET", url, params=kwargs)

    def create_job(self, **kwargs) -> Any:
        """Create a new job.

        Path: /api/v4/jobs
        Method: POST
        """
        url = "/api/v4/jobs"
        return self.request("POST", url, data=kwargs)

    def get_job(self, job_id: str, **kwargs) -> Any:
        """Get a job.

        Path: /api/v4/jobs/{job_id}
        Method: GET
        """
        url = f"/api/v4/jobs/{job_id}"
        return self.request("GET", url, params=kwargs)

    def download_job(self, job_id: str, **kwargs) -> Any:
        """Download the results of a job.

        Path: /api/v4/jobs/{job_id}/download
        Method: GET
        """
        url = f"/api/v4/jobs/{job_id}/download"
        return self.request("GET", url, params=kwargs)

    def cancel_job(self, job_id: str, **kwargs) -> Any:
        """Cancel a job.

        Path: /api/v4/jobs/{job_id}/cancel
        Method: POST
        """
        url = f"/api/v4/jobs/{job_id}/cancel"
        return self.request("POST", url, data=kwargs)

    def get_jobs_by_type(self, job_type: str, **kwargs) -> Any:
        """Get the jobs of the given type.

        Path: /api/v4/jobs/type/{job_type}
        Method: GET
        """
        url = f"/api/v4/jobs/type/{job_type}"
        return self.request("GET", url, params=kwargs)

    def update_job_status(self, job_id: str, **kwargs) -> Any:
        """Update the status of a job

        Path: /api/v4/jobs/{job_id}/status
        Method: PATCH
        """
        url = f"/api/v4/jobs/{job_id}/status"
        return self.request("PATCH", url, data=kwargs)
