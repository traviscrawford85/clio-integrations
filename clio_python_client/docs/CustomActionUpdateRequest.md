# CustomActionUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CustomActionUpdateRequestData**](CustomActionUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.custom_action_update_request import CustomActionUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomActionUpdateRequest from a JSON string
custom_action_update_request_instance = CustomActionUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomActionUpdateRequest.to_json())

# convert the object into a dict
custom_action_update_request_dict = custom_action_update_request_instance.to_dict()
# create an instance of CustomActionUpdateRequest from a dict
custom_action_update_request_from_dict = CustomActionUpdateRequest.from_dict(custom_action_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


