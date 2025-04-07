# TaskCreateRequestDataAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single User or Contact associated with the Task. The keyword &#x60;null&#x60; is not valid for this field. | 
**type** | **str** | Model type of the assignee. | 

## Example

```python
from openapi_client.models.task_create_request_data_assignee import TaskCreateRequestDataAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCreateRequestDataAssignee from a JSON string
task_create_request_data_assignee_instance = TaskCreateRequestDataAssignee.from_json(json)
# print the JSON string representation of the object
print(TaskCreateRequestDataAssignee.to_json())

# convert the object into a dict
task_create_request_data_assignee_dict = task_create_request_data_assignee_instance.to_dict()
# create an instance of TaskCreateRequestDataAssignee from a dict
task_create_request_data_assignee_from_dict = TaskCreateRequestDataAssignee.from_dict(task_create_request_data_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


