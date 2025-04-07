# ContactBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Contact* | [optional] 
**etag** | **str** | ETag for the *Contact* | [optional] 
**name** | **str** | The full name of the *Contact* | [optional] 
**first_name** | **str** | First name of the Person | [optional] 
**middle_name** | **str** | Middle name of the Person | [optional] 
**last_name** | **str** | Last name of the Person | [optional] 
**date_of_birth** | **date** | Date of birth | [optional] 
**type** | **str** | The type of the *Contact* | [optional] 
**created_at** | **datetime** | The time the *Contact* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Contact* was last updated (as a ISO-8601 timestamp) | [optional] 
**prefix** | **str** | The prefix of the *Contact* (Mr, Mrs, etc) | [optional] 
**title** | **str** | The designated title of the *Contact* | [optional] 
**initials** | **str** | The initials of the *Contact* | [optional] 
**clio_connect_email** | **str** | Clio Connect email if the *Contact* is a ClioConnect User | [optional] 
**locked_clio_connect_email** | **bool** | A boolean indicating if the ability to modify this *Contacts Clio connect email is locked. | [optional] 
**client_connect_user_id** | **int** | The ID for the Clio Connect user associated with this *Contact* | [optional] 
**primary_email_address** | **str** | The primary email address associated with this *Contact*. | [optional] 
**secondary_email_address** | **str** | The secondary email address associated with this *Contact*. | [optional] 
**primary_phone_number** | **str** | The primary phone number associated with this *Contact*. | [optional] 
**secondary_phone_number** | **str** | The secondary phone number of the *Contact*. | [optional] 
**ledes_client_id** | **str** | LEDES client id of the Contact | [optional] 
**has_clio_for_clients_permission** | **bool** | True if at least one resource has been shared with the contact using Clio for Clients. | [optional] 
**is_client** | **bool** | Whether or not the Contact is a client | [optional] 
**is_clio_for_client_user** | **bool** | Whether or not this contact has client_login and client_user (can be created due to addition to client portal or client_share_permissions) | [optional] 
**is_co_counsel** | **bool** | Whether or not the Contact has matters shared as co-counsel | [optional] 
**is_bill_recipient** | **bool** | Whether the Contact is a bill recipient on at least one matter. | [optional] 
**sales_tax_number** | **str** | The sales tax number of the *Contact* | [optional] 
**currency** | **object** | Currency of the *Contact* | [optional] 

## Example

```python
from openapi_client.models.contact_base import ContactBase

# TODO update the JSON string below
json = "{}"
# create an instance of ContactBase from a JSON string
contact_base_instance = ContactBase.from_json(json)
# print the JSON string representation of the object
print(ContactBase.to_json())

# convert the object into a dict
contact_base_dict = contact_base_instance.to_dict()
# create an instance of ContactBase from a dict
contact_base_from_dict = ContactBase.from_dict(contact_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


