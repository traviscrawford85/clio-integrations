# TaskTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TaskType]**](TaskType.md) | TaskType List Response | 

## Example

```python
from openapi_client.models.task_type_list import TaskTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTypeList from a JSON string
task_type_list_instance = TaskTypeList.from_json(json)
# print the JSON string representation of the object
print(TaskTypeList.to_json())

# convert the object into a dict
task_type_list_dict = task_type_list_instance.to_dict()
# create an instance of TaskTypeList from a dict
task_type_list_from_dict = TaskTypeList.from_dict(task_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


