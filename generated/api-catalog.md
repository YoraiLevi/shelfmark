<!-- catalog: 69 method/path pairs, 61 paths -->
### Spec and health

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/health` | `api_health_get` | Health check endpoint for container orchestration. |
| GET | `/api/openapi.json` | `api_openapi_json_get` | OpenAPI 3 description of the live HTTP API. |
| GET | `/openapi.json` | `openapi_json_get` | OpenAPI 3 description of the live HTTP API. |

### Auth

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/auth/check` | `api_auth_check_get` | Check if user has a valid session. |
| POST | `/api/auth/login` | `api_login_post` | Login endpoint that validates credentials and creates a session. |
| POST | `/api/auth/logout` | `api_logout_post` | Logout endpoint that clears the session. |
| GET | `/api/auth/oidc/callback` | `oidc_callback_get` | Handle OIDC callback from identity provider. |
| GET | `/api/auth/oidc/login` | `oidc_login_get` | Initiate OIDC login flow and redirect to the provider. |

### Metadata search

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| POST | `/api/metadata/book/{provider}/targets/batch` | `api_metadata_book_targets_batch_post` | Get provider-managed list/status targets for multiple books. |
| GET | `/api/metadata/book/{provider}/{book_id}` | `api_metadata_book_get` | Get detailed book information from a metadata provider. |
| GET | `/api/metadata/book/{provider}/{book_id}/targets` | `api_metadata_book_targets_get` | Get provider-managed list/status targets for a specific book. |
| PUT | `/api/metadata/book/{provider}/{book_id}/targets` | `api_metadata_book_targets_update_put` | Set whether a book belongs to a provider-managed list or shelf. |
| GET | `/api/metadata/config` | `api_metadata_config_get` | Return provider-specific metadata search config for the active session. |
| GET | `/api/metadata/field-options` | `api_metadata_field_options_get` | Return dynamic search-field options for a metadata provider. |
| GET | `/api/metadata/providers` | `api_metadata_providers_get` | Get list of available metadata providers. |
| GET | `/api/metadata/search` | `api_metadata_search_get` | Search for books using the configured metadata provider. |

### Releases and files

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/covers/{cover_id}` | `api_cover_get` | Serve a cached book cover image. |
| GET | `/api/localdownload` | `api_local_download_get` | Download an EPUB file from local storage if available. |
| GET | `/api/release-sources` | `api_release_sources_get` | Get available release sources from the plugin registry. |
| GET | `/api/release-sources/{source_name}/records/{record_id}` | `api_release_source_record_get` | Resolve a source-native browse record for a release source. |
| GET | `/api/releases` | `api_releases_get` | Search for downloadable releases of a book. |
| POST | `/api/releases/download` | `api_download_release_post` | Queue a release for download. |
| POST | `/api/releases/inspect` | `api_inspect_release_post` | Inspect a release before queueing a download. |

### Queue and downloads

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| DELETE | `/api/download/{book_id}/cancel` | `api_cancel_download_delete` | Cancel a download. |
| POST | `/api/download/{book_id}/retry` | `api_retry_download_post` | Retry a failed download. |
| GET | `/api/downloads/active` | `api_active_downloads_get` | Get list of currently active downloads. |
| GET | `/api/queue/order` | `api_queue_order_get` | Get current queue order for display. |
| POST | `/api/queue/reorder` | `api_reorder_queue_post` | Bulk reorder queue by setting new priorities. |
| PUT | `/api/queue/{book_id}/priority` | `api_set_priority_put` | Set priority for a queued book. |
| GET | `/api/status` | `api_status_get` | Get current download queue status. |

### Activity

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| POST | `/api/activity/dismiss` | `api_activity_dismiss_post` | Dismiss one activity item. |
| POST | `/api/activity/dismiss-many` | `api_activity_dismiss_many_post` | Dismiss many activity items. |
| DELETE | `/api/activity/history` | `api_activity_history_clear_delete` | Clear activity history. |
| GET | `/api/activity/history` | `api_activity_history_get` | List activity history. |
| GET | `/api/activity/snapshot` | `api_activity_snapshot_get` | Return the current activity snapshot for the viewer. |

### Requests (multi-user)

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/request-policy` | `api_request_policy_get` | Return request policy for the current user. |
| GET | `/api/requests` | `api_list_requests_get` | List the current user's book requests. |
| POST | `/api/requests` | `api_create_request_post` | Submit a book request. |
| POST | `/api/requests/batch` | `api_create_requests_batch_post` | Submit many book requests. |
| DELETE | `/api/requests/{request_id}` | `api_cancel_request_delete` | Cancel one of the current user's requests. |

### Settings and onboarding

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/config` | `api_config_get` | Get application configuration for frontend. |
| GET | `/api/onboarding` | `api_onboarding_get_get` | Get onboarding configuration including steps, fields, and current values. |
| POST | `/api/onboarding` | `api_onboarding_save_post` | Save onboarding settings and mark as complete. |
| POST | `/api/onboarding/skip` | `api_onboarding_skip_post` | Skip onboarding and mark as complete without saving any settings. |
| GET | `/api/settings` | `api_settings_get_all_get` | Get all settings tabs with their fields and current values. |
| GET | `/api/settings/{tab_name}` | `api_settings_get_tab_get` | Get settings for a specific tab. |
| PUT | `/api/settings/{tab_name}` | `api_settings_update_tab_put` | Update settings for a specific tab. |
| POST | `/api/settings/{tab_name}/action/{action_key}` | `api_settings_execute_action_post` | Execute a settings action (e.g., test connection). |

### Users

| Method | Path | operationId | Use |
| :--- | :--- | :--- | :--- |
| GET | `/api/admin/booklore-options` | `admin_booklore_options_get` | List Booklore libraries for admin settings. |
| GET | `/api/admin/download-defaults` | `admin_download_defaults_get` | Return default download destination settings for new users. |
| GET | `/api/admin/requests` | `api_admin_list_requests_get` | Admin list of book requests. |
| GET | `/api/admin/requests/count` | `api_admin_request_counts_get` | Admin counts of pending book requests. |
| POST | `/api/admin/requests/{request_id}/fulfil` | `api_admin_fulfil_request_post` | Fulfil a book request. |
| POST | `/api/admin/requests/{request_id}/reject` | `api_admin_reject_request_post` | Reject a book request. |
| GET | `/api/admin/settings/overrides-summary` | `admin_settings_overrides_summary_get` | Summarize per-user settings overrides. |
| GET | `/api/admin/users` | `admin_list_users_get` | List all users. |
| POST | `/api/admin/users` | `admin_create_user_post` | Create a new user with password authentication. |
| POST | `/api/admin/users/sync-cwa` | `admin_sync_cwa_users_post` | Manually sync users from Calibre-Web into users.db. |
| DELETE | `/api/admin/users/{user_id}` | `admin_delete_user_delete` | Delete a user. |
| GET | `/api/admin/users/{user_id}` | `admin_get_user_get` | Get a user by ID with their settings. |
| PUT | `/api/admin/users/{user_id}` | `admin_update_user_put` | Update user fields and/or settings. |
| GET | `/api/admin/users/{user_id}/delivery-preferences` | `admin_get_delivery_preferences_get` | Return delivery preferences for one user. |
| GET | `/api/admin/users/{user_id}/effective-settings` | `admin_get_effective_settings_get` | Return merged settings for one user. |
| GET | `/api/admin/users/{user_id}/notification-preferences` | `admin_get_notification_preferences_get` | Return notification preferences for one user. |
| POST | `/api/admin/users/{user_id}/notification-preferences/test` | `admin_test_notification_preferences_post` | Send a test notification for one user. |
| GET | `/api/admin/users/{user_id}/search-preferences` | `admin_get_search_preferences_get` | Return search preferences for one user. |
| PUT | `/api/users/me` | `users_me_update_put` | Update the current user. |
| GET | `/api/users/me/edit-context` | `users_me_edit_context_get` | Return edit-form context for the current user. |
| POST | `/api/users/me/notification-preferences/test` | `users_me_test_notification_preferences_post` | Send a test notification to the current user. |
