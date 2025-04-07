# LineItemTotalsBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Sum of quantity for included line items. | [optional] 
**price** | **float** | Sum of price for included line items. | [optional] 
**discount_percent** | **float** | Sum of discount as percentage for included line items. | [optional] 
**total** | **float** | Sum of total for included line items. | [optional] 
**sub_total** | **float** | Sum of total before discount and tax is applied. | [optional] 

## Example

```python
from openapi_client.models.line_item_totals_base import LineItemTotalsBase

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemTotalsBase from a JSON string
line_item_totals_base_instance = LineItemTotalsBase.from_json(json)
# print the JSON string representation of the object
print(LineItemTotalsBase.to_json())

# convert the object into a dict
line_item_totals_base_dict = line_item_totals_base_instance.to_dict()
# create an instance of LineItemTotalsBase from a dict
line_item_totals_base_from_dict = LineItemTotalsBase.from_dict(line_item_totals_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


