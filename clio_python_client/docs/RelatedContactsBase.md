# RelatedContactsBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *RelatedContacts* | [optional] 
**contact_id** | **int** | The id of the *RelatedContacts* | [optional] 
**name** | **str** | The full name of the *RelatedContacts* | [optional] 
**first_name** | **str** | First name of the Person | [optional] 
**middle_name** | **str** | Middle name of the Person | [optional] 
**last_name** | **str** | Last name of the Person | [optional] 
**type** | **str** | The type of the *RelatedContacts* | [optional] 
**created_at** | **datetime** | The time the *RelatedContacts* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *RelatedContacts* was last updated (as a ISO-8601 timestamp) | [optional] 
**prefix** | **str** | The prefix of the *RelatedContacts* (Mr, Mrs, etc) | [optional] 
**title** | **str** | The designated title of the *RelatedContacts* | [optional] 
**initials** | **str** | The initials of the *RelatedContacts* | [optional] 
**is_matter_client** | **bool** | Whether or not the RelatedContacts is also the client of the matter | [optional] 
**primary_email_address** | **str** | The primary email address of related contact | [optional] 
**primary_phone_number** | **str** | The primary phone number of related contact | [optional] 
**client_connect_user_id** | **int** | The client connect ID of the contacts associated user | [optional] 

## Example

```python
from openapi_client.models.related_contacts_base import RelatedContactsBase

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedContactsBase from a JSON string
related_contacts_base_instance = RelatedContactsBase.from_json(json)
# print the JSON string representation of the object
print(RelatedContactsBase.to_json())

# convert the object into a dict
related_contacts_base_dict = related_contacts_base_instance.to_dict()
# create an instance of RelatedContactsBase from a dict
related_contacts_base_from_dict = RelatedContactsBase.from_dict(related_contacts_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


