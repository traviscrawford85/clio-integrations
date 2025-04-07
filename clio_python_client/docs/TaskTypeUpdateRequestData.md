# TaskTypeUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_at** | **date** | Date the TaskType was disabled. (Expects an ISO-8601 timestamp). | [optional] 
**name** | **str** | Name of the TaskType. | [optional] 

## Example

```python
from openapi_client.models.task_type_update_request_data import TaskTypeUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTypeUpdateRequestData from a JSON string
task_type_update_request_data_instance = TaskTypeUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(TaskTypeUpdateRequestData.to_json())

# convert the object into a dict
task_type_update_request_data_dict = task_type_update_request_data_instance.to_dict()
# create an instance of TaskTypeUpdateRequestData from a dict
task_type_update_request_data_from_dict = TaskTypeUpdateRequestData.from_dict(task_type_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


