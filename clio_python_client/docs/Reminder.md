# Reminder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Reminder* | [optional] 
**etag** | **str** | ETag for the *Reminder* | [optional] 
**duration** | **int** | Time in minutes to remind user before the subject | [optional] 
**next_delivery_at** | **datetime** | The time the *Reminder* will be delivered (as a ISO-8601 timestamp) | [optional] 
**state** | **str** | The current state of the *Reminder* | [optional] 
**created_at** | **datetime** | The time the *Reminder* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Reminder* was last updated (as a ISO-8601 timestamp) | [optional] 
**notification_method** | [**NotificationMethodBase**](NotificationMethodBase.md) |  | [optional] 
**subject** | [**PolymorphicObjectBase**](PolymorphicObjectBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.reminder import Reminder

# TODO update the JSON string below
json = "{}"
# create an instance of Reminder from a JSON string
reminder_instance = Reminder.from_json(json)
# print the JSON string representation of the object
print(Reminder.to_json())

# convert the object into a dict
reminder_dict = reminder_instance.to_dict()
# create an instance of Reminder from a dict
reminder_from_dict = Reminder.from_dict(reminder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


