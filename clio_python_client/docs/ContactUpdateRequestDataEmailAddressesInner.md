# ContactUpdateRequestDataEmailAddressesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single EmailAddress associated with the Contact. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**name** | **str** | Name of the EmailAddress. | [optional] [default to 'Other']
**address** | **str** | Email address. | [optional] 
**default_email** | **bool** | Whether or not the Contact should be the default email for the Contact. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated EmailAddress is present, the EmailAddress is deleted from the Contact. | [optional] 

## Example

```python
from openapi_client.models.contact_update_request_data_email_addresses_inner import ContactUpdateRequestDataEmailAddressesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUpdateRequestDataEmailAddressesInner from a JSON string
contact_update_request_data_email_addresses_inner_instance = ContactUpdateRequestDataEmailAddressesInner.from_json(json)
# print the JSON string representation of the object
print(ContactUpdateRequestDataEmailAddressesInner.to_json())

# convert the object into a dict
contact_update_request_data_email_addresses_inner_dict = contact_update_request_data_email_addresses_inner_instance.to_dict()
# create an instance of ContactUpdateRequestDataEmailAddressesInner from a dict
contact_update_request_data_email_addresses_inner_from_dict = ContactUpdateRequestDataEmailAddressesInner.from_dict(contact_update_request_data_email_addresses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


