# TaskTemplateListCopyRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the TaskTemplateList copy. | [optional] 
**name** | **str** | The name of the TaskTemplateList copy. | [optional] 
**practice_area** | [**TaskTemplateListCopyRequestDataPracticeArea**](TaskTemplateListCopyRequestDataPracticeArea.md) |  | [optional] 

## Example

```python
from openapi_client.models.task_template_list_copy_request_data import TaskTemplateListCopyRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateListCopyRequestData from a JSON string
task_template_list_copy_request_data_instance = TaskTemplateListCopyRequestData.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateListCopyRequestData.to_json())

# convert the object into a dict
task_template_list_copy_request_data_dict = task_template_list_copy_request_data_instance.to_dict()
# create an instance of TaskTemplateListCopyRequestData from a dict
task_template_list_copy_request_data_from_dict = TaskTemplateListCopyRequestData.from_dict(task_template_list_copy_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


