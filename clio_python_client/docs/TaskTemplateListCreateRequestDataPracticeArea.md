# TaskTemplateListCreateRequestDataPracticeArea


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single PracticeArea associated with the TaskTemplateList. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.task_template_list_create_request_data_practice_area import TaskTemplateListCreateRequestDataPracticeArea

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateListCreateRequestDataPracticeArea from a JSON string
task_template_list_create_request_data_practice_area_instance = TaskTemplateListCreateRequestDataPracticeArea.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateListCreateRequestDataPracticeArea.to_json())

# convert the object into a dict
task_template_list_create_request_data_practice_area_dict = task_template_list_create_request_data_practice_area_instance.to_dict()
# create an instance of TaskTemplateListCreateRequestDataPracticeArea from a dict
task_template_list_create_request_data_practice_area_from_dict = TaskTemplateListCreateRequestDataPracticeArea.from_dict(task_template_list_create_request_data_practice_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


