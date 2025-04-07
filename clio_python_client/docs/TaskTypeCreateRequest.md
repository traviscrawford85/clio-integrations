# TaskTypeCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskTypeCreateRequestData**](TaskTypeCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.task_type_create_request import TaskTypeCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTypeCreateRequest from a JSON string
task_type_create_request_instance = TaskTypeCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TaskTypeCreateRequest.to_json())

# convert the object into a dict
task_type_create_request_dict = task_type_create_request_instance.to_dict()
# create an instance of TaskTypeCreateRequest from a dict
task_type_create_request_from_dict = TaskTypeCreateRequest.from_dict(task_type_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


