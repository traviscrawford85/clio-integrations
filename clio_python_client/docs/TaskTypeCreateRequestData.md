# TaskTypeCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_at** | **date** | Date the TaskType was disabled. (Expects an ISO-8601 timestamp). | [optional] 
**name** | **str** | Name of the TaskType. | 

## Example

```python
from openapi_client.models.task_type_create_request_data import TaskTypeCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTypeCreateRequestData from a JSON string
task_type_create_request_data_instance = TaskTypeCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(TaskTypeCreateRequestData.to_json())

# convert the object into a dict
task_type_create_request_data_dict = task_type_create_request_data_instance.to_dict()
# create an instance of TaskTypeCreateRequestData from a dict
task_type_create_request_data_from_dict = TaskTypeCreateRequestData.from_dict(task_type_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


