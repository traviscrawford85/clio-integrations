# MatterCreateRequestDataCustomFieldSetAssociationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_order** | **int** | The order to display the CustomFieldSet in a Matter. If not specified, it is added as the last CustomFieldSet of the Matter. | [optional] 
**custom_field_set** | [**ContactCreateRequestDataCustomFieldSetAssociationsInnerCustomFieldSet**](ContactCreateRequestDataCustomFieldSetAssociationsInnerCustomFieldSet.md) |  | 

## Example

```python
from openapi_client.models.matter_create_request_data_custom_field_set_associations_inner import MatterCreateRequestDataCustomFieldSetAssociationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataCustomFieldSetAssociationsInner from a JSON string
matter_create_request_data_custom_field_set_associations_inner_instance = MatterCreateRequestDataCustomFieldSetAssociationsInner.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataCustomFieldSetAssociationsInner.to_json())

# convert the object into a dict
matter_create_request_data_custom_field_set_associations_inner_dict = matter_create_request_data_custom_field_set_associations_inner_instance.to_dict()
# create an instance of MatterCreateRequestDataCustomFieldSetAssociationsInner from a dict
matter_create_request_data_custom_field_set_associations_inner_from_dict = MatterCreateRequestDataCustomFieldSetAssociationsInner.from_dict(matter_create_request_data_custom_field_set_associations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


