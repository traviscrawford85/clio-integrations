# CustomFieldCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CustomFieldCreateRequestData**](CustomFieldCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.custom_field_create_request import CustomFieldCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldCreateRequest from a JSON string
custom_field_create_request_instance = CustomFieldCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomFieldCreateRequest.to_json())

# convert the object into a dict
custom_field_create_request_dict = custom_field_create_request_instance.to_dict()
# create an instance of CustomFieldCreateRequest from a dict
custom_field_create_request_from_dict = CustomFieldCreateRequest.from_dict(custom_field_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


