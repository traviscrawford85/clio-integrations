# MatterUpdateRequestDataCustomFieldSetAssociationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single CustomFieldSetAssociation associated with the Matter. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**display_order** | **int** | The order to display the CustomFieldSet in a Matter. If not specified, it is added as the last CustomFieldSet of the Matter. | [optional] 
**custom_field_set** | [**ContactUpdateRequestDataCustomFieldSetAssociationsInnerCustomFieldSet**](ContactUpdateRequestDataCustomFieldSetAssociationsInnerCustomFieldSet.md) |  | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated CustomFieldSetAssociation is present, the CustomFieldSetAssociation is deleted from the Matter. | [optional] 

## Example

```python
from openapi_client.models.matter_update_request_data_custom_field_set_associations_inner import MatterUpdateRequestDataCustomFieldSetAssociationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatterUpdateRequestDataCustomFieldSetAssociationsInner from a JSON string
matter_update_request_data_custom_field_set_associations_inner_instance = MatterUpdateRequestDataCustomFieldSetAssociationsInner.from_json(json)
# print the JSON string representation of the object
print(MatterUpdateRequestDataCustomFieldSetAssociationsInner.to_json())

# convert the object into a dict
matter_update_request_data_custom_field_set_associations_inner_dict = matter_update_request_data_custom_field_set_associations_inner_instance.to_dict()
# create an instance of MatterUpdateRequestDataCustomFieldSetAssociationsInner from a dict
matter_update_request_data_custom_field_set_associations_inner_from_dict = MatterUpdateRequestDataCustomFieldSetAssociationsInner.from_dict(matter_update_request_data_custom_field_set_associations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


