# MatterUpdateRequestDataCustomFieldValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the CustomFieldValue. | [optional] 
**custom_field** | [**ContactUpdateRequestDataCustomFieldValuesInnerCustomField**](ContactUpdateRequestDataCustomFieldValuesInnerCustomField.md) |  | [optional] 
**id** | **int** | The unique identifier for a single CustomFieldValue associated with the Matter. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated CustomFieldValue is present, the CustomFieldValue is deleted from the Matter. | [optional] 

## Example

```python
from openapi_client.models.matter_update_request_data_custom_field_values_inner import MatterUpdateRequestDataCustomFieldValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatterUpdateRequestDataCustomFieldValuesInner from a JSON string
matter_update_request_data_custom_field_values_inner_instance = MatterUpdateRequestDataCustomFieldValuesInner.from_json(json)
# print the JSON string representation of the object
print(MatterUpdateRequestDataCustomFieldValuesInner.to_json())

# convert the object into a dict
matter_update_request_data_custom_field_values_inner_dict = matter_update_request_data_custom_field_values_inner_instance.to_dict()
# create an instance of MatterUpdateRequestDataCustomFieldValuesInner from a dict
matter_update_request_data_custom_field_values_inner_from_dict = MatterUpdateRequestDataCustomFieldValuesInner.from_dict(matter_update_request_data_custom_field_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


