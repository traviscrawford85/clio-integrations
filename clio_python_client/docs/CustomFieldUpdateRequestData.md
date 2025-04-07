# CustomFieldUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_order** | **int** | The display position of the CustomField. | [optional] 
**displayed** | **bool** | Whether or not the CustomField should be displayed by default. | [optional] [default to True]
**name** | **str** | CustomField name. | [optional] 
**picklist_options** | [**List[CustomFieldCreateRequestDataPicklistOptionsInner]**](CustomFieldCreateRequestDataPicklistOptionsInner.md) |  | [optional] 
**required** | **bool** | Whether or not the CustomField should require a value. | [optional] [default to False]

## Example

```python
from openapi_client.models.custom_field_update_request_data import CustomFieldUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldUpdateRequestData from a JSON string
custom_field_update_request_data_instance = CustomFieldUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(CustomFieldUpdateRequestData.to_json())

# convert the object into a dict
custom_field_update_request_data_dict = custom_field_update_request_data_instance.to_dict()
# create an instance of CustomFieldUpdateRequestData from a dict
custom_field_update_request_data_from_dict = CustomFieldUpdateRequestData.from_dict(custom_field_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


