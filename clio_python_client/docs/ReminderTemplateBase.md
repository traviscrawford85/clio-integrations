# ReminderTemplateBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ReminderTemplate* | [optional] 
**etag** | **str** | ETag for the *ReminderTemplate* | [optional] 
**duration** | **int** | The time in minutes to remind user before the subject. | [optional] 
**notification_type** | **str** | The type of method to be notified by | [optional] 
**created_at** | **datetime** | The time the *ReminderTemplate* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ReminderTemplate* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.reminder_template_base import ReminderTemplateBase

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderTemplateBase from a JSON string
reminder_template_base_instance = ReminderTemplateBase.from_json(json)
# print the JSON string representation of the object
print(ReminderTemplateBase.to_json())

# convert the object into a dict
reminder_template_base_dict = reminder_template_base_instance.to_dict()
# create an instance of ReminderTemplateBase from a dict
reminder_template_base_from_dict = ReminderTemplateBase.from_dict(reminder_template_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


