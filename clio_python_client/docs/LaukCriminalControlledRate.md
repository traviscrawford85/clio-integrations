# LaukCriminalControlledRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *LaukCriminalControlledRate* | [optional] 
**activity** | **str** | Activity of the *LaukCriminalControlledRate* | [optional] 
**activity_type** | **str** | Activity type | [optional] 
**category_of_law** | **str** | Category of law | [optional] 
**counsel** | **str** | Associated counsel | [optional] 
**court** | **str** | Court associated | [optional] 
**created_at** | **datetime** | The time the *LaukCriminalControlledRate* was created (as a ISO-8601 timestamp) | [optional] 
**etag** | **str** | ETag for the *LaukCriminalControlledRate* | [optional] 
**exceptional** | **float** | Fee applied for high activity count | [optional] 
**fee** | **float** | Fee amount | [optional] 
**fee_scheme** | **str** | Fee scheme | [optional] 
**post_nov_24_exceptional** | **float** | Post-Nov 24 exceptional fee | [optional] 
**post_nov_24_fee** | **float** | Post-Nov 24 fee amount | [optional] 
**post_sept_22_exceptional** | **float** | Post-Sept 22 exceptional fee | [optional] 
**post_sept_22_fee** | **float** | Post-Sept 22 fee amount | [optional] 
**key** | **str** | Unique key | [optional] 
**rate_type** | **str** | Rate type | [optional] 
**region** | **str** | Region | [optional] 
**solicitor_type** | **str** | Solicitor type | [optional] 
**updated_at** | **datetime** | The time the *LaukCriminalControlledRate* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.lauk_criminal_controlled_rate import LaukCriminalControlledRate

# TODO update the JSON string below
json = "{}"
# create an instance of LaukCriminalControlledRate from a JSON string
lauk_criminal_controlled_rate_instance = LaukCriminalControlledRate.from_json(json)
# print the JSON string representation of the object
print(LaukCriminalControlledRate.to_json())

# convert the object into a dict
lauk_criminal_controlled_rate_dict = lauk_criminal_controlled_rate_instance.to_dict()
# create an instance of LaukCriminalControlledRate from a dict
lauk_criminal_controlled_rate_from_dict = LaukCriminalControlledRate.from_dict(lauk_criminal_controlled_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


