# shelfmark_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_booklore_options_get**](DefaultApi.md#admin_booklore_options_get) | **GET** /api/admin/booklore-options | List Booklore libraries for admin settings
[**admin_create_user_post**](DefaultApi.md#admin_create_user_post) | **POST** /api/admin/users | Create a new user with password authentication.
[**admin_delete_user_delete**](DefaultApi.md#admin_delete_user_delete) | **DELETE** /api/admin/users/{user_id} | Delete a user.
[**admin_download_defaults_get**](DefaultApi.md#admin_download_defaults_get) | **GET** /api/admin/download-defaults | Default download destination for new users
[**admin_get_delivery_preferences_get**](DefaultApi.md#admin_get_delivery_preferences_get) | **GET** /api/admin/users/{user_id}/delivery-preferences | Delivery preferences for one user
[**admin_get_effective_settings_get**](DefaultApi.md#admin_get_effective_settings_get) | **GET** /api/admin/users/{user_id}/effective-settings | Merged settings for one user
[**admin_get_notification_preferences_get**](DefaultApi.md#admin_get_notification_preferences_get) | **GET** /api/admin/users/{user_id}/notification-preferences | Notification preferences for one user
[**admin_get_search_preferences_get**](DefaultApi.md#admin_get_search_preferences_get) | **GET** /api/admin/users/{user_id}/search-preferences | Search preferences for one user
[**admin_get_user_get**](DefaultApi.md#admin_get_user_get) | **GET** /api/admin/users/{user_id} | Get a user by ID with their settings.
[**admin_list_users_get**](DefaultApi.md#admin_list_users_get) | **GET** /api/admin/users | List all users.
[**admin_settings_overrides_summary_get**](DefaultApi.md#admin_settings_overrides_summary_get) | **GET** /api/admin/settings/overrides-summary | Summary of per-user settings overrides
[**admin_sync_cwa_users_post**](DefaultApi.md#admin_sync_cwa_users_post) | **POST** /api/admin/users/sync-cwa | Manually sync users from Calibre-Web into users.db.
[**admin_test_notification_preferences_post**](DefaultApi.md#admin_test_notification_preferences_post) | **POST** /api/admin/users/{user_id}/notification-preferences/test | Send a test notification for one user
[**admin_update_user_put**](DefaultApi.md#admin_update_user_put) | **PUT** /api/admin/users/{user_id} | Update user fields and/or settings.
[**api_active_downloads_get**](DefaultApi.md#api_active_downloads_get) | **GET** /api/downloads/active | Get list of currently active downloads.
[**api_activity_dismiss_many_post**](DefaultApi.md#api_activity_dismiss_many_post) | **POST** /api/activity/dismiss-many | Dismiss many activity items
[**api_activity_dismiss_post**](DefaultApi.md#api_activity_dismiss_post) | **POST** /api/activity/dismiss | Dismiss one activity item
[**api_activity_history_clear_delete**](DefaultApi.md#api_activity_history_clear_delete) | **DELETE** /api/activity/history | Clear activity history
[**api_activity_history_get**](DefaultApi.md#api_activity_history_get) | **GET** /api/activity/history | List activity history
[**api_activity_snapshot_get**](DefaultApi.md#api_activity_snapshot_get) | **GET** /api/activity/snapshot | Current activity snapshot
[**api_admin_fulfil_request_post**](DefaultApi.md#api_admin_fulfil_request_post) | **POST** /api/admin/requests/{request_id}/fulfil | Fulfil a book request
[**api_admin_list_requests_get**](DefaultApi.md#api_admin_list_requests_get) | **GET** /api/admin/requests | Admin list of book requests
[**api_admin_reject_request_post**](DefaultApi.md#api_admin_reject_request_post) | **POST** /api/admin/requests/{request_id}/reject | Reject a book request
[**api_admin_request_counts_get**](DefaultApi.md#api_admin_request_counts_get) | **GET** /api/admin/requests/count | Admin counts of pending book requests
[**api_auth_check_get**](DefaultApi.md#api_auth_check_get) | **GET** /api/auth/check | Check if user has a valid session.
[**api_cancel_download_delete**](DefaultApi.md#api_cancel_download_delete) | **DELETE** /api/download/{book_id}/cancel | Cancel a download.
[**api_cancel_request_delete**](DefaultApi.md#api_cancel_request_delete) | **DELETE** /api/requests/{request_id} | Cancel one of the current user&#39;s requests
[**api_config_get**](DefaultApi.md#api_config_get) | **GET** /api/config | Get application configuration for frontend.
[**api_cover_get**](DefaultApi.md#api_cover_get) | **GET** /api/covers/{cover_id} | Serve a cached book cover image.
[**api_create_request_post**](DefaultApi.md#api_create_request_post) | **POST** /api/requests | Submit a book request
[**api_create_requests_batch_post**](DefaultApi.md#api_create_requests_batch_post) | **POST** /api/requests/batch | Submit many book requests
[**api_download_release_post**](DefaultApi.md#api_download_release_post) | **POST** /api/releases/download | Queue a release for download.
[**api_health_get**](DefaultApi.md#api_health_get) | **GET** /api/health | Health check endpoint for container orchestration.
[**api_inspect_release_post**](DefaultApi.md#api_inspect_release_post) | **POST** /api/releases/inspect | Inspect a release before queueing a download
[**api_list_requests_get**](DefaultApi.md#api_list_requests_get) | **GET** /api/requests | List the current user&#39;s book requests
[**api_local_download_get**](DefaultApi.md#api_local_download_get) | **GET** /api/localdownload | Download an EPUB file from local storage if available.
[**api_login_post**](DefaultApi.md#api_login_post) | **POST** /api/auth/login | Login endpoint that validates credentials and creates a session.
[**api_logout_post**](DefaultApi.md#api_logout_post) | **POST** /api/auth/logout | Logout endpoint that clears the session.
[**api_metadata_book_get**](DefaultApi.md#api_metadata_book_get) | **GET** /api/metadata/book/{provider}/{book_id} | Get detailed book information from a metadata provider.
[**api_metadata_book_targets_batch_post**](DefaultApi.md#api_metadata_book_targets_batch_post) | **POST** /api/metadata/book/{provider}/targets/batch | Get provider-managed list/status targets for multiple books.
[**api_metadata_book_targets_get**](DefaultApi.md#api_metadata_book_targets_get) | **GET** /api/metadata/book/{provider}/{book_id}/targets | Get provider-managed list/status targets for a specific book.
[**api_metadata_book_targets_update_put**](DefaultApi.md#api_metadata_book_targets_update_put) | **PUT** /api/metadata/book/{provider}/{book_id}/targets | Set whether a book belongs to a provider-managed list or shelf.
[**api_metadata_config_get**](DefaultApi.md#api_metadata_config_get) | **GET** /api/metadata/config | Return provider-specific metadata search config for the active session.
[**api_metadata_field_options_get**](DefaultApi.md#api_metadata_field_options_get) | **GET** /api/metadata/field-options | Return dynamic search-field options for a metadata provider.
[**api_metadata_providers_get**](DefaultApi.md#api_metadata_providers_get) | **GET** /api/metadata/providers | Get list of available metadata providers.
[**api_metadata_search_get**](DefaultApi.md#api_metadata_search_get) | **GET** /api/metadata/search | Search for books using the configured metadata provider.
[**api_onboarding_get_get**](DefaultApi.md#api_onboarding_get_get) | **GET** /api/onboarding | Get onboarding configuration including steps, fields, and current values.
[**api_onboarding_save_post**](DefaultApi.md#api_onboarding_save_post) | **POST** /api/onboarding | Save onboarding settings and mark as complete.
[**api_onboarding_skip_post**](DefaultApi.md#api_onboarding_skip_post) | **POST** /api/onboarding/skip | Skip onboarding and mark as complete without saving any settings.
[**api_openapi_json_get**](DefaultApi.md#api_openapi_json_get) | **GET** /api/openapi.json | OpenAPI 3 description of the live HTTP API.
[**api_queue_order_get**](DefaultApi.md#api_queue_order_get) | **GET** /api/queue/order | Get current queue order for display.
[**api_release_source_record_get**](DefaultApi.md#api_release_source_record_get) | **GET** /api/release-sources/{source_name}/records/{record_id} | Resolve a source-native browse record for a release source.
[**api_release_sources_get**](DefaultApi.md#api_release_sources_get) | **GET** /api/release-sources | Get available release sources from the plugin registry.
[**api_releases_get**](DefaultApi.md#api_releases_get) | **GET** /api/releases | Search for downloadable releases of a book.
[**api_reorder_queue_post**](DefaultApi.md#api_reorder_queue_post) | **POST** /api/queue/reorder | Bulk reorder queue by setting new priorities.
[**api_request_policy_get**](DefaultApi.md#api_request_policy_get) | **GET** /api/request-policy | Request policy for the current user
[**api_retry_download_post**](DefaultApi.md#api_retry_download_post) | **POST** /api/download/{book_id}/retry | Retry a failed download.
[**api_set_priority_put**](DefaultApi.md#api_set_priority_put) | **PUT** /api/queue/{book_id}/priority | Set priority for a queued book.
[**api_settings_execute_action_post**](DefaultApi.md#api_settings_execute_action_post) | **POST** /api/settings/{tab_name}/action/{action_key} | Execute a settings action (e.g., test connection).
[**api_settings_get_all_get**](DefaultApi.md#api_settings_get_all_get) | **GET** /api/settings | Get all settings tabs with their fields and current values.
[**api_settings_get_tab_get**](DefaultApi.md#api_settings_get_tab_get) | **GET** /api/settings/{tab_name} | Get settings for a specific tab.
[**api_settings_update_tab_put**](DefaultApi.md#api_settings_update_tab_put) | **PUT** /api/settings/{tab_name} | Update settings for a specific tab.
[**api_status_get**](DefaultApi.md#api_status_get) | **GET** /api/status | Get current download queue status.
[**oidc_callback_get**](DefaultApi.md#oidc_callback_get) | **GET** /api/auth/oidc/callback | Handle OIDC callback from identity provider.
[**oidc_login_get**](DefaultApi.md#oidc_login_get) | **GET** /api/auth/oidc/login | Initiate OIDC login flow and redirect to the provider.
[**openapi_json_get**](DefaultApi.md#openapi_json_get) | **GET** /openapi.json | OpenAPI 3 description of the live HTTP API.
[**users_me_edit_context_get**](DefaultApi.md#users_me_edit_context_get) | **GET** /api/users/me/edit-context | Edit-form context for the current user
[**users_me_test_notification_preferences_post**](DefaultApi.md#users_me_test_notification_preferences_post) | **POST** /api/users/me/notification-preferences/test | Send a test notification to the current user
[**users_me_update_put**](DefaultApi.md#users_me_update_put) | **PUT** /api/users/me | Update the current user


# **admin_booklore_options_get**
> admin_booklore_options_get()

List Booklore libraries for admin settings



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # List Booklore libraries for admin settings
        await api_instance.admin_booklore_options_get()
    except Exception as e:
        print("Exception when calling DefaultApi->admin_booklore_options_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_create_user_post**
> admin_create_user_post()

Create a new user with password authentication.

Create a new user with password authentication.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Create a new user with password authentication.
        await api_instance.admin_create_user_post()
    except Exception as e:
        print("Exception when calling DefaultApi->admin_create_user_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_user_delete**
> admin_delete_user_delete(user_id)

Delete a user.

Delete a user.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    user_id = 56 # int | 

    try:
        # Delete a user.
        await api_instance.admin_delete_user_delete(user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->admin_delete_user_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_download_defaults_get**
> admin_download_defaults_get()

Default download destination for new users



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Default download destination for new users
        await api_instance.admin_download_defaults_get()
    except Exception as e:
        print("Exception when calling DefaultApi->admin_download_defaults_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_delivery_preferences_get**
> admin_get_delivery_preferences_get(user_id)

Delivery preferences for one user



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    user_id = 56 # int | 

    try:
        # Delivery preferences for one user
        await api_instance.admin_get_delivery_preferences_get(user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->admin_get_delivery_preferences_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_effective_settings_get**
> admin_get_effective_settings_get(user_id)

Merged settings for one user



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    user_id = 56 # int | 

    try:
        # Merged settings for one user
        await api_instance.admin_get_effective_settings_get(user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->admin_get_effective_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_notification_preferences_get**
> admin_get_notification_preferences_get(user_id)

Notification preferences for one user



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    user_id = 56 # int | 

    try:
        # Notification preferences for one user
        await api_instance.admin_get_notification_preferences_get(user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->admin_get_notification_preferences_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_search_preferences_get**
> admin_get_search_preferences_get(user_id)

Search preferences for one user



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    user_id = 56 # int | 

    try:
        # Search preferences for one user
        await api_instance.admin_get_search_preferences_get(user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->admin_get_search_preferences_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_user_get**
> admin_get_user_get(user_id)

Get a user by ID with their settings.

Get a user by ID with their settings.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    user_id = 56 # int | 

    try:
        # Get a user by ID with their settings.
        await api_instance.admin_get_user_get(user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->admin_get_user_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_list_users_get**
> admin_list_users_get()

List all users.

List all users.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # List all users.
        await api_instance.admin_list_users_get()
    except Exception as e:
        print("Exception when calling DefaultApi->admin_list_users_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_settings_overrides_summary_get**
> admin_settings_overrides_summary_get()

Summary of per-user settings overrides



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Summary of per-user settings overrides
        await api_instance.admin_settings_overrides_summary_get()
    except Exception as e:
        print("Exception when calling DefaultApi->admin_settings_overrides_summary_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_sync_cwa_users_post**
> admin_sync_cwa_users_post()

Manually sync users from Calibre-Web into users.db.

Manually sync users from Calibre-Web into users.db.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Manually sync users from Calibre-Web into users.db.
        await api_instance.admin_sync_cwa_users_post()
    except Exception as e:
        print("Exception when calling DefaultApi->admin_sync_cwa_users_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_test_notification_preferences_post**
> admin_test_notification_preferences_post(user_id)

Send a test notification for one user



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    user_id = 56 # int | 

    try:
        # Send a test notification for one user
        await api_instance.admin_test_notification_preferences_post(user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->admin_test_notification_preferences_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_user_put**
> admin_update_user_put(user_id)

Update user fields and/or settings.

Update user fields and/or settings.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    user_id = 56 # int | 

    try:
        # Update user fields and/or settings.
        await api_instance.admin_update_user_put(user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->admin_update_user_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_active_downloads_get**
> api_active_downloads_get()

Get list of currently active downloads.

Get list of currently active downloads.

Returns:
    flask.Response: JSON array of active download book IDs.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Get list of currently active downloads.
        await api_instance.api_active_downloads_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_active_downloads_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_activity_dismiss_many_post**
> api_activity_dismiss_many_post()

Dismiss many activity items



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Dismiss many activity items
        await api_instance.api_activity_dismiss_many_post()
    except Exception as e:
        print("Exception when calling DefaultApi->api_activity_dismiss_many_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_activity_dismiss_post**
> api_activity_dismiss_post()

Dismiss one activity item



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Dismiss one activity item
        await api_instance.api_activity_dismiss_post()
    except Exception as e:
        print("Exception when calling DefaultApi->api_activity_dismiss_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_activity_history_clear_delete**
> api_activity_history_clear_delete()

Clear activity history



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Clear activity history
        await api_instance.api_activity_history_clear_delete()
    except Exception as e:
        print("Exception when calling DefaultApi->api_activity_history_clear_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_activity_history_get**
> api_activity_history_get()

List activity history



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # List activity history
        await api_instance.api_activity_history_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_activity_history_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_activity_snapshot_get**
> api_activity_snapshot_get()

Current activity snapshot



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Current activity snapshot
        await api_instance.api_activity_snapshot_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_activity_snapshot_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_admin_fulfil_request_post**
> api_admin_fulfil_request_post(request_id)

Fulfil a book request



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    request_id = 56 # int | 

    try:
        # Fulfil a book request
        await api_instance.api_admin_fulfil_request_post(request_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_admin_fulfil_request_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_admin_list_requests_get**
> api_admin_list_requests_get()

Admin list of book requests



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Admin list of book requests
        await api_instance.api_admin_list_requests_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_admin_list_requests_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_admin_reject_request_post**
> api_admin_reject_request_post(request_id)

Reject a book request



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    request_id = 56 # int | 

    try:
        # Reject a book request
        await api_instance.api_admin_reject_request_post(request_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_admin_reject_request_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_admin_request_counts_get**
> api_admin_request_counts_get()

Admin counts of pending book requests



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Admin counts of pending book requests
        await api_instance.api_admin_request_counts_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_admin_request_counts_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_auth_check_get**
> api_auth_check_get()

Check if user has a valid session.

Check if user has a valid session.

Returns:
    flask.Response: JSON with authentication status, whether auth is required,
    which auth mode is active, and whether user has admin privileges.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Check if user has a valid session.
        await api_instance.api_auth_check_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_auth_check_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_cancel_download_delete**
> api_cancel_download_delete(book_id)

Cancel a download.

Cancel a download.

Path Parameters:
    book_id (str): Book identifier to cancel

Returns:
    flask.Response: JSON status indicating success or failure.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    book_id = 'book_id_example' # str | 

    try:
        # Cancel a download.
        await api_instance.api_cancel_download_delete(book_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_cancel_download_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_cancel_request_delete**
> api_cancel_request_delete(request_id)

Cancel one of the current user's requests



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    request_id = 56 # int | 

    try:
        # Cancel one of the current user's requests
        await api_instance.api_cancel_request_delete(request_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_cancel_request_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_config_get**
> api_config_get()

Get application configuration for frontend.

Get application configuration for frontend.

Uses the dynamic config singleton to ensure settings changes
are reflected without requiring a container restart.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Get application configuration for frontend.
        await api_instance.api_config_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_cover_get**
> api_cover_get(cover_id, url)

Serve a cached book cover image.

Serve a cached book cover image.

This endpoint proxies and caches cover images from external sources.
Images are cached to disk for faster subsequent requests.

Path Parameters:
    cover_id (str): Cover identifier (book ID or composite key for universal mode)

Query Parameters:
    url (str): Base64-encoded original image URL (required on first request)

Returns:
    flask.Response: Binary image data with appropriate Content-Type, or 404.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    cover_id = 'cover_id_example' # str | 
    url = 'url_example' # str | Base64-encoded original image URL (required on first request)

    try:
        # Serve a cached book cover image.
        await api_instance.api_cover_get(cover_id, url)
    except Exception as e:
        print("Exception when calling DefaultApi->api_cover_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cover_id** | **str**|  | 
 **url** | **str**| Base64-encoded original image URL (required on first request) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_create_request_post**
> api_create_request_post()

Submit a book request



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Submit a book request
        await api_instance.api_create_request_post()
    except Exception as e:
        print("Exception when calling DefaultApi->api_create_request_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_create_requests_batch_post**
> api_create_requests_batch_post()

Submit many book requests



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Submit many book requests
        await api_instance.api_create_requests_batch_post()
    except Exception as e:
        print("Exception when calling DefaultApi->api_create_requests_batch_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_download_release_post**
> api_download_release_post(api_download_release_post_request)

Queue a release for download.

Queue a release for download.

This endpoint is used when downloading from the ReleaseModal where the
frontend already has all the release data from the search results.

Request Body (JSON):
    source (str): Release source (e.g., "direct_download")
    source_id (str): ID within the source (e.g., AA MD5 hash)
    title (str): Book title
    format (str, optional): File format
    size (str, optional): Human-readable size
    extra (dict, optional): Additional metadata

Returns:
    flask.Response: JSON status object indicating success or failure.

### Example


```python
import shelfmark_client
from shelfmark_client.models.api_download_release_post_request import ApiDownloadReleasePostRequest
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    api_download_release_post_request = shelfmark_client.ApiDownloadReleasePostRequest() # ApiDownloadReleasePostRequest | 

    try:
        # Queue a release for download.
        await api_instance.api_download_release_post(api_download_release_post_request)
    except Exception as e:
        print("Exception when calling DefaultApi->api_download_release_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_download_release_post_request** | [**ApiDownloadReleasePostRequest**](ApiDownloadReleasePostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_health_get**
> api_health_get()

Health check endpoint for container orchestration.

Health check endpoint for container orchestration.

No authentication required.

Returns:
    flask.Response: JSON with status "ok" and optional degraded features.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Health check endpoint for container orchestration.
        await api_instance.api_health_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_inspect_release_post**
> api_inspect_release_post()

Inspect a release before queueing a download



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Inspect a release before queueing a download
        await api_instance.api_inspect_release_post()
    except Exception as e:
        print("Exception when calling DefaultApi->api_inspect_release_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_list_requests_get**
> api_list_requests_get()

List the current user's book requests



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # List the current user's book requests
        await api_instance.api_list_requests_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_list_requests_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_local_download_get**
> api_local_download_get(id=id)

Download an EPUB file from local storage if available.

Download an EPUB file from local storage if available.

Query Parameters:
    id (str): Book identifier (MD5 hash)

Returns:
    flask.Response: The EPUB file if found, otherwise an error response.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    id = 'id_example' # str | Book identifier (MD5 hash) (optional)

    try:
        # Download an EPUB file from local storage if available.
        await api_instance.api_local_download_get(id=id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_local_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Book identifier (MD5 hash) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_login_post**
> api_login_post()

Login endpoint that validates credentials and creates a session.

Login endpoint that validates credentials and creates a session.

Supports both built-in credentials and CWA database authentication.
Includes rate limiting: 10 failed attempts = 30 minute lockout.

Request Body:
    username (str): Username
    password (str): Password
    remember_me (bool): Whether to extend session duration

Returns:
    flask.Response: JSON with success status or error message.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Login endpoint that validates credentials and creates a session.
        await api_instance.api_login_post()
    except Exception as e:
        print("Exception when calling DefaultApi->api_login_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_logout_post**
> api_logout_post()

Logout endpoint that clears the session.

Logout endpoint that clears the session.

For proxy auth, returns the logout URL if configured.

Returns:
    flask.Response: JSON with success status and optional logout_url.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Logout endpoint that clears the session.
        await api_instance.api_logout_post()
    except Exception as e:
        print("Exception when calling DefaultApi->api_logout_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_metadata_book_get**
> api_metadata_book_get(provider, book_id)

Get detailed book information from a metadata provider.

Get detailed book information from a metadata provider.

Path Parameters:
    provider (str): Provider name (e.g., "hardcover", "openlibrary")
    book_id (str): Book ID in the provider's system

Returns:
    flask.Response: JSON with book details.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    provider = 'provider_example' # str | 
    book_id = 'book_id_example' # str | 

    try:
        # Get detailed book information from a metadata provider.
        await api_instance.api_metadata_book_get(provider, book_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_metadata_book_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **book_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_metadata_book_targets_batch_post**
> api_metadata_book_targets_batch_post(provider)

Get provider-managed list/status targets for multiple books.

Get provider-managed list/status targets for multiple books.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Get provider-managed list/status targets for multiple books.
        await api_instance.api_metadata_book_targets_batch_post(provider)
    except Exception as e:
        print("Exception when calling DefaultApi->api_metadata_book_targets_batch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_metadata_book_targets_get**
> api_metadata_book_targets_get(provider, book_id)

Get provider-managed list/status targets for a specific book.

Get provider-managed list/status targets for a specific book.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    provider = 'provider_example' # str | 
    book_id = 'book_id_example' # str | 

    try:
        # Get provider-managed list/status targets for a specific book.
        await api_instance.api_metadata_book_targets_get(provider, book_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_metadata_book_targets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **book_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_metadata_book_targets_update_put**
> api_metadata_book_targets_update_put(provider, book_id)

Set whether a book belongs to a provider-managed list or shelf.

Set whether a book belongs to a provider-managed list or shelf.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    provider = 'provider_example' # str | 
    book_id = 'book_id_example' # str | 

    try:
        # Set whether a book belongs to a provider-managed list or shelf.
        await api_instance.api_metadata_book_targets_update_put(provider, book_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_metadata_book_targets_update_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **book_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_metadata_config_get**
> api_metadata_config_get()

Return provider-specific metadata search config for the active session.

Return provider-specific metadata search config for the active session.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Return provider-specific metadata search config for the active session.
        await api_instance.api_metadata_config_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_metadata_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_metadata_field_options_get**
> api_metadata_field_options_get()

Return dynamic search-field options for a metadata provider.

Return dynamic search-field options for a metadata provider.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Return dynamic search-field options for a metadata provider.
        await api_instance.api_metadata_field_options_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_metadata_field_options_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_metadata_providers_get**
> api_metadata_providers_get()

Get list of available metadata providers.

Get list of available metadata providers.

Returns:
    flask.Response: JSON with list of providers and their status.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Get list of available metadata providers.
        await api_instance.api_metadata_providers_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_metadata_providers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_metadata_search_get**
> api_metadata_search_get(query, limit=limit, sort=sort, provider=provider, page=page, content_type=content_type)

Search for books using the configured metadata provider.

Search for books using the configured metadata provider.

Query Parameters:
    query (str): Search query (required)
    limit (int): Maximum number of results (default: 40, max: 100)
    sort (str): Sort order - relevance, popularity, rating, newest, oldest (default: relevance)
    [dynamic fields]: Provider-specific search fields passed as query params

Returns:
    flask.Response: JSON with list of books from metadata provider.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    query = 'query_example' # str | Search query (required)
    limit = 56 # int | Maximum number of results (default: 40, max: 100) (optional)
    sort = 'sort_example' # str | Sort order - relevance, popularity, rating, newest, oldest (default: relevance) (optional)
    provider = 'provider_example' # str | Metadata provider name (openlibrary, hardcover, googlebooks, moly). (optional)
    page = 1 # int | Result page (1-based). (optional) (default to 1)
    content_type = 'ebook' # str | ebook, audiobook, or combined. (optional) (default to 'ebook')

    try:
        # Search for books using the configured metadata provider.
        await api_instance.api_metadata_search_get(query, limit=limit, sort=sort, provider=provider, page=page, content_type=content_type)
    except Exception as e:
        print("Exception when calling DefaultApi->api_metadata_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query (required) | 
 **limit** | **int**| Maximum number of results (default: 40, max: 100) | [optional] 
 **sort** | **str**| Sort order - relevance, popularity, rating, newest, oldest (default: relevance) | [optional] 
 **provider** | **str**| Metadata provider name (openlibrary, hardcover, googlebooks, moly). | [optional] 
 **page** | **int**| Result page (1-based). | [optional] [default to 1]
 **content_type** | **str**| ebook, audiobook, or combined. | [optional] [default to &#39;ebook&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_onboarding_get_get**
> api_onboarding_get_get()

Get onboarding configuration including steps, fields, and current values.

Get onboarding configuration including steps, fields, and current values.

Returns:
    flask.Response: JSON with onboarding steps and values.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Get onboarding configuration including steps, fields, and current values.
        await api_instance.api_onboarding_get_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_onboarding_get_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_onboarding_save_post**
> api_onboarding_save_post()

Save onboarding settings and mark as complete.

Save onboarding settings and mark as complete.

Request Body:
    JSON object with all onboarding field values

Returns:
    flask.Response: JSON with success/error status.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Save onboarding settings and mark as complete.
        await api_instance.api_onboarding_save_post()
    except Exception as e:
        print("Exception when calling DefaultApi->api_onboarding_save_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_onboarding_skip_post**
> api_onboarding_skip_post()

Skip onboarding and mark as complete without saving any settings.

Skip onboarding and mark as complete without saving any settings.

Returns:
    flask.Response: JSON with success status.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Skip onboarding and mark as complete without saving any settings.
        await api_instance.api_onboarding_skip_post()
    except Exception as e:
        print("Exception when calling DefaultApi->api_onboarding_skip_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_openapi_json_get**
> api_openapi_json_get()

OpenAPI 3 description of the live HTTP API.

OpenAPI 3 description of the live HTTP API.

No authentication required.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # OpenAPI 3 description of the live HTTP API.
        await api_instance.api_openapi_json_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_openapi_json_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_queue_order_get**
> api_queue_order_get()

Get current queue order for display.

Get current queue order for display.

Returns:
    flask.Response: JSON array of queued books with their order and priorities.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Get current queue order for display.
        await api_instance.api_queue_order_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_queue_order_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_release_source_record_get**
> api_release_source_record_get(source_name, record_id)

Resolve a source-native browse record for a release source.

Resolve a source-native browse record for a release source.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    source_name = 'source_name_example' # str | 
    record_id = 'record_id_example' # str | 

    try:
        # Resolve a source-native browse record for a release source.
        await api_instance.api_release_source_record_get(source_name, record_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_release_source_record_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_name** | **str**|  | 
 **record_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_release_sources_get**
> api_release_sources_get()

Get available release sources from the plugin registry.

Get available release sources from the plugin registry.

Returns:
    flask.Response: JSON list of available release sources.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Get available release sources from the plugin registry.
        await api_instance.api_release_sources_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_release_sources_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_releases_get**
> api_releases_get(provider, book_id, source=source, query=query, isbn=isbn, title=title, author=author, content_type=content_type, expand_search=expand_search, languages=languages, manual_query=manual_query, indexers=indexers)

Search for downloadable releases of a book.

Search for downloadable releases of a book.

This endpoint takes book metadata and searches available release sources
(e.g., Anna's Archive, Libgen) for downloadable files.

Query Parameters:
    provider (str): Metadata provider name (required)
    book_id (str): Book ID from metadata provider (required)
    source (str): Release source to search (optional, default: all)

Returns:
    flask.Response: JSON with list of available releases.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    provider = 'provider_example' # str | Metadata provider name (required)
    book_id = 'book_id_example' # str | Book ID from metadata provider (required)
    source = 'source_example' # str | Release source to search (optional, default: all) (optional)
    query = 'query_example' # str | Browse/manual query text. With source=, used instead of provider+book_id. (optional)
    isbn = ['isbn_example'] # List[str] | ISBN-10 or ISBN-13 filter. Repeat the parameter for multiple values. (optional)
    title = 'title_example' # str | Title override or browse title filter. (optional)
    author = 'author_example' # str | Author override or browse author filter. (optional)
    content_type = 'ebook' # str |  (optional) (default to 'ebook')
    expand_search = False # bool | Skip ISBN-first matching and search by title/author. (optional) (default to False)
    languages = 'languages_example' # str | Comma-separated ISO 639-1 language codes. (optional)
    manual_query = 'manual_query_example' # str |  (optional)
    indexers = 'indexers_example' # str | Comma-separated Prowlarr indexer names. (optional)

    try:
        # Search for downloadable releases of a book.
        await api_instance.api_releases_get(provider, book_id, source=source, query=query, isbn=isbn, title=title, author=author, content_type=content_type, expand_search=expand_search, languages=languages, manual_query=manual_query, indexers=indexers)
    except Exception as e:
        print("Exception when calling DefaultApi->api_releases_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Metadata provider name (required) | 
 **book_id** | **str**| Book ID from metadata provider (required) | 
 **source** | **str**| Release source to search (optional, default: all) | [optional] 
 **query** | **str**| Browse/manual query text. With source&#x3D;, used instead of provider+book_id. | [optional] 
 **isbn** | [**List[str]**](str.md)| ISBN-10 or ISBN-13 filter. Repeat the parameter for multiple values. | [optional] 
 **title** | **str**| Title override or browse title filter. | [optional] 
 **author** | **str**| Author override or browse author filter. | [optional] 
 **content_type** | **str**|  | [optional] [default to &#39;ebook&#39;]
 **expand_search** | **bool**| Skip ISBN-first matching and search by title/author. | [optional] [default to False]
 **languages** | **str**| Comma-separated ISO 639-1 language codes. | [optional] 
 **manual_query** | **str**|  | [optional] 
 **indexers** | **str**| Comma-separated Prowlarr indexer names. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_reorder_queue_post**
> api_reorder_queue_post()

Bulk reorder queue by setting new priorities.

Bulk reorder queue by setting new priorities.

Request Body:
    book_priorities (dict): Mapping of book_id to new priority

Returns:
    flask.Response: JSON status indicating success or failure.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Bulk reorder queue by setting new priorities.
        await api_instance.api_reorder_queue_post()
    except Exception as e:
        print("Exception when calling DefaultApi->api_reorder_queue_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_request_policy_get**
> api_request_policy_get()

Request policy for the current user



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Request policy for the current user
        await api_instance.api_request_policy_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_request_policy_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_retry_download_post**
> api_retry_download_post(book_id)

Retry a failed download.

Retry a failed download.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    book_id = 'book_id_example' # str | 

    try:
        # Retry a failed download.
        await api_instance.api_retry_download_post(book_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_retry_download_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_set_priority_put**
> api_set_priority_put(book_id)

Set priority for a queued book.

Set priority for a queued book.

Path Parameters:
    book_id (str): Book identifier

Request Body:
    priority (int): New priority level (lower number = higher priority)

Returns:
    flask.Response: JSON status indicating success or failure.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    book_id = 'book_id_example' # str | 

    try:
        # Set priority for a queued book.
        await api_instance.api_set_priority_put(book_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_set_priority_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_settings_execute_action_post**
> api_settings_execute_action_post(tab_name, action_key)

Execute a settings action (e.g., test connection).

Execute a settings action (e.g., test connection).

Path Parameters:
    tab_name (str): Settings tab name
    action_key (str): Action key to execute

Request Body (optional):
    JSON object with current form values (unsaved)

Returns:
    flask.Response: JSON with action result.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    tab_name = 'tab_name_example' # str | 
    action_key = 'action_key_example' # str | 

    try:
        # Execute a settings action (e.g., test connection).
        await api_instance.api_settings_execute_action_post(tab_name, action_key)
    except Exception as e:
        print("Exception when calling DefaultApi->api_settings_execute_action_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tab_name** | **str**|  | 
 **action_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_settings_get_all_get**
> api_settings_get_all_get()

Get all settings tabs with their fields and current values.

Get all settings tabs with their fields and current values.

Returns:
    flask.Response: JSON with all settings tabs.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Get all settings tabs with their fields and current values.
        await api_instance.api_settings_get_all_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_settings_get_all_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_settings_get_tab_get**
> api_settings_get_tab_get(tab_name)

Get settings for a specific tab.

Get settings for a specific tab.

Path Parameters:
    tab_name (str): Settings tab name (e.g., "general", "hardcover")

Returns:
    flask.Response: JSON with tab settings and values.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    tab_name = 'tab_name_example' # str | 

    try:
        # Get settings for a specific tab.
        await api_instance.api_settings_get_tab_get(tab_name)
    except Exception as e:
        print("Exception when calling DefaultApi->api_settings_get_tab_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tab_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_settings_update_tab_put**
> api_settings_update_tab_put(tab_name)

Update settings for a specific tab.

Update settings for a specific tab.

Path Parameters:
    tab_name (str): Settings tab name

Request Body:
    JSON object with setting keys and values to update.

Returns:
    flask.Response: JSON with update result.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)
    tab_name = 'tab_name_example' # str | 

    try:
        # Update settings for a specific tab.
        await api_instance.api_settings_update_tab_put(tab_name)
    except Exception as e:
        print("Exception when calling DefaultApi->api_settings_update_tab_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tab_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_status_get**
> api_status_get()

Get current download queue status.

Get current download queue status.

Returns:
    flask.Response: JSON object with queue status.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Get current download queue status.
        await api_instance.api_status_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_callback_get**
> oidc_callback_get()

Handle OIDC callback from identity provider.

Handle OIDC callback from identity provider.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Handle OIDC callback from identity provider.
        await api_instance.oidc_callback_get()
    except Exception as e:
        print("Exception when calling DefaultApi->oidc_callback_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_login_get**
> oidc_login_get()

Initiate OIDC login flow and redirect to the provider.

Initiate OIDC login flow and redirect to the provider.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Initiate OIDC login flow and redirect to the provider.
        await api_instance.oidc_login_get()
    except Exception as e:
        print("Exception when calling DefaultApi->oidc_login_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_json_get**
> openapi_json_get()

OpenAPI 3 description of the live HTTP API.

OpenAPI 3 description of the live HTTP API.

No authentication required.

### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # OpenAPI 3 description of the live HTTP API.
        await api_instance.openapi_json_get()
    except Exception as e:
        print("Exception when calling DefaultApi->openapi_json_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_edit_context_get**
> users_me_edit_context_get()

Edit-form context for the current user



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Edit-form context for the current user
        await api_instance.users_me_edit_context_get()
    except Exception as e:
        print("Exception when calling DefaultApi->users_me_edit_context_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_test_notification_preferences_post**
> users_me_test_notification_preferences_post()

Send a test notification to the current user



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Send a test notification to the current user
        await api_instance.users_me_test_notification_preferences_post()
    except Exception as e:
        print("Exception when calling DefaultApi->users_me_test_notification_preferences_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_update_put**
> users_me_update_put()

Update the current user



### Example


```python
import shelfmark_client
from shelfmark_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = shelfmark_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with shelfmark_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = shelfmark_client.DefaultApi(api_client)

    try:
        # Update the current user
        await api_instance.users_me_update_put()
    except Exception as e:
        print("Exception when calling DefaultApi->users_me_update_put: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Authentication required when AUTH_METHOD is not none |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

