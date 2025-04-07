# TaskTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *TaskTemplate* | [optional] 
**etag** | **str** | ETag for the *TaskTemplate* | [optional] 
**name** | **str** | The name of the *TaskTemplate* | [optional] 
**description** | **str** | A detailed description of the *TaskTemplate* | [optional] 
**priority** | **str** | *TaskTemplate* priority | [optional] 
**private** | **bool** | Whether the *TaskTemplate* is private. | [optional] 
**created_at** | **datetime** | The time the *TaskTemplate* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *TaskTemplate* was last updated (as a ISO-8601 timestamp) | [optional] 
**cascading_source** | [**CascadingTaskTemplateBase**](CascadingTaskTemplateBase.md) |  | [optional] 
**assignee** | [**UserBase**](UserBase.md) |  | [optional] 
**task_template_list** | [**TaskTemplateListBase**](TaskTemplateListBase.md) |  | [optional] 
**task_type** | [**TaskTypeBase**](TaskTypeBase.md) |  | [optional] 
**template_creator** | [**UserBase**](UserBase.md) |  | [optional] 
**reminder_templates** | [**List[ReminderTemplateBase]**](ReminderTemplateBase.md) | ReminderTemplate | [optional] 

## Example

```python
from openapi_client.models.task_template import TaskTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplate from a JSON string
task_template_instance = TaskTemplate.from_json(json)
# print the JSON string representation of the object
print(TaskTemplate.to_json())

# convert the object into a dict
task_template_dict = task_template_instance.to_dict()
# create an instance of TaskTemplate from a dict
task_template_from_dict = TaskTemplate.from_dict(task_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


