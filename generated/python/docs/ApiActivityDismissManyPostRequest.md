# ApiActivityDismissManyPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[Dict[str, object]]** | List of objects with item_type and item_key (required) | 

## Example

```python
from shelfmark_client.models.api_activity_dismiss_many_post_request import ApiActivityDismissManyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiActivityDismissManyPostRequest from a JSON string
api_activity_dismiss_many_post_request_instance = ApiActivityDismissManyPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiActivityDismissManyPostRequest.to_json())

# convert the object into a dict
api_activity_dismiss_many_post_request_dict = api_activity_dismiss_many_post_request_instance.to_dict()
# create an instance of ApiActivityDismissManyPostRequest from a dict
api_activity_dismiss_many_post_request_from_dict = ApiActivityDismissManyPostRequest.from_dict(api_activity_dismiss_many_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


