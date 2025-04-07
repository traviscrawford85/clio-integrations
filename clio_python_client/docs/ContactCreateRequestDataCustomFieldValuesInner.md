# ContactCreateRequestDataCustomFieldValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the CustomFieldValue. | 
**custom_field** | [**ContactCreateRequestDataCustomFieldValuesInnerCustomField**](ContactCreateRequestDataCustomFieldValuesInnerCustomField.md) |  | 

## Example

```python
from openapi_client.models.contact_create_request_data_custom_field_values_inner import ContactCreateRequestDataCustomFieldValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateRequestDataCustomFieldValuesInner from a JSON string
contact_create_request_data_custom_field_values_inner_instance = ContactCreateRequestDataCustomFieldValuesInner.from_json(json)
# print the JSON string representation of the object
print(ContactCreateRequestDataCustomFieldValuesInner.to_json())

# convert the object into a dict
contact_create_request_data_custom_field_values_inner_dict = contact_create_request_data_custom_field_values_inner_instance.to_dict()
# create an instance of ContactCreateRequestDataCustomFieldValuesInner from a dict
contact_create_request_data_custom_field_values_inner_from_dict = ContactCreateRequestDataCustomFieldValuesInner.from_dict(contact_create_request_data_custom_field_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


