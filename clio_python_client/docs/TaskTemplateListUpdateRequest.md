# TaskTemplateListUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskTemplateListUpdateRequestData**](TaskTemplateListUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.task_template_list_update_request import TaskTemplateListUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateListUpdateRequest from a JSON string
task_template_list_update_request_instance = TaskTemplateListUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateListUpdateRequest.to_json())

# convert the object into a dict
task_template_list_update_request_dict = task_template_list_update_request_instance.to_dict()
# create an instance of TaskTemplateListUpdateRequest from a dict
task_template_list_update_request_from_dict = TaskTemplateListUpdateRequest.from_dict(task_template_list_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


