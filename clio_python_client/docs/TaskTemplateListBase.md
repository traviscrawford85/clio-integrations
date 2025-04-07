# TaskTemplateListBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The time the *TaskTemplateList* was created (as a ISO-8601 timestamp) | [optional] 
**description** | **str** | A detailed description of the *TaskTemplateList* | [optional] 
**id** | **int** | Unique identifier for the *TaskTemplateList* | [optional] 
**etag** | **str** | ETag for the *TaskTemplateList* | [optional] 
**name** | **str** | The name of the *TaskTemplateList* | [optional] 
**templates_count** | **int** | How many task templates exist as an association to the *TaskTemplateList* | [optional] 
**updated_at** | **datetime** | The time the *TaskTemplateList* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.task_template_list_base import TaskTemplateListBase

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateListBase from a JSON string
task_template_list_base_instance = TaskTemplateListBase.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateListBase.to_json())

# convert the object into a dict
task_template_list_base_dict = task_template_list_base_instance.to_dict()
# create an instance of TaskTemplateListBase from a dict
task_template_list_base_from_dict = TaskTemplateListBase.from_dict(task_template_list_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


