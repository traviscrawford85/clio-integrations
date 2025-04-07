# ActivityRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ActivityRate* | [optional] 
**etag** | **str** | ETag for the *ActivityRate* | [optional] 
**rate** | **float** | Monetary value of this rate. Either hourly value or flat rate value | [optional] 
**flat_rate** | **bool** | Whether this is a flat rate | [optional] 
**created_at** | **datetime** | The time the *ActivityRate* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ActivityRate* was last updated (as a ISO-8601 timestamp) | [optional] 
**contact_id** | **int** | Filter ActivityRate records for the contact. | [optional] 
**co_counsel_contact_id** | **int** | Filter ActivityRate records for the co-counsel. | [optional] 
**user** | [**UserBase**](UserBase.md) |  | [optional] 
**group** | [**GroupBase**](GroupBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.activity_rate import ActivityRate

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityRate from a JSON string
activity_rate_instance = ActivityRate.from_json(json)
# print the JSON string representation of the object
print(ActivityRate.to_json())

# convert the object into a dict
activity_rate_dict = activity_rate_instance.to_dict()
# create an instance of ActivityRate from a dict
activity_rate_from_dict = ActivityRate.from_dict(activity_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


