# CustomFieldSetUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CustomFieldSetUpdateRequestData**](CustomFieldSetUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.custom_field_set_update_request import CustomFieldSetUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldSetUpdateRequest from a JSON string
custom_field_set_update_request_instance = CustomFieldSetUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomFieldSetUpdateRequest.to_json())

# convert the object into a dict
custom_field_set_update_request_dict = custom_field_set_update_request_instance.to_dict()
# create an instance of CustomFieldSetUpdateRequest from a dict
custom_field_set_update_request_from_dict = CustomFieldSetUpdateRequest.from_dict(custom_field_set_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


