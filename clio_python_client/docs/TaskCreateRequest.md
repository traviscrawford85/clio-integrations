# TaskCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskCreateRequestData**](TaskCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.task_create_request import TaskCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCreateRequest from a JSON string
task_create_request_instance = TaskCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TaskCreateRequest.to_json())

# convert the object into a dict
task_create_request_dict = task_create_request_instance.to_dict()
# create an instance of TaskCreateRequest from a dict
task_create_request_from_dict = TaskCreateRequest.from_dict(task_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


