# TaskTemplateCreateRequestDataTaskTemplateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single TaskTemplateList associated with the TaskTemplate. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.task_template_create_request_data_task_template_list import TaskTemplateCreateRequestDataTaskTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateCreateRequestDataTaskTemplateList from a JSON string
task_template_create_request_data_task_template_list_instance = TaskTemplateCreateRequestDataTaskTemplateList.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateCreateRequestDataTaskTemplateList.to_json())

# convert the object into a dict
task_template_create_request_data_task_template_list_dict = task_template_create_request_data_task_template_list_instance.to_dict()
# create an instance of TaskTemplateCreateRequestDataTaskTemplateList from a dict
task_template_create_request_data_task_template_list_from_dict = TaskTemplateCreateRequestDataTaskTemplateList.from_dict(task_template_create_request_data_task_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


