# LineItemUpdateRequestDataDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** | Discount rate for the LineItem. | [optional] 
**type** | **bool** | Discount type. This should be set to one of: &#39;percentage&#39; or &#39;money&#39;. | [optional] 

## Example

```python
from openapi_client.models.line_item_update_request_data_discount import LineItemUpdateRequestDataDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemUpdateRequestDataDiscount from a JSON string
line_item_update_request_data_discount_instance = LineItemUpdateRequestDataDiscount.from_json(json)
# print the JSON string representation of the object
print(LineItemUpdateRequestDataDiscount.to_json())

# convert the object into a dict
line_item_update_request_data_discount_dict = line_item_update_request_data_discount_instance.to_dict()
# create an instance of LineItemUpdateRequestDataDiscount from a dict
line_item_update_request_data_discount_from_dict = LineItemUpdateRequestDataDiscount.from_dict(line_item_update_request_data_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


