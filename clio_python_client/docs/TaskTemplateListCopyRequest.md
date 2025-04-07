# TaskTemplateListCopyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskTemplateListCopyRequestData**](TaskTemplateListCopyRequestData.md) |  | 

## Example

```python
from openapi_client.models.task_template_list_copy_request import TaskTemplateListCopyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateListCopyRequest from a JSON string
task_template_list_copy_request_instance = TaskTemplateListCopyRequest.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateListCopyRequest.to_json())

# convert the object into a dict
task_template_list_copy_request_dict = task_template_list_copy_request_instance.to_dict()
# create an instance of TaskTemplateListCopyRequest from a dict
task_template_list_copy_request_from_dict = TaskTemplateListCopyRequest.from_dict(task_template_list_copy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


