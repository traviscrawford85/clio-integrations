# BillRecipientContactBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Contact* | [optional] 
**name** | **str** | The full name of the *Contact* | [optional] 
**first_name** | **str** | First name of the Person | [optional] 
**middle_name** | **str** | Middle name of the Person | [optional] 
**last_name** | **str** | Last name of the Person | [optional] 
**type** | **str** | The type of the *Contact* | [optional] 
**primary_email_address** | **str** | The primary email address associated with this *Contact*. | [optional] 

## Example

```python
from openapi_client.models.bill_recipient_contact_base import BillRecipientContactBase

# TODO update the JSON string below
json = "{}"
# create an instance of BillRecipientContactBase from a JSON string
bill_recipient_contact_base_instance = BillRecipientContactBase.from_json(json)
# print the JSON string representation of the object
print(BillRecipientContactBase.to_json())

# convert the object into a dict
bill_recipient_contact_base_dict = bill_recipient_contact_base_instance.to_dict()
# create an instance of BillRecipientContactBase from a dict
bill_recipient_contact_base_from_dict = BillRecipientContactBase.from_dict(bill_recipient_contact_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


