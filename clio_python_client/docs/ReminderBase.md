# ReminderBase


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

## Example

```python
from openapi_client.models.reminder_base import ReminderBase

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderBase from a JSON string
reminder_base_instance = ReminderBase.from_json(json)
# print the JSON string representation of the object
print(ReminderBase.to_json())

# convert the object into a dict
reminder_base_dict = reminder_base_instance.to_dict()
# create an instance of ReminderBase from a dict
reminder_base_from_dict = ReminderBase.from_dict(reminder_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


