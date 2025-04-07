# CustomFieldSetCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayed** | **bool** | Whether or not the CustomFieldSet should be displayed by default. | [optional] 
**name** | **str** | CustomFieldSet name. | 
**parent_type** | **str** | Type of object the CustomFieldSet is for. | [optional] 

## Example

```python
from openapi_client.models.custom_field_set_create_request_data import CustomFieldSetCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldSetCreateRequestData from a JSON string
custom_field_set_create_request_data_instance = CustomFieldSetCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(CustomFieldSetCreateRequestData.to_json())

# convert the object into a dict
custom_field_set_create_request_data_dict = custom_field_set_create_request_data_instance.to_dict()
# create an instance of CustomFieldSetCreateRequestData from a dict
custom_field_set_create_request_data_from_dict = CustomFieldSetCreateRequestData.from_dict(custom_field_set_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


