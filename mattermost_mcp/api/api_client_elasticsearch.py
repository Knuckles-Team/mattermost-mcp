"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def test_elasticsearch(self, **kwargs) -> Any:
        """Test Elasticsearch configuration
        
        Path: /api/v4/elasticsearch/test
        Method: POST
        """
        url = "/api/v4/elasticsearch/test"
        return self.request("POST", url, data=kwargs)

    def purge_elasticsearch_indexes(self, **kwargs) -> Any:
        """Purge all Elasticsearch indexes
        
        Path: /api/v4/elasticsearch/purge_indexes
        Method: POST
        """
        url = "/api/v4/elasticsearch/purge_indexes"
        return self.request("POST", url, data=kwargs)
