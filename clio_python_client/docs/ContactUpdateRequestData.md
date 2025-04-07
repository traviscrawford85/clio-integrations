# ContactUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[ContactUpdateRequestDataAddressesInner]**](ContactUpdateRequestDataAddressesInner.md) |  | [optional] 
**avatar** | [**ContactCreateRequestDataAvatar**](ContactCreateRequestDataAvatar.md) |  | [optional] 
**clio_connect_email** | **str** | Notifications will be sent to this email when a resource is shared. | [optional] 
**co_counsel_rate** | [**ContactCreateRequestDataCoCounselRate**](ContactCreateRequestDataCoCounselRate.md) |  | [optional] 
**company** | [**ContactCreateRequestDataCompany**](ContactCreateRequestDataCompany.md) |  | [optional] 
**currency** | **object** | The Currency the contact is associated with. | [optional] 
**custom_field_set_associations** | [**List[ContactUpdateRequestDataCustomFieldSetAssociationsInner]**](ContactUpdateRequestDataCustomFieldSetAssociationsInner.md) |  | [optional] 
**custom_field_values** | [**List[ContactUpdateRequestDataCustomFieldValuesInner]**](ContactUpdateRequestDataCustomFieldValuesInner.md) |  | [optional] 
**date_of_birth** | **date** | Date of birth of the Contact. | [optional] 
**email_addresses** | [**List[ContactUpdateRequestDataEmailAddressesInner]**](ContactUpdateRequestDataEmailAddressesInner.md) |  | [optional] 
**first_name** | **str** | First name of the Contact. | [optional] 
**instant_messengers** | [**List[ContactUpdateRequestDataInstantMessengersInner]**](ContactUpdateRequestDataInstantMessengersInner.md) |  | [optional] 
**last_name** | **str** | Last name of the Contact. | [optional] 
**ledes_client_id** | **str** | LEDES client id of the Contact. | [optional] 
**middle_name** | **str** | Middle name of the Contact. | [optional] 
**name** | **str** | Full name of the Contact. For requirements, see [Contact Name](https://docs.developers.clio.com/api-reference/#section/Contact-Name). | [optional] 
**phone_numbers** | [**List[ContactUpdateRequestDataPhoneNumbersInner]**](ContactUpdateRequestDataPhoneNumbersInner.md) |  | [optional] 
**prefix** | **str** | Personal title of the Contact. | [optional] 
**sales_tax_number** | **str** | A contact&#39;s sales tax number will appear on invoices generated for the Contact. | [optional] 
**title** | **str** | Professional title of the Contact. | [optional] 
**type** | **str** | Type of the Contact. | [optional] 
**web_sites** | [**List[ContactUpdateRequestDataWebSitesInner]**](ContactUpdateRequestDataWebSitesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.contact_update_request_data import ContactUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUpdateRequestData from a JSON string
contact_update_request_data_instance = ContactUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(ContactUpdateRequestData.to_json())

# convert the object into a dict
contact_update_request_data_dict = contact_update_request_data_instance.to_dict()
# create an instance of ContactUpdateRequestData from a dict
contact_update_request_data_from_dict = ContactUpdateRequestData.from_dict(contact_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


