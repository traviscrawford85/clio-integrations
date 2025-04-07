# ContactCreateRequestDataCustomFieldSetAssociationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_order** | **int** | The order to display the CustomFieldSet in a Contact. If not specified, it is added as the last CustomFieldSet of the Contact. | [optional] 
**custom_field_set** | [**ContactCreateRequestDataCustomFieldSetAssociationsInnerCustomFieldSet**](ContactCreateRequestDataCustomFieldSetAssociationsInnerCustomFieldSet.md) |  | 

## Example

```python
from openapi_client.models.contact_create_request_data_custom_field_set_associations_inner import ContactCreateRequestDataCustomFieldSetAssociationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateRequestDataCustomFieldSetAssociationsInner from a JSON string
contact_create_request_data_custom_field_set_associations_inner_instance = ContactCreateRequestDataCustomFieldSetAssociationsInner.from_json(json)
# print the JSON string representation of the object
print(ContactCreateRequestDataCustomFieldSetAssociationsInner.to_json())

# convert the object into a dict
contact_create_request_data_custom_field_set_associations_inner_dict = contact_create_request_data_custom_field_set_associations_inner_instance.to_dict()
# create an instance of ContactCreateRequestDataCustomFieldSetAssociationsInner from a dict
contact_create_request_data_custom_field_set_associations_inner_from_dict = ContactCreateRequestDataCustomFieldSetAssociationsInner.from_dict(contact_create_request_data_custom_field_set_associations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


