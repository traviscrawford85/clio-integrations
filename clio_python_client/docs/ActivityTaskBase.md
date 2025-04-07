# ActivityTaskBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Task* | [optional] 
**etag** | **str** | ETag for the *Task* | [optional] 

## Example

```python
from openapi_client.models.activity_task_base import ActivityTaskBase

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityTaskBase from a JSON string
activity_task_base_instance = ActivityTaskBase.from_json(json)
# print the JSON string representation of the object
print(ActivityTaskBase.to_json())

# convert the object into a dict
activity_task_base_dict = activity_task_base_instance.to_dict()
# create an instance of ActivityTaskBase from a dict
activity_task_base_from_dict = ActivityTaskBase.from_dict(activity_task_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


