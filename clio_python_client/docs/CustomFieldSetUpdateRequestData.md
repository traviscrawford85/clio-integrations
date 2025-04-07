# CustomFieldSetUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayed** | **bool** | Whether or not the CustomFieldSet should be displayed by default. | [optional] 
**name** | **str** | CustomFieldSet name. | [optional] 
**parent_type** | **str** | Type of object the CustomFieldSet is for. | [optional] 

## Example

```python
from openapi_client.models.custom_field_set_update_request_data import CustomFieldSetUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldSetUpdateRequestData from a JSON string
custom_field_set_update_request_data_instance = CustomFieldSetUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(CustomFieldSetUpdateRequestData.to_json())

# convert the object into a dict
custom_field_set_update_request_data_dict = custom_field_set_update_request_data_instance.to_dict()
# create an instance of CustomFieldSetUpdateRequestData from a dict
custom_field_set_update_request_data_from_dict = CustomFieldSetUpdateRequestData.from_dict(custom_field_set_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


