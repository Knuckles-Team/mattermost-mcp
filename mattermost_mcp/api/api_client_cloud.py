"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_cloud_limits(self, **kwargs) -> Any:
        """Get cloud workspace limits
        
        Path: /api/v4/cloud/limits
        Method: GET
        """
        url = "/api/v4/cloud/limits"
        return self.request("GET", url, params=kwargs)

    def get_cloud_products(self, **kwargs) -> Any:
        """Get cloud products
        
        Path: /api/v4/cloud/products
        Method: GET
        """
        url = "/api/v4/cloud/products"
        return self.request("GET", url, params=kwargs)

    def get_cloud_customer(self, **kwargs) -> Any:
        """Get cloud customer
        
        Path: /api/v4/cloud/customer
        Method: GET
        """
        url = "/api/v4/cloud/customer"
        return self.request("GET", url, params=kwargs)

    def update_cloud_customer(self, **kwargs) -> Any:
        """Update cloud customer
        
        Path: /api/v4/cloud/customer
        Method: PUT
        """
        url = "/api/v4/cloud/customer"
        return self.request("PUT", url, data=kwargs)

    def update_cloud_customer_address(self, **kwargs) -> Any:
        """Update cloud customer address
        
        Path: /api/v4/cloud/customer/address
        Method: PUT
        """
        url = "/api/v4/cloud/customer/address"
        return self.request("PUT", url, data=kwargs)

    def validate_business_email(self, **kwargs) -> Any:
        """Validate business email
        
        Path: /api/v4/cloud/validate-business-email
        Method: POST
        """
        url = "/api/v4/cloud/validate-business-email"
        return self.request("POST", url, data=kwargs)

    def validate_workspace_business_email(self, **kwargs) -> Any:
        """Validate workspace business email
        
        Path: /api/v4/cloud/validate-workspace-business-email
        Method: POST
        """
        url = "/api/v4/cloud/validate-workspace-business-email"
        return self.request("POST", url, data=kwargs)

    def get_subscription(self, **kwargs) -> Any:
        """Get cloud subscription
        
        Path: /api/v4/cloud/subscription
        Method: GET
        """
        url = "/api/v4/cloud/subscription"
        return self.request("GET", url, params=kwargs)

    def get_endpoint_for_installation_information(self, **kwargs) -> Any:
        """GET endpoint for Installation information
        
        Path: /api/v4/cloud/installation
        Method: GET
        """
        url = "/api/v4/cloud/installation"
        return self.request("GET", url, params=kwargs)

    def get_invoices_for_subscription(self, **kwargs) -> Any:
        """Get cloud subscription invoices
        
        Path: /api/v4/cloud/subscription/invoices
        Method: GET
        """
        url = "/api/v4/cloud/subscription/invoices"
        return self.request("GET", url, params=kwargs)

    def get_invoice_for_subscription_as_pdf(self, invoice_id: str, **kwargs) -> Any:
        """Get cloud invoice PDF
        
        Path: /api/v4/cloud/subscription/invoices/{invoice_id}/pdf
        Method: GET
        """
        url = "/api/v4/cloud/subscription/invoices/{invoice_id}/pdf".format(invoice_id=invoice_id)
        return self.request("GET", url, params=kwargs)

    def hosted_customer_signup_available(self, **kwargs) -> Any:
        """Check hosted signup availability
        
        Path: /api/v4/hosted_customer/signup_available
        Method: GET
        """
        url = "/api/v4/hosted_customer/signup_available"
        return self.request("GET", url, params=kwargs)

    def check_c_w_s_connection(self, **kwargs) -> Any:
        """Check CWS connection
        
        Path: /api/v4/cloud/check-cws-connection
        Method: GET
        """
        url = "/api/v4/cloud/check-cws-connection"
        return self.request("GET", url, params=kwargs)

    def post_endpoint_for_cws_webhooks(self, **kwargs) -> Any:
        """POST endpoint for CWS Webhooks
        
        Path: /api/v4/cloud/webhook
        Method: POST
        """
        url = "/api/v4/cloud/webhook"
        return self.request("POST", url, data=kwargs)

    def get_preview_modal_data(self, **kwargs) -> Any:
        """Get cloud preview modal data
        
        Path: /api/v4/cloud/preview/modal_data
        Method: GET
        """
        url = "/api/v4/cloud/preview/modal_data"
        return self.request("GET", url, params=kwargs)
