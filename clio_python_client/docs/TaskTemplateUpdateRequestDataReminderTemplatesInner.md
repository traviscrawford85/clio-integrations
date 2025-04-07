# TaskTemplateUpdateRequestDataReminderTemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_value** | **int** | Time measured in &#x60;duration_unit&#x60; to remind user before the subject. | [optional] 
**duration_unit** | **str** | Unit to measure the duration value in. | [optional] 
**notification_type** | **str** | Notification method. | [optional] 
**id** | **int** | The unique identifier for a single ReminderTemplate associated with the TaskTemplate. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated ReminderTemplate is present, the ReminderTemplate is deleted from the TaskTemplate. | [optional] 

## Example

```python
from openapi_client.models.task_template_update_request_data_reminder_templates_inner import TaskTemplateUpdateRequestDataReminderTemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateUpdateRequestDataReminderTemplatesInner from a JSON string
task_template_update_request_data_reminder_templates_inner_instance = TaskTemplateUpdateRequestDataReminderTemplatesInner.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateUpdateRequestDataReminderTemplatesInner.to_json())

# convert the object into a dict
task_template_update_request_data_reminder_templates_inner_dict = task_template_update_request_data_reminder_templates_inner_instance.to_dict()
# create an instance of TaskTemplateUpdateRequestDataReminderTemplatesInner from a dict
task_template_update_request_data_reminder_templates_inner_from_dict = TaskTemplateUpdateRequestDataReminderTemplatesInner.from_dict(task_template_update_request_data_reminder_templates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


