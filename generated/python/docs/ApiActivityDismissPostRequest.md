# ApiActivityDismissPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | **str** | Item kind such as download or request (required) | 
**item_key** | **str** | Dismiss key such as download:&lt;task_id&gt; (required) | 

## Example

```python
from shelfmark_client.models.api_activity_dismiss_post_request import ApiActivityDismissPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiActivityDismissPostRequest from a JSON string
api_activity_dismiss_post_request_instance = ApiActivityDismissPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiActivityDismissPostRequest.to_json())

# convert the object into a dict
api_activity_dismiss_post_request_dict = api_activity_dismiss_post_request_instance.to_dict()
# create an instance of ApiActivityDismissPostRequest from a dict
api_activity_dismiss_post_request_from_dict = ApiActivityDismissPostRequest.from_dict(api_activity_dismiss_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


