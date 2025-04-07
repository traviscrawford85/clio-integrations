# MatterContacts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_created_at** | **datetime** | Timestamp of the time the contact was created | [optional] 
**contact_updated_at** | **datetime** | Timestamp of the time the contact was created | [optional] 
**created_at** | **datetime** | The time the *MatterContacts* was created (as a ISO-8601 timestamp) | [optional] 
**description** | **str** | Description of the matter | [optional] 
**etag** | **str** | ETag for the *MatterContacts* | [optional] 
**first_name** | **str** | First name of the Person | [optional] 
**id** | **int** | Unique identifier for the *MatterContacts* | [optional] 
**initials** | **str** | The initials of the *MatterContacts* | [optional] 
**is_client** | **bool** | Whether or not the MatterContacts is a client | [optional] 
**last_name** | **str** | Last name of the Person | [optional] 
**matter_id** | **int** | ID of the matter | [optional] 
**matter_number** | **str** | Number of the matter | [optional] 
**middle_name** | **str** | Middle name of the Person | [optional] 
**name** | **str** | The full name of the *MatterContacts* | [optional] 
**prefix** | **str** | The prefix of the *MatterContacts* (Mr, Mrs, etc) | [optional] 
**primary_email_address** | **str** | The primary email address associated with this *MatterContacts*. | [optional] 
**primary_phone_number** | **str** | The primary phone number associated with this *MatterContacts*. | [optional] 
**relationship_name** | **str** | The description of the relation between the contact and the matter, or \&quot;Client\&quot; if the user is the client. | [optional] 
**secondary_email_address** | **str** | The secondary email address of the contact | [optional] 
**secondary_phone_number** | **str** | The secondary phone number of the contact | [optional] 
**title** | **str** | The designated title of the *MatterContacts* | [optional] 
**type** | **str** | The type of the *MatterContacts* | [optional] 
**updated_at** | **datetime** | The time the *MatterContacts* was last updated (as a ISO-8601 timestamp) | [optional] 
**client_connect_user_id** | **int** | The client connect ID of the contacts associated user | [optional] 
**avatar** | [**AvatarBase**](AvatarBase.md) |  | [optional] 
**company** | [**ContactBase**](ContactBase.md) |  | [optional] 
**primary_address** | [**AddressBase**](AddressBase.md) |  | [optional] 
**primary_web_site** | [**WebSiteBase**](WebSiteBase.md) |  | [optional] 
**secondary_address** | [**AddressBase**](AddressBase.md) |  | [optional] 
**secondary_web_site** | [**WebSiteBase**](WebSiteBase.md) |  | [optional] 
**addresses** | [**List[AddressBase]**](AddressBase.md) | Address | [optional] 
**custom_field_values** | [**List[CustomFieldValueBase]**](CustomFieldValueBase.md) | CustomFieldValue | [optional] 
**email_addresses** | [**List[EmailAddressBase]**](EmailAddressBase.md) | EmailAddress | [optional] 
**phone_numbers** | [**List[PhoneNumberBase]**](PhoneNumberBase.md) | PhoneNumber | [optional] 
**web_sites** | [**List[WebSiteBase]**](WebSiteBase.md) | WebSite | [optional] 
**relationship** | [**RelationshipBase**](RelationshipBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.matter_contacts import MatterContacts

# TODO update the JSON string below
json = "{}"
# create an instance of MatterContacts from a JSON string
matter_contacts_instance = MatterContacts.from_json(json)
# print the JSON string representation of the object
print(MatterContacts.to_json())

# convert the object into a dict
matter_contacts_dict = matter_contacts_instance.to_dict()
# create an instance of MatterContacts from a dict
matter_contacts_from_dict = MatterContacts.from_dict(matter_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


