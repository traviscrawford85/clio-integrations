# InterestChargeBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *InterestCharge* | [optional] 
**etag** | **str** | ETag for the *InterestCharge* | [optional] 
**var_date** | **date** | The *InterestCharge* date (as a ISO-8601 date) | [optional] 
**description** | **str** | The description for the *InterestCharge* | [optional] 
**total** | **float** | The total amount for the *InterestCharge* | [optional] 
**created_at** | **datetime** | The time the *InterestCharge* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *InterestCharge* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.interest_charge_base import InterestChargeBase

# TODO update the JSON string below
json = "{}"
# create an instance of InterestChargeBase from a JSON string
interest_charge_base_instance = InterestChargeBase.from_json(json)
# print the JSON string representation of the object
print(InterestChargeBase.to_json())

# convert the object into a dict
interest_charge_base_dict = interest_charge_base_instance.to_dict()
# create an instance of InterestChargeBase from a dict
interest_charge_base_from_dict = InterestChargeBase.from_dict(interest_charge_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


