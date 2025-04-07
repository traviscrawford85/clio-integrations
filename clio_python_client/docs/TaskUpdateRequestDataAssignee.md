# TaskUpdateRequestDataAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single User or Contact associated with the Task. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**type** | **str** | Model type of the assignee. | [optional] 

## Example

```python
from openapi_client.models.task_update_request_data_assignee import TaskUpdateRequestDataAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of TaskUpdateRequestDataAssignee from a JSON string
task_update_request_data_assignee_instance = TaskUpdateRequestDataAssignee.from_json(json)
# print the JSON string representation of the object
print(TaskUpdateRequestDataAssignee.to_json())

# convert the object into a dict
task_update_request_data_assignee_dict = task_update_request_data_assignee_instance.to_dict()
# create an instance of TaskUpdateRequestDataAssignee from a dict
task_update_request_data_assignee_from_dict = TaskUpdateRequestDataAssignee.from_dict(task_update_request_data_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


