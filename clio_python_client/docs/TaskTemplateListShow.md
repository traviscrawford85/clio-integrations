# TaskTemplateListShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskTemplateList**](TaskTemplateList.md) |  | 

## Example

```python
from openapi_client.models.task_template_list_show import TaskTemplateListShow

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateListShow from a JSON string
task_template_list_show_instance = TaskTemplateListShow.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateListShow.to_json())

# convert the object into a dict
task_template_list_show_dict = task_template_list_show_instance.to_dict()
# create an instance of TaskTemplateListShow from a dict
task_template_list_show_from_dict = TaskTemplateListShow.from_dict(task_template_list_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


