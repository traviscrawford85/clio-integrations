# ActivityCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActivityCreateRequestData**](ActivityCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.activity_create_request import ActivityCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCreateRequest from a JSON string
activity_create_request_instance = ActivityCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ActivityCreateRequest.to_json())

# convert the object into a dict
activity_create_request_dict = activity_create_request_instance.to_dict()
# create an instance of ActivityCreateRequest from a dict
activity_create_request_from_dict = ActivityCreateRequest.from_dict(activity_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


