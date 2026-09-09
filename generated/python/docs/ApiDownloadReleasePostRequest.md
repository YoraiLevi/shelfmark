# ApiDownloadReleasePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Release source (e.g., \&quot;direct_download\&quot;) | 
**source_id** | **str** | ID within the source (e.g., AA MD5 hash) | 
**title** | **str** | Book title | [optional] 
**format** | **str** | File format | [optional] 
**size** | **str** | Human-readable size | [optional] 
**extra** | **Dict[str, object]** | Additional metadata | [optional] 
**priority** | **int** | Queue priority, lower is sooner | [optional] 

## Example

```python
from shelfmark_client.models.api_download_release_post_request import ApiDownloadReleasePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDownloadReleasePostRequest from a JSON string
api_download_release_post_request_instance = ApiDownloadReleasePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiDownloadReleasePostRequest.to_json())

# convert the object into a dict
api_download_release_post_request_dict = api_download_release_post_request_instance.to_dict()
# create an instance of ApiDownloadReleasePostRequest from a dict
api_download_release_post_request_from_dict = ApiDownloadReleasePostRequest.from_dict(api_download_release_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


