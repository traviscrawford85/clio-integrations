# TaskTemplateListUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the TaskTemplateList. | [optional] 
**name** | **str** | Name of the TaskTemplateList. | [optional] 
**practice_area** | [**TaskTemplateListCreateRequestDataPracticeArea**](TaskTemplateListCreateRequestDataPracticeArea.md) |  | [optional] 

## Example

```python
from openapi_client.models.task_template_list_update_request_data import TaskTemplateListUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateListUpdateRequestData from a JSON string
task_template_list_update_request_data_instance = TaskTemplateListUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateListUpdateRequestData.to_json())

# convert the object into a dict
task_template_list_update_request_data_dict = task_template_list_update_request_data_instance.to_dict()
# create an instance of TaskTemplateListUpdateRequestData from a dict
task_template_list_update_request_data_from_dict = TaskTemplateListUpdateRequestData.from_dict(task_template_list_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


