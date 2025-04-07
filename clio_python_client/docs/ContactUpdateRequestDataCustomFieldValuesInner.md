# ContactUpdateRequestDataCustomFieldValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the CustomFieldValue. | [optional] 
**custom_field** | [**ContactUpdateRequestDataCustomFieldValuesInnerCustomField**](ContactUpdateRequestDataCustomFieldValuesInnerCustomField.md) |  | [optional] 
**id** | **int** | The unique identifier for a single CustomFieldValue associated with the Contact. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated CustomFieldValue is present, the CustomFieldValue is deleted from the Contact. | [optional] 

## Example

```python
from openapi_client.models.contact_update_request_data_custom_field_values_inner import ContactUpdateRequestDataCustomFieldValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUpdateRequestDataCustomFieldValuesInner from a JSON string
contact_update_request_data_custom_field_values_inner_instance = ContactUpdateRequestDataCustomFieldValuesInner.from_json(json)
# print the JSON string representation of the object
print(ContactUpdateRequestDataCustomFieldValuesInner.to_json())

# convert the object into a dict
contact_update_request_data_custom_field_values_inner_dict = contact_update_request_data_custom_field_values_inner_instance.to_dict()
# create an instance of ContactUpdateRequestDataCustomFieldValuesInner from a dict
contact_update_request_data_custom_field_values_inner_from_dict = ContactUpdateRequestDataCustomFieldValuesInner.from_dict(contact_update_request_data_custom_field_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


