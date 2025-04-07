# ActivityRateCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActivityRateCreateRequestData**](ActivityRateCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.activity_rate_create_request import ActivityRateCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityRateCreateRequest from a JSON string
activity_rate_create_request_instance = ActivityRateCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ActivityRateCreateRequest.to_json())

# convert the object into a dict
activity_rate_create_request_dict = activity_rate_create_request_instance.to_dict()
# create an instance of ActivityRateCreateRequest from a dict
activity_rate_create_request_from_dict = ActivityRateCreateRequest.from_dict(activity_rate_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


