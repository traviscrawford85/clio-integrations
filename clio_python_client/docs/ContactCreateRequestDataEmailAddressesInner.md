# ContactCreateRequestDataEmailAddressesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the EmailAddress. | [optional] [default to 'Other']
**address** | **str** | Email address. | [optional] 
**default_email** | **bool** | Whether or not the Contact should be the default email for the Contact. | [optional] 

## Example

```python
from openapi_client.models.contact_create_request_data_email_addresses_inner import ContactCreateRequestDataEmailAddressesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateRequestDataEmailAddressesInner from a JSON string
contact_create_request_data_email_addresses_inner_instance = ContactCreateRequestDataEmailAddressesInner.from_json(json)
# print the JSON string representation of the object
print(ContactCreateRequestDataEmailAddressesInner.to_json())

# convert the object into a dict
contact_create_request_data_email_addresses_inner_dict = contact_create_request_data_email_addresses_inner_instance.to_dict()
# create an instance of ContactCreateRequestDataEmailAddressesInner from a dict
contact_create_request_data_email_addresses_inner_from_dict = ContactCreateRequestDataEmailAddressesInner.from_dict(contact_create_request_data_email_addresses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


