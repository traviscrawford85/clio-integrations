# ActivityUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActivityUpdateRequestData**](ActivityUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.activity_update_request import ActivityUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityUpdateRequest from a JSON string
activity_update_request_instance = ActivityUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ActivityUpdateRequest.to_json())

# convert the object into a dict
activity_update_request_dict = activity_update_request_instance.to_dict()
# create an instance of ActivityUpdateRequest from a dict
activity_update_request_from_dict = ActivityUpdateRequest.from_dict(activity_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


