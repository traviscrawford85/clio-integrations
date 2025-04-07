# AttendeeBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Attendee* | [optional] 
**etag** | **str** | ETag for the *Attendee* | [optional] 
**type** | **str** | The class name of the *Attendee* | [optional] 
**name** | **str** | The name of the *Attendee* | [optional] 
**enabled** | **bool** | If the Attendee is a user, represents whether the user is enabled or disabled. Returns null if attendee is a Contact. | [optional] 
**email** | **str** | If the Attendee is a User, this is the User&#39;s email. If the Attendee is a contact, this is the Contact&#39;s primary email address. | [optional] 
**created_at** | **datetime** | The time the *Attendee* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Attendee* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.attendee_base import AttendeeBase

# TODO update the JSON string below
json = "{}"
# create an instance of AttendeeBase from a JSON string
attendee_base_instance = AttendeeBase.from_json(json)
# print the JSON string representation of the object
print(AttendeeBase.to_json())

# convert the object into a dict
attendee_base_dict = attendee_base_instance.to_dict()
# create an instance of AttendeeBase from a dict
attendee_base_from_dict = AttendeeBase.from_dict(attendee_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


