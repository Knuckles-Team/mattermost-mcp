"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_saml_metadata(self, **kwargs) -> Any:
        """Get metadata
        
        Path: /api/v4/saml/metadata
        Method: GET
        """
        url = "/api/v4/saml/metadata"
        return self.request("GET", url, params=kwargs)

    def get_saml_metadata_from_idp(self, **kwargs) -> Any:
        """Get metadata from Identity Provider
        
        Path: /api/v4/saml/metadatafromidp
        Method: POST
        """
        url = "/api/v4/saml/metadatafromidp"
        return self.request("POST", url, data=kwargs)

    def upload_saml_idp_certificate(self, **kwargs) -> Any:
        """Upload IDP certificate
        
        Path: /api/v4/saml/certificate/idp
        Method: POST
        """
        url = "/api/v4/saml/certificate/idp"
        return self.request("POST", url, data=kwargs)

    def delete_saml_idp_certificate(self, **kwargs) -> Any:
        """Remove IDP certificate
        
        Path: /api/v4/saml/certificate/idp
        Method: DELETE
        """
        url = "/api/v4/saml/certificate/idp"
        return self.request("DELETE", url, params=kwargs)

    def upload_saml_public_certificate(self, **kwargs) -> Any:
        """Upload public certificate
        
        Path: /api/v4/saml/certificate/public
        Method: POST
        """
        url = "/api/v4/saml/certificate/public"
        return self.request("POST", url, data=kwargs)

    def delete_saml_public_certificate(self, **kwargs) -> Any:
        """Remove public certificate
        
        Path: /api/v4/saml/certificate/public
        Method: DELETE
        """
        url = "/api/v4/saml/certificate/public"
        return self.request("DELETE", url, params=kwargs)

    def upload_saml_private_certificate(self, **kwargs) -> Any:
        """Upload private key
        
        Path: /api/v4/saml/certificate/private
        Method: POST
        """
        url = "/api/v4/saml/certificate/private"
        return self.request("POST", url, data=kwargs)

    def delete_saml_private_certificate(self, **kwargs) -> Any:
        """Remove private key
        
        Path: /api/v4/saml/certificate/private
        Method: DELETE
        """
        url = "/api/v4/saml/certificate/private"
        return self.request("DELETE", url, params=kwargs)

    def get_saml_certificate_status(self, **kwargs) -> Any:
        """Get certificate status
        
        Path: /api/v4/saml/certificate/status
        Method: GET
        """
        url = "/api/v4/saml/certificate/status"
        return self.request("GET", url, params=kwargs)

    def reset_saml_auth_data_to_email(self, **kwargs) -> Any:
        """Reset AuthData to Email
        
        Path: /api/v4/saml/reset_auth_data
        Method: POST
        """
        url = "/api/v4/saml/reset_auth_data"
        return self.request("POST", url, data=kwargs)
