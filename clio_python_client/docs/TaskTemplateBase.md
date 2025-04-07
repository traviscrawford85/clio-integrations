# TaskTemplateBase


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

## Example

```python
from openapi_client.models.task_template_base import TaskTemplateBase

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateBase from a JSON string
task_template_base_instance = TaskTemplateBase.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateBase.to_json())

# convert the object into a dict
task_template_base_dict = task_template_base_instance.to_dict()
# create an instance of TaskTemplateBase from a dict
task_template_base_from_dict = TaskTemplateBase.from_dict(task_template_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


