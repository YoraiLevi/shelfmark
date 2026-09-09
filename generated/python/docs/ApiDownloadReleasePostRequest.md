# ApiDownloadReleasePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Release source name. | 
**source_id** | **str** | ID within the source, such as an MD5. | 
**title** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**extra** | **object** |  | [optional] 
**priority** | **int** |  | [optional] [default to 0]

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


