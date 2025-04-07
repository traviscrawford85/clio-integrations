# CustomActionCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CustomActionCreateRequestData**](CustomActionCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.custom_action_create_request import CustomActionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomActionCreateRequest from a JSON string
custom_action_create_request_instance = CustomActionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomActionCreateRequest.to_json())

# convert the object into a dict
custom_action_create_request_dict = custom_action_create_request_instance.to_dict()
# create an instance of CustomActionCreateRequest from a dict
custom_action_create_request_from_dict = CustomActionCreateRequest.from_dict(custom_action_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


