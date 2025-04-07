# TaskTypeBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *TaskType* | [optional] 
**etag** | **str** | ETag for the *TaskType* | [optional] 
**name** | **str** | The name of the *TaskType* | [optional] 
**deleted_at** | **datetime** | The time the *TaskType* was deleted (as a ISO-8601 timestamp) | [optional] 
**created_at** | **datetime** | The time the *TaskType* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *TaskType* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.task_type_base import TaskTypeBase

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTypeBase from a JSON string
task_type_base_instance = TaskTypeBase.from_json(json)
# print the JSON string representation of the object
print(TaskTypeBase.to_json())

# convert the object into a dict
task_type_base_dict = task_type_base_instance.to_dict()
# create an instance of TaskTypeBase from a dict
task_type_base_from_dict = TaskTypeBase.from_dict(task_type_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


