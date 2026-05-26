"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_incoming_webhooks(self, **kwargs) -> Any:
        """List incoming webhooks
        
        Path: /api/v4/hooks/incoming
        Method: GET
        """
        url = "/api/v4/hooks/incoming"
        return self.request("GET", url, params=kwargs)

    def create_incoming_webhook(self, **kwargs) -> Any:
        """Create an incoming webhook
        
        Path: /api/v4/hooks/incoming
        Method: POST
        """
        url = "/api/v4/hooks/incoming"
        return self.request("POST", url, data=kwargs)

    def get_incoming_webhook(self, hook_id: str, **kwargs) -> Any:
        """Get an incoming webhook
        
        Path: /api/v4/hooks/incoming/{hook_id}
        Method: GET
        """
        url = "/api/v4/hooks/incoming/{hook_id}".format(hook_id=hook_id)
        return self.request("GET", url, params=kwargs)

    def update_incoming_webhook(self, hook_id: str, **kwargs) -> Any:
        """Update an incoming webhook
        
        Path: /api/v4/hooks/incoming/{hook_id}
        Method: PUT
        """
        url = "/api/v4/hooks/incoming/{hook_id}".format(hook_id=hook_id)
        return self.request("PUT", url, data=kwargs)

    def delete_incoming_webhook(self, hook_id: str, **kwargs) -> Any:
        """Delete an incoming webhook
        
        Path: /api/v4/hooks/incoming/{hook_id}
        Method: DELETE
        """
        url = "/api/v4/hooks/incoming/{hook_id}".format(hook_id=hook_id)
        return self.request("DELETE", url, params=kwargs)

    def get_outgoing_webhooks(self, **kwargs) -> Any:
        """List outgoing webhooks
        
        Path: /api/v4/hooks/outgoing
        Method: GET
        """
        url = "/api/v4/hooks/outgoing"
        return self.request("GET", url, params=kwargs)

    def create_outgoing_webhook(self, **kwargs) -> Any:
        """Create an outgoing webhook
        
        Path: /api/v4/hooks/outgoing
        Method: POST
        """
        url = "/api/v4/hooks/outgoing"
        return self.request("POST", url, data=kwargs)

    def get_outgoing_webhook(self, hook_id: str, **kwargs) -> Any:
        """Get an outgoing webhook
        
        Path: /api/v4/hooks/outgoing/{hook_id}
        Method: GET
        """
        url = "/api/v4/hooks/outgoing/{hook_id}".format(hook_id=hook_id)
        return self.request("GET", url, params=kwargs)

    def update_outgoing_webhook(self, hook_id: str, **kwargs) -> Any:
        """Update an outgoing webhook
        
        Path: /api/v4/hooks/outgoing/{hook_id}
        Method: PUT
        """
        url = "/api/v4/hooks/outgoing/{hook_id}".format(hook_id=hook_id)
        return self.request("PUT", url, data=kwargs)

    def delete_outgoing_webhook(self, hook_id: str, **kwargs) -> Any:
        """Delete an outgoing webhook
        
        Path: /api/v4/hooks/outgoing/{hook_id}
        Method: DELETE
        """
        url = "/api/v4/hooks/outgoing/{hook_id}".format(hook_id=hook_id)
        return self.request("DELETE", url, params=kwargs)

    def regen_outgoing_hook_token(self, hook_id: str, **kwargs) -> Any:
        """Regenerate the token for the outgoing webhook.
        
        Path: /api/v4/hooks/outgoing/{hook_id}/regen_token
        Method: POST
        """
        url = "/api/v4/hooks/outgoing/{hook_id}/regen_token".format(hook_id=hook_id)
        return self.request("POST", url, data=kwargs)
