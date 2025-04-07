# CascadingTaskTemplateBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *TaskTemplate* | [optional] 
**name** | **str** | The name of the *TaskTemplate* | [optional] 

## Example

```python
from openapi_client.models.cascading_task_template_base import CascadingTaskTemplateBase

# TODO update the JSON string below
json = "{}"
# create an instance of CascadingTaskTemplateBase from a JSON string
cascading_task_template_base_instance = CascadingTaskTemplateBase.from_json(json)
# print the JSON string representation of the object
print(CascadingTaskTemplateBase.to_json())

# convert the object into a dict
cascading_task_template_base_dict = cascading_task_template_base_instance.to_dict()
# create an instance of CascadingTaskTemplateBase from a dict
cascading_task_template_base_from_dict = CascadingTaskTemplateBase.from_dict(cascading_task_template_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


