# ApiInspectReleasePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Release source name (required) | 
**source_id** | **str** | ID within the source (required) | 

## Example

```python
from shelfmark_client.models.api_inspect_release_post_request import ApiInspectReleasePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInspectReleasePostRequest from a JSON string
api_inspect_release_post_request_instance = ApiInspectReleasePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiInspectReleasePostRequest.to_json())

# convert the object into a dict
api_inspect_release_post_request_dict = api_inspect_release_post_request_instance.to_dict()
# create an instance of ApiInspectReleasePostRequest from a dict
api_inspect_release_post_request_from_dict = ApiInspectReleasePostRequest.from_dict(api_inspect_release_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


