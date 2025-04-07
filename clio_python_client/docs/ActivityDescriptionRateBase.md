# ActivityDescriptionRateBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Monetary value of this rate. Either hourly value or flat rate value | [optional] 
**non_billable_amount** | **float** | Monetary value of this rate for non billable activities. Either hourly value or flat rate value | [optional] 
**type** | **str** | What kind of rate it is. | [optional] 
**hierarchy** | **str** | What rate hierarchy the rate belongs to. | [optional] 

## Example

```python
from openapi_client.models.activity_description_rate_base import ActivityDescriptionRateBase

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityDescriptionRateBase from a JSON string
activity_description_rate_base_instance = ActivityDescriptionRateBase.from_json(json)
# print the JSON string representation of the object
print(ActivityDescriptionRateBase.to_json())

# convert the object into a dict
activity_description_rate_base_dict = activity_description_rate_base_instance.to_dict()
# create an instance of ActivityDescriptionRateBase from a dict
activity_description_rate_base_from_dict = ActivityDescriptionRateBase.from_dict(activity_description_rate_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


