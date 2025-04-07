# ContactUpdateRequestDataPhoneNumbersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the PhoneNumber. | [optional] [default to 'Other']
**number** | **str** | Phone number. | [optional] 
**default_number** | **bool** | Whether or not the PhoneNumber should be the default number for the Contact. | [optional] 
**id** | **int** | The unique identifier for a single PhoneNumber associated with the Contact. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated PhoneNumber is present, the PhoneNumber is deleted from the Contact. | [optional] 

## Example

```python
from openapi_client.models.contact_update_request_data_phone_numbers_inner import ContactUpdateRequestDataPhoneNumbersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUpdateRequestDataPhoneNumbersInner from a JSON string
contact_update_request_data_phone_numbers_inner_instance = ContactUpdateRequestDataPhoneNumbersInner.from_json(json)
# print the JSON string representation of the object
print(ContactUpdateRequestDataPhoneNumbersInner.to_json())

# convert the object into a dict
contact_update_request_data_phone_numbers_inner_dict = contact_update_request_data_phone_numbers_inner_instance.to_dict()
# create an instance of ContactUpdateRequestDataPhoneNumbersInner from a dict
contact_update_request_data_phone_numbers_inner_from_dict = ContactUpdateRequestDataPhoneNumbersInner.from_dict(contact_update_request_data_phone_numbers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


