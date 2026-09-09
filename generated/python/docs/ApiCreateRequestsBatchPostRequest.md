# ApiCreateRequestsBatchPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | **List[Dict[str, object]]** | List of request objects as for POST /api/requests (required) | 

## Example

```python
from shelfmark_client.models.api_create_requests_batch_post_request import ApiCreateRequestsBatchPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCreateRequestsBatchPostRequest from a JSON string
api_create_requests_batch_post_request_instance = ApiCreateRequestsBatchPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiCreateRequestsBatchPostRequest.to_json())

# convert the object into a dict
api_create_requests_batch_post_request_dict = api_create_requests_batch_post_request_instance.to_dict()
# create an instance of ApiCreateRequestsBatchPostRequest from a dict
api_create_requests_batch_post_request_from_dict = ApiCreateRequestsBatchPostRequest.from_dict(api_create_requests_batch_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


