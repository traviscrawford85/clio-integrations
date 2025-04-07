# JobTitleBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *JobTitle* | [optional] 
**etag** | **str** | ETag for the *JobTitle* | [optional] 
**name** | **str** | Name of the job title | [optional] 
**initials** | **str** | Initials of the job title | [optional] 

## Example

```python
from openapi_client.models.job_title_base import JobTitleBase

# TODO update the JSON string below
json = "{}"
# create an instance of JobTitleBase from a JSON string
job_title_base_instance = JobTitleBase.from_json(json)
# print the JSON string representation of the object
print(JobTitleBase.to_json())

# convert the object into a dict
job_title_base_dict = job_title_base_instance.to_dict()
# create an instance of JobTitleBase from a dict
job_title_base_from_dict = JobTitleBase.from_dict(job_title_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


