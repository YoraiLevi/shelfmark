# ApiReorderQueuePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**book_priorities** | **Dict[str, object]** | Mapping of book_id to new priority | 

## Example

```python
from shelfmark_client.models.api_reorder_queue_post_request import ApiReorderQueuePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiReorderQueuePostRequest from a JSON string
api_reorder_queue_post_request_instance = ApiReorderQueuePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiReorderQueuePostRequest.to_json())

# convert the object into a dict
api_reorder_queue_post_request_dict = api_reorder_queue_post_request_instance.to_dict()
# create an instance of ApiReorderQueuePostRequest from a dict
api_reorder_queue_post_request_from_dict = ApiReorderQueuePostRequest.from_dict(api_reorder_queue_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


