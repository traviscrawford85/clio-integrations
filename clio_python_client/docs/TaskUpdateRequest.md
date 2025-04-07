# TaskUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskUpdateRequestData**](TaskUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.task_update_request import TaskUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskUpdateRequest from a JSON string
task_update_request_instance = TaskUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TaskUpdateRequest.to_json())

# convert the object into a dict
task_update_request_dict = task_update_request_instance.to_dict()
# create an instance of TaskUpdateRequest from a dict
task_update_request_from_dict = TaskUpdateRequest.from_dict(task_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


