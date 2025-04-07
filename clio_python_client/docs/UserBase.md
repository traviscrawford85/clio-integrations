# UserBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_owner** | **bool** | Whether the *User* is the owner of the account | [optional] 
**clio_connect** | **bool** | Whether the *User* is a Clio Connect user | [optional] 
**court_rules_default_attendee** | **bool** | Whether the *User* is a default attendee for court rules events | [optional] 
**created_at** | **datetime** | The time the *User* was created (as a ISO-8601 timestamp) | [optional] 
**default_calendar_id** | **int** | Default calendar id for *User*. | [optional] 
**email** | **str** | The email of the *User* | [optional] 
**enabled** | **bool** | Whether the *User* is allowed to log in | [optional] 
**etag** | **str** | ETag for the *User* | [optional] 
**first_name** | **str** | The first name of the *User* | [optional] 
**id** | **int** | Unique identifier for the *User* | [optional] 
**initials** | **str** | The initials of the *User* | [optional] 
**last_name** | **str** | The last name of the *User* | [optional] 
**name** | **str** | The full name of the *User* | [optional] 
**phone_number** | **str** | The primary phone number for the *User*. | [optional] 
**rate** | **float** | Default user activity rate for *User*. | [optional] 
**roles** | **List[str]** | An array of roles assigned to this *User* | [optional] 
**subscription_type** | **str** | The subscription type of the *User* | [optional] 
**time_zone** | **str** | The selected time zone of the *User* | [optional] 
**updated_at** | **datetime** | The time the *User* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.user_base import UserBase

# TODO update the JSON string below
json = "{}"
# create an instance of UserBase from a JSON string
user_base_instance = UserBase.from_json(json)
# print the JSON string representation of the object
print(UserBase.to_json())

# convert the object into a dict
user_base_dict = user_base_instance.to_dict()
# create an instance of UserBase from a dict
user_base_from_dict = UserBase.from_dict(user_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


