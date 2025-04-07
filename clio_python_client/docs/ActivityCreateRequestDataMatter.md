# ActivityCreateRequestDataMatter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Matter associated with the Activity. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.activity_create_request_data_matter import ActivityCreateRequestDataMatter

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCreateRequestDataMatter from a JSON string
activity_create_request_data_matter_instance = ActivityCreateRequestDataMatter.from_json(json)
# print the JSON string representation of the object
print(ActivityCreateRequestDataMatter.to_json())

# convert the object into a dict
activity_create_request_data_matter_dict = activity_create_request_data_matter_instance.to_dict()
# create an instance of ActivityCreateRequestDataMatter from a dict
activity_create_request_data_matter_from_dict = ActivityCreateRequestDataMatter.from_dict(activity_create_request_data_matter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


