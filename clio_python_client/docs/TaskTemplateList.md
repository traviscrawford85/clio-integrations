# TaskTemplateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TaskTemplate]**](TaskTemplate.md) | TaskTemplate List Response | 

## Example

```python
from openapi_client.models.task_template_list import TaskTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateList from a JSON string
task_template_list_instance = TaskTemplateList.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateList.to_json())

# convert the object into a dict
task_template_list_dict = task_template_list_instance.to_dict()
# create an instance of TaskTemplateList from a dict
task_template_list_from_dict = TaskTemplateList.from_dict(task_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


