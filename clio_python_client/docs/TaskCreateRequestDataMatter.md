# TaskCreateRequestDataMatter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Matter associated with the Task. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.task_create_request_data_matter import TaskCreateRequestDataMatter

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCreateRequestDataMatter from a JSON string
task_create_request_data_matter_instance = TaskCreateRequestDataMatter.from_json(json)
# print the JSON string representation of the object
print(TaskCreateRequestDataMatter.to_json())

# convert the object into a dict
task_create_request_data_matter_dict = task_create_request_data_matter_instance.to_dict()
# create an instance of TaskCreateRequestDataMatter from a dict
task_create_request_data_matter_from_dict = TaskCreateRequestDataMatter.from_dict(task_create_request_data_matter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


