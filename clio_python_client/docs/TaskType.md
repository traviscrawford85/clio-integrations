# TaskType


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
from openapi_client.models.task_type import TaskType

# TODO update the JSON string below
json = "{}"
# create an instance of TaskType from a JSON string
task_type_instance = TaskType.from_json(json)
# print the JSON string representation of the object
print(TaskType.to_json())

# convert the object into a dict
task_type_dict = task_type_instance.to_dict()
# create an instance of TaskType from a dict
task_type_from_dict = TaskType.from_dict(task_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


