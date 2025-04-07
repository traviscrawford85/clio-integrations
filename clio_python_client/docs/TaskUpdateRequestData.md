# TaskUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**TaskUpdateRequestDataAssignee**](TaskUpdateRequestDataAssignee.md) |  | [optional] 
**cascading** | **bool** | Determines if the Task has a due date that is derived from another Task. (Note that if false, no other cascading information will be checked) | [optional] 
**cascading_offset** | **int** | The amount of time that will differentiate the cascaded Task from its parent. | [optional] 
**cascading_offset_polarity** | **str** | Determines whether or not the cascading_offset occurs before or after its parent. | [optional] 
**cascading_offset_type** | **str** | Determines the quantity of the cascading offset (e.g. CalendarDays, CalendarWeeks etc.) | [optional] 
**cascading_source** | **int** | The parent Task that is used to determine the due_at property of the cascaded Task | [optional] 
**description** | **str** | Longer description of the Task. | [optional] 
**due_at** | **datetime** | Date when the Task must be completed by. (Expects an ISO-8601 date). | [optional] 
**matter** | [**TaskCreateRequestDataMatter**](TaskCreateRequestDataMatter.md) |  | [optional] 
**name** | **str** | Name of the Task. | [optional] 
**notify_assignee** | **bool** | Whether or not the Task should notify the assignee on creation. | [optional] 
**notify_completion** | **bool** | Whether or not the Task should notify the assigner on completion. | [optional] 
**permission** | **str** | Permission of the Task. Defaults to &#x60;public&#x60; | [optional] [default to 'public']
**priority** | **str** | Priority of the Task. | [optional] [default to 'Normal']
**status** | **str** | Task status. Users without advanced tasks are allowed to select &#x60;Complete&#x60; or &#x60;Pending&#x60; only. | [optional] [default to 'pending']
**task_type** | [**TaskCreateRequestDataTaskType**](TaskCreateRequestDataTaskType.md) |  | [optional] 
**time_estimated** | **int** | Time the Task should take to complete. | [optional] 

## Example

```python
from openapi_client.models.task_update_request_data import TaskUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskUpdateRequestData from a JSON string
task_update_request_data_instance = TaskUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(TaskUpdateRequestData.to_json())

# convert the object into a dict
task_update_request_data_dict = task_update_request_data_instance.to_dict()
# create an instance of TaskUpdateRequestData from a dict
task_update_request_data_from_dict = TaskUpdateRequestData.from_dict(task_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


