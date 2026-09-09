# ApiSetPriorityPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** | New priority level (lower number &#x3D; higher priority) | 

## Example

```python
from shelfmark_client.models.api_set_priority_put_request import ApiSetPriorityPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSetPriorityPutRequest from a JSON string
api_set_priority_put_request_instance = ApiSetPriorityPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiSetPriorityPutRequest.to_json())

# convert the object into a dict
api_set_priority_put_request_dict = api_set_priority_put_request_instance.to_dict()
# create an instance of ApiSetPriorityPutRequest from a dict
api_set_priority_put_request_from_dict = ApiSetPriorityPutRequest.from_dict(api_set_priority_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


