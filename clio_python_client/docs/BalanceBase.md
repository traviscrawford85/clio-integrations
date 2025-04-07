# BalanceBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Balance* | [optional] 
**amount** | **float** | The amount for this Balance. | [optional] 
**type** | **str** | The type of Balance this data is for. | [optional] 
**interest_amount** | **float** | The interest amount for this Balance. | [optional] 
**due** | **float** | The amount due for this Balance, factoring in applicable discounts. | [optional] 

## Example

```python
from openapi_client.models.balance_base import BalanceBase

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceBase from a JSON string
balance_base_instance = BalanceBase.from_json(json)
# print the JSON string representation of the object
print(BalanceBase.to_json())

# convert the object into a dict
balance_base_dict = balance_base_instance.to_dict()
# create an instance of BalanceBase from a dict
balance_base_from_dict = BalanceBase.from_dict(balance_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


