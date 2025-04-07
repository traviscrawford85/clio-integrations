# CustomFieldUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CustomFieldUpdateRequestData**](CustomFieldUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.custom_field_update_request import CustomFieldUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldUpdateRequest from a JSON string
custom_field_update_request_instance = CustomFieldUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomFieldUpdateRequest.to_json())

# convert the object into a dict
custom_field_update_request_dict = custom_field_update_request_instance.to_dict()
# create an instance of CustomFieldUpdateRequest from a dict
custom_field_update_request_from_dict = CustomFieldUpdateRequest.from_dict(custom_field_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


