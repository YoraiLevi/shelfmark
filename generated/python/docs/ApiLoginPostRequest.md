# ApiLoginPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username | 
**password** | **str** | Password | 
**remember_me** | **bool** | Whether to extend session duration | 

## Example

```python
from shelfmark_client.models.api_login_post_request import ApiLoginPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLoginPostRequest from a JSON string
api_login_post_request_instance = ApiLoginPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiLoginPostRequest.to_json())

# convert the object into a dict
api_login_post_request_dict = api_login_post_request_instance.to_dict()
# create an instance of ApiLoginPostRequest from a dict
api_login_post_request_from_dict = ApiLoginPostRequest.from_dict(api_login_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


