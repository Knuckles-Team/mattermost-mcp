"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_property_fields(self, group_name: str, object_type: str, **kwargs) -> Any:
        """Get property fields
        
        Path: /api/v4/properties/groups/{group_name}/{object_type}/fields
        Method: GET
        """
        url = "/api/v4/properties/groups/{group_name}/{object_type}/fields".format(group_name=group_name, object_type=object_type)
        return self.request("GET", url, params=kwargs)

    def create_property_field(self, group_name: str, object_type: str, **kwargs) -> Any:
        """Create a property field
        
        Path: /api/v4/properties/groups/{group_name}/{object_type}/fields
        Method: POST
        """
        url = "/api/v4/properties/groups/{group_name}/{object_type}/fields".format(group_name=group_name, object_type=object_type)
        return self.request("POST", url, data=kwargs)

    def delete_property_field(self, group_name: str, object_type: str, field_id: str, **kwargs) -> Any:
        """Delete a property field
        
        Path: /api/v4/properties/groups/{group_name}/{object_type}/fields/{field_id}
        Method: DELETE
        """
        url = "/api/v4/properties/groups/{group_name}/{object_type}/fields/{field_id}".format(group_name=group_name, object_type=object_type, field_id=field_id)
        return self.request("DELETE", url, params=kwargs)

    def update_property_field(self, group_name: str, object_type: str, field_id: str, **kwargs) -> Any:
        """Update a property field
        
        Path: /api/v4/properties/groups/{group_name}/{object_type}/fields/{field_id}
        Method: PATCH
        """
        url = "/api/v4/properties/groups/{group_name}/{object_type}/fields/{field_id}".format(group_name=group_name, object_type=object_type, field_id=field_id)
        return self.request("PATCH", url, data=kwargs)

    def get_property_values(self, group_name: str, object_type: str, target_id: str, **kwargs) -> Any:
        """Get property values for a target
        
        Path: /api/v4/properties/groups/{group_name}/{object_type}/values/{target_id}
        Method: GET
        """
        url = "/api/v4/properties/groups/{group_name}/{object_type}/values/{target_id}".format(group_name=group_name, object_type=object_type, target_id=target_id)
        return self.request("GET", url, params=kwargs)

    def update_property_values(self, group_name: str, object_type: str, target_id: str, **kwargs) -> Any:
        """Update property values for a target
        
        Path: /api/v4/properties/groups/{group_name}/{object_type}/values/{target_id}
        Method: PATCH
        """
        url = "/api/v4/properties/groups/{group_name}/{object_type}/values/{target_id}".format(group_name=group_name, object_type=object_type, target_id=target_id)
        return self.request("PATCH", url, data=kwargs)

    def get_system_property_values(self, group_name: str, **kwargs) -> Any:
        """Get property values for the system
        
        Path: /api/v4/properties/groups/{group_name}/system/values
        Method: GET
        """
        url = "/api/v4/properties/groups/{group_name}/system/values".format(group_name=group_name)
        return self.request("GET", url, params=kwargs)

    def update_system_property_values(self, group_name: str, **kwargs) -> Any:
        """Update property values for the system
        
        Path: /api/v4/properties/groups/{group_name}/system/values
        Method: PATCH
        """
        url = "/api/v4/properties/groups/{group_name}/system/values".format(group_name=group_name)
        return self.request("PATCH", url, data=kwargs)
