# TaskTemplateListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TaskTemplateList]**](TaskTemplateList.md) | TaskTemplateList List Response | 

## Example

```python
from openapi_client.models.task_template_list_list import TaskTemplateListList

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateListList from a JSON string
task_template_list_list_instance = TaskTemplateListList.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateListList.to_json())

# convert the object into a dict
task_template_list_list_dict = task_template_list_list_instance.to_dict()
# create an instance of TaskTemplateListList from a dict
task_template_list_list_from_dict = TaskTemplateListList.from_dict(task_template_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


