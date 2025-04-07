# TaskTemplateListInstaceBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *TaskTemplateListInstace* | [optional] 
**etag** | **str** | ETag for the *TaskTemplateListInstace* | [optional] 
**created_at** | **datetime** | The time the *TaskTemplateListInstace* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *TaskTemplateListInstace* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.task_template_list_instace_base import TaskTemplateListInstaceBase

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateListInstaceBase from a JSON string
task_template_list_instace_base_instance = TaskTemplateListInstaceBase.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateListInstaceBase.to_json())

# convert the object into a dict
task_template_list_instace_base_dict = task_template_list_instace_base_instance.to_dict()
# create an instance of TaskTemplateListInstaceBase from a dict
task_template_list_instace_base_from_dict = TaskTemplateListInstaceBase.from_dict(task_template_list_instace_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


