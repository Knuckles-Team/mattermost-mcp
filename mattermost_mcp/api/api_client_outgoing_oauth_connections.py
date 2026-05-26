"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def list_outgoing_o_auth_connections(self, **kwargs) -> Any:
        """List all connections
        
        Path: /api/v4/oauth/outgoing_connections
        Method: GET
        """
        url = "/api/v4/oauth/outgoing_connections"
        return self.request("GET", url, params=kwargs)

    def create_outgoing_o_auth_connection(self, **kwargs) -> Any:
        """Create a connection
        
        Path: /api/v4/oauth/outgoing_connections
        Method: POST
        """
        url = "/api/v4/oauth/outgoing_connections"
        return self.request("POST", url, data=kwargs)

    def get_outgoing_o_auth_connection(self, outgoing_oauth_connection_id: str, **kwargs) -> Any:
        """Get a connection
        
        Path: /api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}
        Method: GET
        """
        url = "/api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}".format(outgoing_oauth_connection_id=outgoing_oauth_connection_id)
        return self.request("GET", url, params=kwargs)

    def update_outgoing_o_auth_connection(self, outgoing_oauth_connection_id: str, **kwargs) -> Any:
        """Update a connection
        
        Path: /api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}
        Method: PUT
        """
        url = "/api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}".format(outgoing_oauth_connection_id=outgoing_oauth_connection_id)
        return self.request("PUT", url, data=kwargs)

    def delete_outgoing_o_auth_connection(self, outgoing_oauth_connection_id: str, **kwargs) -> Any:
        """Delete a connection
        
        Path: /api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}
        Method: DELETE
        """
        url = "/api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}".format(outgoing_oauth_connection_id=outgoing_oauth_connection_id)
        return self.request("DELETE", url, params=kwargs)

    def validate_outgoing_o_auth_connection(self, **kwargs) -> Any:
        """Validate a connection configuration
        
        Path: /api/v4/oauth/outgoing_connections/validate
        Method: POST
        """
        url = "/api/v4/oauth/outgoing_connections/validate"
        return self.request("POST", url, data=kwargs)
