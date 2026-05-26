"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def sync_ldap(self, **kwargs) -> Any:
        """Sync with LDAP
        
        Path: /api/v4/ldap/sync
        Method: POST
        """
        url = "/api/v4/ldap/sync"
        return self.request("POST", url, data=kwargs)

    def test_ldap(self, **kwargs) -> Any:
        """Test LDAP configuration
        
        Path: /api/v4/ldap/test
        Method: POST
        """
        url = "/api/v4/ldap/test"
        return self.request("POST", url, data=kwargs)

    def test_ldap_connection(self, **kwargs) -> Any:
        """Test LDAP connection with specific settings
        
        Path: /api/v4/ldap/test_connection
        Method: POST
        """
        url = "/api/v4/ldap/test_connection"
        return self.request("POST", url, data=kwargs)

    def test_ldap_diagnostics(self, **kwargs) -> Any:
        """Test LDAP diagnostics with specific settings
        
        Path: /api/v4/ldap/test_diagnostics
        Method: POST
        """
        url = "/api/v4/ldap/test_diagnostics"
        return self.request("POST", url, data=kwargs)

    def get_ldap_groups(self, **kwargs) -> Any:
        """Returns a list of LDAP groups
        
        Path: /api/v4/ldap/groups
        Method: GET
        """
        url = "/api/v4/ldap/groups"
        return self.request("GET", url, params=kwargs)

    def link_ldap_group(self, remote_id: str, **kwargs) -> Any:
        """Link a LDAP group
        
        Path: /api/v4/ldap/groups/{remote_id}/link
        Method: POST
        """
        url = "/api/v4/ldap/groups/{remote_id}/link".format(remote_id=remote_id)
        return self.request("POST", url, data=kwargs)

    def unlink_ldap_group(self, remote_id: str, **kwargs) -> Any:
        """Delete a link for LDAP group
        
        Path: /api/v4/ldap/groups/{remote_id}/link
        Method: DELETE
        """
        url = "/api/v4/ldap/groups/{remote_id}/link".format(remote_id=remote_id)
        return self.request("DELETE", url, params=kwargs)

    def migrate_id_ldap(self, **kwargs) -> Any:
        """Migrate Id LDAP
        
        Path: /api/v4/ldap/migrateid
        Method: POST
        """
        url = "/api/v4/ldap/migrateid"
        return self.request("POST", url, data=kwargs)

    def upload_ldap_public_certificate(self, **kwargs) -> Any:
        """Upload public certificate
        
        Path: /api/v4/ldap/certificate/public
        Method: POST
        """
        url = "/api/v4/ldap/certificate/public"
        return self.request("POST", url, data=kwargs)

    def delete_ldap_public_certificate(self, **kwargs) -> Any:
        """Remove public certificate
        
        Path: /api/v4/ldap/certificate/public
        Method: DELETE
        """
        url = "/api/v4/ldap/certificate/public"
        return self.request("DELETE", url, params=kwargs)

    def upload_ldap_private_certificate(self, **kwargs) -> Any:
        """Upload private key
        
        Path: /api/v4/ldap/certificate/private
        Method: POST
        """
        url = "/api/v4/ldap/certificate/private"
        return self.request("POST", url, data=kwargs)

    def delete_ldap_private_certificate(self, **kwargs) -> Any:
        """Remove private key
        
        Path: /api/v4/ldap/certificate/private
        Method: DELETE
        """
        url = "/api/v4/ldap/certificate/private"
        return self.request("DELETE", url, params=kwargs)

    def add_user_to_group_syncables(self, user_id: str, **kwargs) -> Any:
        """Create memberships for LDAP configured channels and teams for this user
        
        Path: /api/v4/ldap/users/{user_id}/group_sync_memberships
        Method: POST
        """
        url = "/api/v4/ldap/users/{user_id}/group_sync_memberships".format(user_id=user_id)
        return self.request("POST", url, data=kwargs)
