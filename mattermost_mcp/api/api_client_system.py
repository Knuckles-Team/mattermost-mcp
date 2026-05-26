"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_supported_timezone(self, **kwargs) -> Any:
        """Retrieve a list of supported timezones
        
        Path: /api/v4/system/timezones
        Method: GET
        """
        url = "/api/v4/system/timezones"
        return self.request("GET", url, params=kwargs)

    def get_ping(self, **kwargs) -> Any:
        """Check system health
        
        Path: /api/v4/system/ping
        Method: GET
        """
        url = "/api/v4/system/ping"
        return self.request("GET", url, params=kwargs)

    def connect_web_socket(self, **kwargs) -> Any:
        """Open a WebSocket connection
        
        Path: /api/v4/websocket
        Method: GET
        """
        url = "/api/v4/websocket"
        return self.request("GET", url, params=kwargs)

    def manual_test(self, **kwargs) -> Any:
        """Run manual testing helpers
        
        Path: /manualtest
        Method: GET
        """
        url = "/manualtest"
        return self.request("GET", url, params=kwargs)

    def get_notices(self, team_id: str, **kwargs) -> Any:
        """Get notices for logged in user in specified team
        
        Path: /api/v4/system/notices/{team_id}
        Method: GET
        """
        url = "/api/v4/system/notices/{team_id}".format(team_id=team_id)
        return self.request("GET", url, params=kwargs)

    def mark_notices_viewed(self, **kwargs) -> Any:
        """Update notices as 'viewed'
        
        Path: /api/v4/system/notices/view
        Method: PUT
        """
        url = "/api/v4/system/notices/view"
        return self.request("PUT", url, data=kwargs)

    def get_onboarding_complete(self, **kwargs) -> Any:
        """Get first admin onboarding completion status
        
        Path: /api/v4/system/onboarding/complete
        Method: GET
        """
        url = "/api/v4/system/onboarding/complete"
        return self.request("GET", url, params=kwargs)

    def complete_onboarding(self, **kwargs) -> Any:
        """Complete first admin onboarding
        
        Path: /api/v4/system/onboarding/complete
        Method: POST
        """
        url = "/api/v4/system/onboarding/complete"
        return self.request("POST", url, data=kwargs)

    def get_a_i_bridge_test_helper(self, **kwargs) -> Any:
        """Get AI bridge E2E test helper state
        
        Path: /api/v4/system/e2e/ai_bridge
        Method: GET
        """
        url = "/api/v4/system/e2e/ai_bridge"
        return self.request("GET", url, params=kwargs)

    def set_a_i_bridge_test_helper(self, **kwargs) -> Any:
        """Configure AI bridge E2E test helper
        
        Path: /api/v4/system/e2e/ai_bridge
        Method: PUT
        """
        url = "/api/v4/system/e2e/ai_bridge"
        return self.request("PUT", url, data=kwargs)

    def delete_a_i_bridge_test_helper(self, **kwargs) -> Any:
        """Reset AI bridge E2E test helper
        
        Path: /api/v4/system/e2e/ai_bridge
        Method: DELETE
        """
        url = "/api/v4/system/e2e/ai_bridge"
        return self.request("DELETE", url, params=kwargs)

    def database_recycle(self, **kwargs) -> Any:
        """Recycle database connections
        
        Path: /api/v4/database/recycle
        Method: POST
        """
        url = "/api/v4/database/recycle"
        return self.request("POST", url, data=kwargs)

    def test_email(self, **kwargs) -> Any:
        """Send a test email
        
        Path: /api/v4/email/test
        Method: POST
        """
        url = "/api/v4/email/test"
        return self.request("POST", url, data=kwargs)

    def test_notification(self, **kwargs) -> Any:
        """Send a test notification
        
        Path: /api/v4/notifications/test
        Method: POST
        """
        url = "/api/v4/notifications/test"
        return self.request("POST", url, data=kwargs)

    def test_site_u_r_l(self, **kwargs) -> Any:
        """Checks the validity of a Site URL
        
        Path: /api/v4/site_url/test
        Method: POST
        """
        url = "/api/v4/site_url/test"
        return self.request("POST", url, data=kwargs)

    def test_s3_connection(self, **kwargs) -> Any:
        """Test AWS S3 connection
        
        Path: /api/v4/file/s3_test
        Method: POST
        """
        url = "/api/v4/file/s3_test"
        return self.request("POST", url, data=kwargs)

    def get_config(self, **kwargs) -> Any:
        """Get configuration
        
        Path: /api/v4/config
        Method: GET
        """
        url = "/api/v4/config"
        return self.request("GET", url, params=kwargs)

    def update_config(self, **kwargs) -> Any:
        """Update configuration
        
        Path: /api/v4/config
        Method: PUT
        """
        url = "/api/v4/config"
        return self.request("PUT", url, data=kwargs)

    def reload_config(self, **kwargs) -> Any:
        """Reload configuration
        
        Path: /api/v4/config/reload
        Method: POST
        """
        url = "/api/v4/config/reload"
        return self.request("POST", url, data=kwargs)

    def migrate_config(self, **kwargs) -> Any:
        """Migrate config storage
        
        Path: /api/v4/config/migrate
        Method: POST
        """
        url = "/api/v4/config/migrate"
        return self.request("POST", url, data=kwargs)

    def get_client_config(self, **kwargs) -> Any:
        """Get client configuration
        
        Path: /api/v4/config/client
        Method: GET
        """
        url = "/api/v4/config/client"
        return self.request("GET", url, params=kwargs)

    def get_environment_config(self, **kwargs) -> Any:
        """Get configuration made through environment variables
        
        Path: /api/v4/config/environment
        Method: GET
        """
        url = "/api/v4/config/environment"
        return self.request("GET", url, params=kwargs)

    def patch_config(self, **kwargs) -> Any:
        """Patch configuration
        
        Path: /api/v4/config/patch
        Method: PUT
        """
        url = "/api/v4/config/patch"
        return self.request("PUT", url, data=kwargs)

    def upload_license_file(self, **kwargs) -> Any:
        """Upload license file
        
        Path: /api/v4/license
        Method: POST
        """
        url = "/api/v4/license"
        return self.request("POST", url, data=kwargs)

    def remove_license_file(self, **kwargs) -> Any:
        """Remove license file
        
        Path: /api/v4/license
        Method: DELETE
        """
        url = "/api/v4/license"
        return self.request("DELETE", url, params=kwargs)

    def get_client_license(self, **kwargs) -> Any:
        """Get client license
        
        Path: /api/v4/license/client
        Method: GET
        """
        url = "/api/v4/license/client"
        return self.request("GET", url, params=kwargs)

    def get_license_load_metric(self, **kwargs) -> Any:
        """Get license load metric
        
        Path: /api/v4/license/load_metric
        Method: GET
        """
        url = "/api/v4/license/load_metric"
        return self.request("GET", url, params=kwargs)

    def request_trial_license(self, **kwargs) -> Any:
        """Request and install a trial license for your server
        
        Path: /api/v4/trial-license
        Method: POST
        """
        url = "/api/v4/trial-license"
        return self.request("POST", url, data=kwargs)

    def get_prev_trial_license(self, **kwargs) -> Any:
        """Get last trial license used
        
        Path: /api/v4/trial-license/prev
        Method: GET
        """
        url = "/api/v4/trial-license/prev"
        return self.request("GET", url, params=kwargs)

    def get_audits(self, **kwargs) -> Any:
        """Get audits
        
        Path: /api/v4/audits
        Method: GET
        """
        url = "/api/v4/audits"
        return self.request("GET", url, params=kwargs)

    def invalidate_caches(self, **kwargs) -> Any:
        """Invalidate all the caches
        
        Path: /api/v4/caches/invalidate
        Method: POST
        """
        url = "/api/v4/caches/invalidate"
        return self.request("POST", url, data=kwargs)

    def get_logs(self, **kwargs) -> Any:
        """Get logs
        
        Path: /api/v4/logs
        Method: GET
        """
        url = "/api/v4/logs"
        return self.request("GET", url, params=kwargs)

    def post_log(self, **kwargs) -> Any:
        """Add log message
        
        Path: /api/v4/logs
        Method: POST
        """
        url = "/api/v4/logs"
        return self.request("POST", url, data=kwargs)

    def query_logs(self, **kwargs) -> Any:
        """Query server logs with filters
        
        Path: /api/v4/logs/query
        Method: POST
        """
        url = "/api/v4/logs/query"
        return self.request("POST", url, data=kwargs)

    def get_analytics_old(self, **kwargs) -> Any:
        """Get analytics
        
        Path: /api/v4/analytics/old
        Method: GET
        """
        url = "/api/v4/analytics/old"
        return self.request("GET", url, params=kwargs)

    def get_latest_version(self, **kwargs) -> Any:
        """Get latest public server release information
        
        Path: /api/v4/latest_version
        Method: GET
        """
        url = "/api/v4/latest_version"
        return self.request("GET", url, params=kwargs)

    def get_applied_schema_migrations(self, **kwargs) -> Any:
        """Get applied database schema migrations
        
        Path: /api/v4/system/schema/version
        Method: GET
        """
        url = "/api/v4/system/schema/version"
        return self.request("GET", url, params=kwargs)

    def get_server_busy_expires(self, **kwargs) -> Any:
        """Get server busy expiry time.
        
        Path: /api/v4/server_busy
        Method: GET
        """
        url = "/api/v4/server_busy"
        return self.request("GET", url, params=kwargs)

    def set_server_busy(self, **kwargs) -> Any:
        """Set the server busy (high load) flag
        
        Path: /api/v4/server_busy
        Method: POST
        """
        url = "/api/v4/server_busy"
        return self.request("POST", url, data=kwargs)

    def clear_server_busy(self, **kwargs) -> Any:
        """Clears the server busy (high load) flag
        
        Path: /api/v4/server_busy
        Method: DELETE
        """
        url = "/api/v4/server_busy"
        return self.request("DELETE", url, params=kwargs)

    def acknowledge_notification(self, **kwargs) -> Any:
        """Acknowledge receiving of a notification
        
        Path: /api/v4/notifications/ack
        Method: POST
        """
        url = "/api/v4/notifications/ack"
        return self.request("POST", url, data=kwargs)

    def get_redirect_location(self, **kwargs) -> Any:
        """Get redirect location
        
        Path: /api/v4/redirect_location
        Method: GET
        """
        url = "/api/v4/redirect_location"
        return self.request("GET", url, params=kwargs)

    def get_image_by_url(self, **kwargs) -> Any:
        """Get an image by url
        
        Path: /api/v4/image
        Method: GET
        """
        url = "/api/v4/image"
        return self.request("GET", url, params=kwargs)

    def upgrade_to_enterprise(self, **kwargs) -> Any:
        """Executes an inplace upgrade from Team Edition to Enterprise Edition
        
        Path: /api/v4/upgrade_to_enterprise
        Method: POST
        """
        url = "/api/v4/upgrade_to_enterprise"
        return self.request("POST", url, data=kwargs)

    def upgrade_to_enterprise_status(self, **kwargs) -> Any:
        """Get the current status for the inplace upgrade from Team Edition to Enterprise Edition
        
        Path: /api/v4/upgrade_to_enterprise/status
        Method: GET
        """
        url = "/api/v4/upgrade_to_enterprise/status"
        return self.request("GET", url, params=kwargs)

    def is_allowed_to_upgrade_to_enterprise(self, **kwargs) -> Any:
        """Check if the user is allowed to upgrade to Enterprise Edition
        
        Path: /api/v4/upgrade_to_enterprise/allowed
        Method: GET
        """
        url = "/api/v4/upgrade_to_enterprise/allowed"
        return self.request("GET", url, params=kwargs)

    def restart_server(self, **kwargs) -> Any:
        """Restart the system after an upgrade from Team Edition to Enterprise Edition
        
        Path: /api/v4/restart
        Method: POST
        """
        url = "/api/v4/restart"
        return self.request("POST", url, data=kwargs)

    def check_integrity(self, **kwargs) -> Any:
        """Perform a database integrity check
        
        Path: /api/v4/integrity
        Method: POST
        """
        url = "/api/v4/integrity"
        return self.request("POST", url, data=kwargs)

    def generate_support_packet(self, **kwargs) -> Any:
        """Download a zip file which contains helpful and useful information for troubleshooting your mattermost instance.
        
        Path: /api/v4/system/support_packet
        Method: GET
        """
        url = "/api/v4/system/support_packet"
        return self.request("GET", url, params=kwargs)
