# TaskCreateRequestDataTaskType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single TaskType associated with the Task. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.task_create_request_data_task_type import TaskCreateRequestDataTaskType

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCreateRequestDataTaskType from a JSON string
task_create_request_data_task_type_instance = TaskCreateRequestDataTaskType.from_json(json)
# print the JSON string representation of the object
print(TaskCreateRequestDataTaskType.to_json())

# convert the object into a dict
task_create_request_data_task_type_dict = task_create_request_data_task_type_instance.to_dict()
# create an instance of TaskCreateRequestDataTaskType from a dict
task_create_request_data_task_type_from_dict = TaskCreateRequestDataTaskType.from_dict(task_create_request_data_task_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


