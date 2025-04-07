# ActivityCreateRequestDataTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Task associated with the Activity. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.activity_create_request_data_task import ActivityCreateRequestDataTask

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCreateRequestDataTask from a JSON string
activity_create_request_data_task_instance = ActivityCreateRequestDataTask.from_json(json)
# print the JSON string representation of the object
print(ActivityCreateRequestDataTask.to_json())

# convert the object into a dict
activity_create_request_data_task_dict = activity_create_request_data_task_instance.to_dict()
# create an instance of ActivityCreateRequestDataTask from a dict
activity_create_request_data_task_from_dict = ActivityCreateRequestDataTask.from_dict(activity_create_request_data_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


