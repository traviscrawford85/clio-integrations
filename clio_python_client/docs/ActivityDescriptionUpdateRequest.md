# ActivityDescriptionUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActivityDescriptionUpdateRequestData**](ActivityDescriptionUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.activity_description_update_request import ActivityDescriptionUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityDescriptionUpdateRequest from a JSON string
activity_description_update_request_instance = ActivityDescriptionUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ActivityDescriptionUpdateRequest.to_json())

# convert the object into a dict
activity_description_update_request_dict = activity_description_update_request_instance.to_dict()
# create an instance of ActivityDescriptionUpdateRequest from a dict
activity_description_update_request_from_dict = ActivityDescriptionUpdateRequest.from_dict(activity_description_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


