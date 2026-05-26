"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def upload_file(self, **kwargs) -> Any:
        """Upload a file
        
        Path: /api/v4/files
        Method: POST
        """
        url = "/api/v4/files"
        return self.request("POST", url, data=kwargs)

    def get_file(self, file_id: str, **kwargs) -> Any:
        """Get a file
        
        Path: /api/v4/files/{file_id}
        Method: GET
        """
        url = "/api/v4/files/{file_id}".format(file_id=file_id)
        return self.request("GET", url, params=kwargs)

    def get_file_thumbnail(self, file_id: str, **kwargs) -> Any:
        """Get a file's thumbnail
        
        Path: /api/v4/files/{file_id}/thumbnail
        Method: GET
        """
        url = "/api/v4/files/{file_id}/thumbnail".format(file_id=file_id)
        return self.request("GET", url, params=kwargs)

    def get_file_preview(self, file_id: str, **kwargs) -> Any:
        """Get a file's preview
        
        Path: /api/v4/files/{file_id}/preview
        Method: GET
        """
        url = "/api/v4/files/{file_id}/preview".format(file_id=file_id)
        return self.request("GET", url, params=kwargs)

    def get_file_link(self, file_id: str, **kwargs) -> Any:
        """Get a public file link
        
        Path: /api/v4/files/{file_id}/link
        Method: GET
        """
        url = "/api/v4/files/{file_id}/link".format(file_id=file_id)
        return self.request("GET", url, params=kwargs)

    def get_file_info(self, file_id: str, **kwargs) -> Any:
        """Get metadata for a file
        
        Path: /api/v4/files/{file_id}/info
        Method: GET
        """
        url = "/api/v4/files/{file_id}/info".format(file_id=file_id)
        return self.request("GET", url, params=kwargs)

    def get_file_public(self, file_id: str, **kwargs) -> Any:
        """Get a public file
        
        Path: /files/{file_id}/public
        Method: GET
        """
        url = "/files/{file_id}/public".format(file_id=file_id)
        return self.request("GET", url, params=kwargs)

    def search_files(self, team_id: str, **kwargs) -> Any:
        """Search files in a team
        
        Path: /api/v4/teams/{team_id}/files/search
        Method: POST
        """
        url = "/api/v4/teams/{team_id}/files/search".format(team_id=team_id)
        return self.request("POST", url, data=kwargs)

    def search_files(self, **kwargs) -> Any:
        """Search files across the teams of the current user
        
        Path: /api/v4/files/search
        Method: POST
        """
        url = "/api/v4/files/search"
        return self.request("POST", url, data=kwargs)
