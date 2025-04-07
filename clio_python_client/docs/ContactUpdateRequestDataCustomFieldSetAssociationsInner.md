# ContactUpdateRequestDataCustomFieldSetAssociationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single CustomFieldSetAssociation associated with the Contact. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**display_order** | **int** | The order to display the CustomFieldSet in a Contact. If not specified, it is added as the last CustomFieldSet of the Contact. | [optional] 
**custom_field_set** | [**ContactUpdateRequestDataCustomFieldSetAssociationsInnerCustomFieldSet**](ContactUpdateRequestDataCustomFieldSetAssociationsInnerCustomFieldSet.md) |  | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated CustomFieldSetAssociation is present, the CustomFieldSetAssociation is deleted from the Contact. | [optional] 

## Example

```python
from openapi_client.models.contact_update_request_data_custom_field_set_associations_inner import ContactUpdateRequestDataCustomFieldSetAssociationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUpdateRequestDataCustomFieldSetAssociationsInner from a JSON string
contact_update_request_data_custom_field_set_associations_inner_instance = ContactUpdateRequestDataCustomFieldSetAssociationsInner.from_json(json)
# print the JSON string representation of the object
print(ContactUpdateRequestDataCustomFieldSetAssociationsInner.to_json())

# convert the object into a dict
contact_update_request_data_custom_field_set_associations_inner_dict = contact_update_request_data_custom_field_set_associations_inner_instance.to_dict()
# create an instance of ContactUpdateRequestDataCustomFieldSetAssociationsInner from a dict
contact_update_request_data_custom_field_set_associations_inner_from_dict = ContactUpdateRequestDataCustomFieldSetAssociationsInner.from_dict(contact_update_request_data_custom_field_set_associations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


