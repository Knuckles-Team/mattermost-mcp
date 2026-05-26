"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_data_retention_policy(self, **kwargs) -> Any:
        """Get the global data retention policy
        
        Path: /api/v4/data_retention/policy
        Method: GET
        """
        url = "/api/v4/data_retention/policy"
        return self.request("GET", url, params=kwargs)

    def get_data_retention_policies_count(self, **kwargs) -> Any:
        """Get the number of granular data retention policies
        
        Path: /api/v4/data_retention/policies_count
        Method: GET
        """
        url = "/api/v4/data_retention/policies_count"
        return self.request("GET", url, params=kwargs)

    def get_data_retention_policies(self, **kwargs) -> Any:
        """Get the granular data retention policies
        
        Path: /api/v4/data_retention/policies
        Method: GET
        """
        url = "/api/v4/data_retention/policies"
        return self.request("GET", url, params=kwargs)

    def create_data_retention_policy(self, **kwargs) -> Any:
        """Create a new granular data retention policy
        
        Path: /api/v4/data_retention/policies
        Method: POST
        """
        url = "/api/v4/data_retention/policies"
        return self.request("POST", url, data=kwargs)

    def get_data_retention_policy_by_i_d(self, policy_id: str, **kwargs) -> Any:
        """Get a granular data retention policy
        
        Path: /api/v4/data_retention/policies/{policy_id}
        Method: GET
        """
        url = "/api/v4/data_retention/policies/{policy_id}".format(policy_id=policy_id)
        return self.request("GET", url, params=kwargs)

    def delete_data_retention_policy(self, policy_id: str, **kwargs) -> Any:
        """Delete a granular data retention policy
        
        Path: /api/v4/data_retention/policies/{policy_id}
        Method: DELETE
        """
        url = "/api/v4/data_retention/policies/{policy_id}".format(policy_id=policy_id)
        return self.request("DELETE", url, params=kwargs)

    def patch_data_retention_policy(self, policy_id: str, **kwargs) -> Any:
        """Patch a granular data retention policy
        
        Path: /api/v4/data_retention/policies/{policy_id}
        Method: PATCH
        """
        url = "/api/v4/data_retention/policies/{policy_id}".format(policy_id=policy_id)
        return self.request("PATCH", url, data=kwargs)

    def get_teams_for_retention_policy(self, policy_id: str, **kwargs) -> Any:
        """Get the teams for a granular data retention policy
        
        Path: /api/v4/data_retention/policies/{policy_id}/teams
        Method: GET
        """
        url = "/api/v4/data_retention/policies/{policy_id}/teams".format(policy_id=policy_id)
        return self.request("GET", url, params=kwargs)

    def add_teams_to_retention_policy(self, policy_id: str, **kwargs) -> Any:
        """Add teams to a granular data retention policy
        
        Path: /api/v4/data_retention/policies/{policy_id}/teams
        Method: POST
        """
        url = "/api/v4/data_retention/policies/{policy_id}/teams".format(policy_id=policy_id)
        return self.request("POST", url, data=kwargs)

    def remove_teams_from_retention_policy(self, policy_id: str, **kwargs) -> Any:
        """Delete teams from a granular data retention policy
        
        Path: /api/v4/data_retention/policies/{policy_id}/teams
        Method: DELETE
        """
        url = "/api/v4/data_retention/policies/{policy_id}/teams".format(policy_id=policy_id)
        return self.request("DELETE", url, params=kwargs)

    def search_teams_for_retention_policy(self, policy_id: str, **kwargs) -> Any:
        """Search for the teams in a granular data retention policy
        
        Path: /api/v4/data_retention/policies/{policy_id}/teams/search
        Method: POST
        """
        url = "/api/v4/data_retention/policies/{policy_id}/teams/search".format(policy_id=policy_id)
        return self.request("POST", url, data=kwargs)

    def get_channels_for_retention_policy(self, policy_id: str, **kwargs) -> Any:
        """Get the channels for a granular data retention policy
        
        Path: /api/v4/data_retention/policies/{policy_id}/channels
        Method: GET
        """
        url = "/api/v4/data_retention/policies/{policy_id}/channels".format(policy_id=policy_id)
        return self.request("GET", url, params=kwargs)

    def add_channels_to_retention_policy(self, policy_id: str, **kwargs) -> Any:
        """Add channels to a granular data retention policy
        
        Path: /api/v4/data_retention/policies/{policy_id}/channels
        Method: POST
        """
        url = "/api/v4/data_retention/policies/{policy_id}/channels".format(policy_id=policy_id)
        return self.request("POST", url, data=kwargs)

    def remove_channels_from_retention_policy(self, policy_id: str, **kwargs) -> Any:
        """Delete channels from a granular data retention policy
        
        Path: /api/v4/data_retention/policies/{policy_id}/channels
        Method: DELETE
        """
        url = "/api/v4/data_retention/policies/{policy_id}/channels".format(policy_id=policy_id)
        return self.request("DELETE", url, params=kwargs)

    def search_channels_for_retention_policy(self, policy_id: str, **kwargs) -> Any:
        """Search for the channels in a granular data retention policy
        
        Path: /api/v4/data_retention/policies/{policy_id}/channels/search
        Method: POST
        """
        url = "/api/v4/data_retention/policies/{policy_id}/channels/search".format(policy_id=policy_id)
        return self.request("POST", url, data=kwargs)
