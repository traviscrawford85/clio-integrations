# TaskBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Task* | [optional] 
**etag** | **str** | ETag for the *Task* | [optional] 
**name** | **str** | The name of the *Task* | [optional] 
**status** | **str** | Status of the *Task*. (Note that users without advanced tasks can only have either complete or pending) | [optional] 
**description** | **str** | A detailed description of the *Task* | [optional] 
**priority** | **str** | The priority of the *Task* | [optional] 
**due_at** | **date** | The date the *Task* is due (as a ISO-8601 date) | [optional] 
**permission** | **str** | The permission of the *Task* | [optional] 
**completed_at** | **datetime** | The time the *Task* was completed (as a ISO-8601 timestamp) | [optional] 
**notify_completion** | **bool** | Whether to notify the assigner of the task&#39;s completion | [optional] 
**statute_of_limitations** | **bool** | Whether the task is a statute of limitations | [optional] 
**time_estimated** | **int** | Time the *Task* should take to complete | [optional] 
**created_at** | **datetime** | The time the *Task* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Task* was last updated (as a ISO-8601 timestamp) | [optional] 
**time_entries_count** | **int** | The number of time entries associated with this task | [optional] 

## Example

```python
from openapi_client.models.task_base import TaskBase

# TODO update the JSON string below
json = "{}"
# create an instance of TaskBase from a JSON string
task_base_instance = TaskBase.from_json(json)
# print the JSON string representation of the object
print(TaskBase.to_json())

# convert the object into a dict
task_base_dict = task_base_instance.to_dict()
# create an instance of TaskBase from a dict
task_base_from_dict = TaskBase.from_dict(task_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


