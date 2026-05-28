"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def open_interactive_dialog(self, **kwargs) -> Any:
        """Open a dialog

        Path: /api/v4/actions/dialogs/open
        Method: POST
        """
        url = "/api/v4/actions/dialogs/open"
        return self.request("POST", url, data=kwargs)

    def submit_interactive_dialog(self, **kwargs) -> Any:
        """Submit a dialog

        Path: /api/v4/actions/dialogs/submit
        Method: POST
        """
        url = "/api/v4/actions/dialogs/submit"
        return self.request("POST", url, data=kwargs)

    def lookup_interactive_dialog(self, **kwargs) -> Any:
        """Lookup dialog elements

        Path: /api/v4/actions/dialogs/lookup
        Method: POST
        """
        url = "/api/v4/actions/dialogs/lookup"
        return self.request("POST", url, data=kwargs)
