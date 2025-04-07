# TaskTypeUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskTypeUpdateRequestData**](TaskTypeUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.task_type_update_request import TaskTypeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTypeUpdateRequest from a JSON string
task_type_update_request_instance = TaskTypeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TaskTypeUpdateRequest.to_json())

# convert the object into a dict
task_type_update_request_dict = task_type_update_request_instance.to_dict()
# create an instance of TaskTypeUpdateRequest from a dict
task_type_update_request_from_dict = TaskTypeUpdateRequest.from_dict(task_type_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


