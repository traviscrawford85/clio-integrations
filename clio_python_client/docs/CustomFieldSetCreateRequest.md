# CustomFieldSetCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CustomFieldSetCreateRequestData**](CustomFieldSetCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.custom_field_set_create_request import CustomFieldSetCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldSetCreateRequest from a JSON string
custom_field_set_create_request_instance = CustomFieldSetCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomFieldSetCreateRequest.to_json())

# convert the object into a dict
custom_field_set_create_request_dict = custom_field_set_create_request_instance.to_dict()
# create an instance of CustomFieldSetCreateRequest from a dict
custom_field_set_create_request_from_dict = CustomFieldSetCreateRequest.from_dict(custom_field_set_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


