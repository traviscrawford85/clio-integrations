# TaskTemplateUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskTemplateUpdateRequestData**](TaskTemplateUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.task_template_update_request import TaskTemplateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateUpdateRequest from a JSON string
task_template_update_request_instance = TaskTemplateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateUpdateRequest.to_json())

# convert the object into a dict
task_template_update_request_dict = task_template_update_request_instance.to_dict()
# create an instance of TaskTemplateUpdateRequest from a dict
task_template_update_request_from_dict = TaskTemplateUpdateRequest.from_dict(task_template_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


