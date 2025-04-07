# Task


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
**time_entries** | [**List[ActivityBase]**](ActivityBase.md) | Activity | [optional] 
**task_type** | [**TaskTypeBase**](TaskTypeBase.md) |  | [optional] 
**assigner** | [**UserBase**](UserBase.md) |  | [optional] 
**matter** | [**MatterBase**](MatterBase.md) |  | [optional] 
**assignee** | [**Participant**](Participant.md) |  | [optional] 
**reminders** | [**List[ReminderBase]**](ReminderBase.md) | Reminder | [optional] 

## Example

```python
from openapi_client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


