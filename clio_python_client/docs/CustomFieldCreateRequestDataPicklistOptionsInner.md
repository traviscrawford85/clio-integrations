# CustomFieldCreateRequestDataPicklistOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single PicklistOption associated with the CustomField. The keyword &#x60;null&#x60; is not valid for this field. Not required for creating new PicklistOptions, but required for updating or deleting existing ones. | [optional] 
**option** | **str** | The option value. | [optional] 
**deleted** | **bool** | Whether or not the PicklistOption should be deleted. | [optional] 

## Example

```python
from openapi_client.models.custom_field_create_request_data_picklist_options_inner import CustomFieldCreateRequestDataPicklistOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldCreateRequestDataPicklistOptionsInner from a JSON string
custom_field_create_request_data_picklist_options_inner_instance = CustomFieldCreateRequestDataPicklistOptionsInner.from_json(json)
# print the JSON string representation of the object
print(CustomFieldCreateRequestDataPicklistOptionsInner.to_json())

# convert the object into a dict
custom_field_create_request_data_picklist_options_inner_dict = custom_field_create_request_data_picklist_options_inner_instance.to_dict()
# create an instance of CustomFieldCreateRequestDataPicklistOptionsInner from a dict
custom_field_create_request_data_picklist_options_inner_from_dict = CustomFieldCreateRequestDataPicklistOptionsInner.from_dict(custom_field_create_request_data_picklist_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


