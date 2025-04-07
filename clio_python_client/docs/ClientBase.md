# ClientBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Client* | [optional] 
**name** | **str** | The full name of the *Client* | [optional] 
**first_name** | **str** | First name of the Person | [optional] 
**middle_name** | **str** | Middle name of the Person | [optional] 
**last_name** | **str** | Last name of the Person | [optional] 
**type** | **str** | The type of the *Client* | [optional] 
**created_at** | **datetime** | The time the *Client* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Client* was last updated (as a ISO-8601 timestamp) | [optional] 
**prefix** | **str** | The prefix of the *Client* (Mr, Mrs, etc) | [optional] 
**title** | **str** | The designated title of the *Client* | [optional] 
**initials** | **str** | The initials of the *Client* | [optional] 
**is_matter_client** | **bool** | Whether or not the Client is also the client of the matter | [optional] 
**primary_email_address** | **str** | The primary email address of client | [optional] 
**primary_phone_number** | **str** | The primary phone number of client | [optional] 
**client_connect_user_id** | **int** | The client connect ID of the contacts associated user | [optional] 
**date_of_birth** | **date** | Date of Birth | [optional] 

## Example

```python
from openapi_client.models.client_base import ClientBase

# TODO update the JSON string below
json = "{}"
# create an instance of ClientBase from a JSON string
client_base_instance = ClientBase.from_json(json)
# print the JSON string representation of the object
print(ClientBase.to_json())

# convert the object into a dict
client_base_dict = client_base_instance.to_dict()
# create an instance of ClientBase from a dict
client_base_from_dict = ClientBase.from_dict(client_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


