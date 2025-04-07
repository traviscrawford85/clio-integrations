# TaskTemplateCreateRequestDataReminderTemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_value** | **int** | Time measured in &#x60;duration_unit&#x60; to remind user before the subject. | 
**duration_unit** | **str** | Unit to measure the duration value in. | 
**notification_type** | **str** | Notification method. | 

## Example

```python
from openapi_client.models.task_template_create_request_data_reminder_templates_inner import TaskTemplateCreateRequestDataReminderTemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateCreateRequestDataReminderTemplatesInner from a JSON string
task_template_create_request_data_reminder_templates_inner_instance = TaskTemplateCreateRequestDataReminderTemplatesInner.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateCreateRequestDataReminderTemplatesInner.to_json())

# convert the object into a dict
task_template_create_request_data_reminder_templates_inner_dict = task_template_create_request_data_reminder_templates_inner_instance.to_dict()
# create an instance of TaskTemplateCreateRequestDataReminderTemplatesInner from a dict
task_template_create_request_data_reminder_templates_inner_from_dict = TaskTemplateCreateRequestDataReminderTemplatesInner.from_dict(task_template_create_request_data_reminder_templates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


