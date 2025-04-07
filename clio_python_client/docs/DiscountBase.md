# DiscountBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** | The rate of the *Discount%* | [optional] 
**type** | **str** | The type of *Discount* being applied in your *Discount* rate. | [optional] 
**note** | **str** | A note for your *Discount* | [optional] 
**early_payment_rate** | **int** | The % discount that will be applied if your *Discount* is paid within the early payment period. | [optional] 
**early_payment_period** | **int** | The number of days for your *Discount* period. If your bill is paid within this time, apply your *Discount* rate to the bill. | [optional] 

## Example

```python
from openapi_client.models.discount_base import DiscountBase

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountBase from a JSON string
discount_base_instance = DiscountBase.from_json(json)
# print the JSON string representation of the object
print(DiscountBase.to_json())

# convert the object into a dict
discount_base_dict = discount_base_instance.to_dict()
# create an instance of DiscountBase from a dict
discount_base_from_dict = DiscountBase.from_dict(discount_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


