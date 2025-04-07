# TaskTemplateListCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the TaskTemplateList. | 
**name** | **str** | Name of the TaskTemplateList. | 
**practice_area** | [**TaskTemplateListCreateRequestDataPracticeArea**](TaskTemplateListCreateRequestDataPracticeArea.md) |  | [optional] 

## Example

```python
from openapi_client.models.task_template_list_create_request_data import TaskTemplateListCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateListCreateRequestData from a JSON string
task_template_list_create_request_data_instance = TaskTemplateListCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateListCreateRequestData.to_json())

# convert the object into a dict
task_template_list_create_request_data_dict = task_template_list_create_request_data_instance.to_dict()
# create an instance of TaskTemplateListCreateRequestData from a dict
task_template_list_create_request_data_from_dict = TaskTemplateListCreateRequestData.from_dict(task_template_list_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


