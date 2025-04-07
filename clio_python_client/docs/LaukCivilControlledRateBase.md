# LaukCivilControlledRateBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *LaukCivilControlledRate* | [optional] 
**activity** | **str** | Activity of the *LaukCivilControlledRate* | [optional] 
**activity_type** | **str** | Activity type | [optional] 
**category_of_law** | **str** | Category of law | [optional] 
**created_at** | **datetime** | The time the *LaukCivilControlledRate* was created (as a ISO-8601 timestamp) | [optional] 
**etag** | **str** | ETag for the *LaukCivilControlledRate* | [optional] 
**exceptional** | **float** | Fee applied for high activity count | [optional] 
**fee** | **float** | Fee amount | [optional] 
**fee_scheme** | **str** | Fee scheme | [optional] 
**key** | **str** | Unique key | [optional] 
**rate_type** | **str** | Rate type | [optional] 
**region** | **str** | Region | [optional] 
**updated_at** | **datetime** | The time the *LaukCivilControlledRate* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.lauk_civil_controlled_rate_base import LaukCivilControlledRateBase

# TODO update the JSON string below
json = "{}"
# create an instance of LaukCivilControlledRateBase from a JSON string
lauk_civil_controlled_rate_base_instance = LaukCivilControlledRateBase.from_json(json)
# print the JSON string representation of the object
print(LaukCivilControlledRateBase.to_json())

# convert the object into a dict
lauk_civil_controlled_rate_base_dict = lauk_civil_controlled_rate_base_instance.to_dict()
# create an instance of LaukCivilControlledRateBase from a dict
lauk_civil_controlled_rate_base_from_dict = LaukCivilControlledRateBase.from_dict(lauk_civil_controlled_rate_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


