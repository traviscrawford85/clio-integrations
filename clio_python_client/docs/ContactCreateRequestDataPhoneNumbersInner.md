# ContactCreateRequestDataPhoneNumbersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the PhoneNumber. | [optional] [default to 'Other']
**number** | **str** | Phone number. | [optional] 
**default_number** | **bool** | Whether or not the PhoneNumber should be the default number for the Contact. | [optional] 

## Example

```python
from openapi_client.models.contact_create_request_data_phone_numbers_inner import ContactCreateRequestDataPhoneNumbersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreateRequestDataPhoneNumbersInner from a JSON string
contact_create_request_data_phone_numbers_inner_instance = ContactCreateRequestDataPhoneNumbersInner.from_json(json)
# print the JSON string representation of the object
print(ContactCreateRequestDataPhoneNumbersInner.to_json())

# convert the object into a dict
contact_create_request_data_phone_numbers_inner_dict = contact_create_request_data_phone_numbers_inner_instance.to_dict()
# create an instance of ContactCreateRequestDataPhoneNumbersInner from a dict
contact_create_request_data_phone_numbers_inner_from_dict = ContactCreateRequestDataPhoneNumbersInner.from_dict(contact_create_request_data_phone_numbers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


