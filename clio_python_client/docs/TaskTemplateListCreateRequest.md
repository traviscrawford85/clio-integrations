# TaskTemplateListCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskTemplateListCreateRequestData**](TaskTemplateListCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.task_template_list_create_request import TaskTemplateListCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateListCreateRequest from a JSON string
task_template_list_create_request_instance = TaskTemplateListCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateListCreateRequest.to_json())

# convert the object into a dict
task_template_list_create_request_dict = task_template_list_create_request_instance.to_dict()
# create an instance of TaskTemplateListCreateRequest from a dict
task_template_list_create_request_from_dict = TaskTemplateListCreateRequest.from_dict(task_template_list_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


