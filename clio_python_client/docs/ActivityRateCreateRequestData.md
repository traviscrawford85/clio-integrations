# ActivityRateCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**co_counsel_contact_id** | **int** | The unique identifier for a single Contact associated with the ActivityRate. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**contact_id** | **int** | The unique identifier for a single Contact associated with the ActivityRate. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**flat_rate** | **bool** | Whether this is a flat rate | [optional] 
**rate** | **float** | Monetary value of this rate. Either hourly value or flat rate value | [optional] 

## Example

```python
from openapi_client.models.activity_rate_create_request_data import ActivityRateCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityRateCreateRequestData from a JSON string
activity_rate_create_request_data_instance = ActivityRateCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(ActivityRateCreateRequestData.to_json())

# convert the object into a dict
activity_rate_create_request_data_dict = activity_rate_create_request_data_instance.to_dict()
# create an instance of ActivityRateCreateRequestData from a dict
activity_rate_create_request_data_from_dict = ActivityRateCreateRequestData.from_dict(activity_rate_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


