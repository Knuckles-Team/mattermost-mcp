"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def list_all_c_p_a_fields(self, **kwargs) -> Any:
        """List all the Custom Profile Attributes fields

        Path: /api/v4/custom_profile_attributes/fields
        Method: GET
        """
        url = "/api/v4/custom_profile_attributes/fields"
        return self.request("GET", url, params=kwargs)

    def create_c_p_a_field(self, **kwargs) -> Any:
        """Create a Custom Profile Attribute field

        Path: /api/v4/custom_profile_attributes/fields
        Method: POST
        """
        url = "/api/v4/custom_profile_attributes/fields"
        return self.request("POST", url, data=kwargs)

    def delete_c_p_a_field(self, field_id: str, **kwargs) -> Any:
        """Delete a Custom Profile Attribute field

        Path: /api/v4/custom_profile_attributes/fields/{field_id}
        Method: DELETE
        """
        url = f"/api/v4/custom_profile_attributes/fields/{field_id}"
        return self.request("DELETE", url, params=kwargs)

    def patch_c_p_a_field(self, field_id: str, **kwargs) -> Any:
        """Patch a Custom Profile Attribute field

        Path: /api/v4/custom_profile_attributes/fields/{field_id}
        Method: PATCH
        """
        url = f"/api/v4/custom_profile_attributes/fields/{field_id}"
        return self.request("PATCH", url, data=kwargs)

    def patch_c_p_a_values(self, **kwargs) -> Any:
        """Patch Custom Profile Attribute values

        Path: /api/v4/custom_profile_attributes/values
        Method: PATCH
        """
        url = "/api/v4/custom_profile_attributes/values"
        return self.request("PATCH", url, data=kwargs)

    def get_c_p_a_group(self, **kwargs) -> Any:
        """Get Custom Profile Attribute property group data

        Path: /api/v4/custom_profile_attributes/group
        Method: GET
        """
        url = "/api/v4/custom_profile_attributes/group"
        return self.request("GET", url, params=kwargs)

    def list_c_p_a_values(self, user_id: str, **kwargs) -> Any:
        """List Custom Profile Attribute values

        Path: /api/v4/users/{user_id}/custom_profile_attributes
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/custom_profile_attributes"
        return self.request("GET", url, params=kwargs)

    def patch_c_p_a_values_for_user(self, user_id: str, **kwargs) -> Any:
        """Update custom profile attribute values for a user

        Path: /api/v4/users/{user_id}/custom_profile_attributes
        Method: PATCH
        """
        url = f"/api/v4/users/{user_id}/custom_profile_attributes"
        return self.request("PATCH", url, data=kwargs)
