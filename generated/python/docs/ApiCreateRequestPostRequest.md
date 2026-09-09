# ApiCreateRequestPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**book_data** | **Dict[str, object]** | Book metadata object (required) | 
**context** | **Dict[str, object]** | source, content_type, and request_level | 
**release_data** | **Dict[str, object]** | Specific release when requesting a file | [optional] 
**note** | **str** | Note for admins | [optional] 
**on_behalf_of_user_id** | **int** | Admin-only target user | [optional] 

## Example

```python
from shelfmark_client.models.api_create_request_post_request import ApiCreateRequestPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCreateRequestPostRequest from a JSON string
api_create_request_post_request_instance = ApiCreateRequestPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiCreateRequestPostRequest.to_json())

# convert the object into a dict
api_create_request_post_request_dict = api_create_request_post_request_instance.to_dict()
# create an instance of ApiCreateRequestPostRequest from a dict
api_create_request_post_request_from_dict = ApiCreateRequestPostRequest.from_dict(api_create_request_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


