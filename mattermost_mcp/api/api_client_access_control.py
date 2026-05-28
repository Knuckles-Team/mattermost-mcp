"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def create_access_control_policy(self, **kwargs) -> Any:
        """Create an access control policy

        Path: /api/v4/access_control_policies
        Method: PUT
        """
        url = "/api/v4/access_control_policies"
        return self.request("PUT", url, data=kwargs)

    def check_access_control_policy_expression(self, **kwargs) -> Any:
        """Check an access control policy expression

        Path: /api/v4/access_control_policies/cel/check
        Method: POST
        """
        url = "/api/v4/access_control_policies/cel/check"
        return self.request("POST", url, data=kwargs)

    def validate_expression_against_requester(self, **kwargs) -> Any:
        """Validate if the current user matches a CEL expression

        Path: /api/v4/access_control_policies/cel/validate_requester
        Method: POST
        """
        url = "/api/v4/access_control_policies/cel/validate_requester"
        return self.request("POST", url, data=kwargs)

    def test_access_control_policy_expression(self, **kwargs) -> Any:
        """Test an access control policy expression

        Path: /api/v4/access_control_policies/cel/test
        Method: POST
        """
        url = "/api/v4/access_control_policies/cel/test"
        return self.request("POST", url, data=kwargs)

    def simulate_access_control_policy_for_users(self, **kwargs) -> Any:
        """Simulate an access control policy decision for an explicit user list

        Path: /api/v4/access_control_policies/cel/simulate_users
        Method: POST
        """
        url = "/api/v4/access_control_policies/cel/simulate_users"
        return self.request("POST", url, data=kwargs)

    def search_access_control_policies(self, **kwargs) -> Any:
        """Search access control policies

        Path: /api/v4/access_control_policies/search
        Method: POST
        """
        url = "/api/v4/access_control_policies/search"
        return self.request("POST", url, data=kwargs)

    def get_access_control_policy_autocomplete_fields(self, **kwargs) -> Any:
        """Get autocomplete fields for access control policies

        Path: /api/v4/access_control_policies/cel/autocomplete/fields
        Method: GET
        """
        url = "/api/v4/access_control_policies/cel/autocomplete/fields"
        return self.request("GET", url, params=kwargs)

    def get_access_control_policy(self, policy_id: str, **kwargs) -> Any:
        """Get an access control policy

        Path: /api/v4/access_control_policies/{policy_id}
        Method: GET
        """
        url = f"/api/v4/access_control_policies/{policy_id}"
        return self.request("GET", url, params=kwargs)

    def delete_access_control_policy(self, policy_id: str, **kwargs) -> Any:
        """Delete an access control policy

        Path: /api/v4/access_control_policies/{policy_id}
        Method: DELETE
        """
        url = f"/api/v4/access_control_policies/{policy_id}"
        return self.request("DELETE", url, params=kwargs)

    def update_access_control_policy_active_status(
        self, policy_id: str, **kwargs
    ) -> Any:
        """Activate or deactivate an access control policy

        Path: /api/v4/access_control_policies/{policy_id}/activate
        Method: GET
        """
        url = f"/api/v4/access_control_policies/{policy_id}/activate"
        return self.request("GET", url, params=kwargs)

    def assign_access_control_policy_to_channels(self, policy_id: str, **kwargs) -> Any:
        """Assign an access control policy to channels

        Path: /api/v4/access_control_policies/{policy_id}/assign
        Method: POST
        """
        url = f"/api/v4/access_control_policies/{policy_id}/assign"
        return self.request("POST", url, data=kwargs)

    def unassign_access_control_policy_from_channels(
        self, policy_id: str, **kwargs
    ) -> Any:
        """Unassign an access control policy from channels

        Path: /api/v4/access_control_policies/{policy_id}/unassign
        Method: DELETE
        """
        url = f"/api/v4/access_control_policies/{policy_id}/unassign"
        return self.request("DELETE", url, params=kwargs)

    def get_channels_for_access_control_policy(self, policy_id: str, **kwargs) -> Any:
        """Get channels for an access control policy

        Path: /api/v4/access_control_policies/{policy_id}/resources/channels
        Method: GET
        """
        url = f"/api/v4/access_control_policies/{policy_id}/resources/channels"
        return self.request("GET", url, params=kwargs)

    def search_channels_for_access_control_policy(
        self, policy_id: str, **kwargs
    ) -> Any:
        """Search channels for an access control policy

        Path: /api/v4/access_control_policies/{policy_id}/resources/channels/search
        Method: POST
        """
        url = f"/api/v4/access_control_policies/{policy_id}/resources/channels/search"
        return self.request("POST", url, data=kwargs)

    def get_channel_access_control_attributes(self, channel_id: str, **kwargs) -> Any:
        """Get access control attributes for a channel

        Path: /api/v4/channels/{channel_id}/access_control/attributes
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}/access_control/attributes"
        return self.request("GET", url, params=kwargs)

    def get_c_e_l_visual_a_s_t(self, **kwargs) -> Any:
        """Get the visual AST for a CEL expression

        Path: /api/v4/access_control_policies/cel/visual_ast
        Method: POST
        """
        url = "/api/v4/access_control_policies/cel/visual_ast"
        return self.request("POST", url, data=kwargs)

    def update_access_control_policies_active(self, **kwargs) -> Any:
        """Activate or deactivate access control policies

        Path: /api/v4/access_control_policies/activate
        Method: PUT
        """
        url = "/api/v4/access_control_policies/activate"
        return self.request("PUT", url, data=kwargs)
