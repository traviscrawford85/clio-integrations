# ActivityDescriptionCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActivityDescriptionCreateRequestData**](ActivityDescriptionCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.activity_description_create_request import ActivityDescriptionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityDescriptionCreateRequest from a JSON string
activity_description_create_request_instance = ActivityDescriptionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ActivityDescriptionCreateRequest.to_json())

# convert the object into a dict
activity_description_create_request_dict = activity_description_create_request_instance.to_dict()
# create an instance of ActivityDescriptionCreateRequest from a dict
activity_description_create_request_from_dict = ActivityDescriptionCreateRequest.from_dict(activity_description_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


