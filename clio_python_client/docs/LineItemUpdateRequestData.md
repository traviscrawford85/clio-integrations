# LineItemUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**LineItemUpdateRequestDataActivity**](LineItemUpdateRequestDataActivity.md) |  | [optional] 
**bill** | [**LineItemUpdateRequestDataBill**](LineItemUpdateRequestDataBill.md) |  | [optional] 
**var_date** | **date** | The LineItem date. | [optional] 
**description** | **str** | Description of the LineItem. | [optional] 
**discount** | [**LineItemUpdateRequestDataDiscount**](LineItemUpdateRequestDataDiscount.md) |  | [optional] 
**group_ordering** | **int** | The LineItem group ordering. | [optional] 
**kind** | **str** | The specific type of activity which is associated with the LineItem. | [optional] 
**matter** | [**LineItemUpdateRequestDataMatter**](LineItemUpdateRequestDataMatter.md) |  | [optional] 
**note** | **str** | The note attached to the LineItem. | [optional] 
**price** | **float** | The price of the LineItem. | [optional] 
**quantity** | **float** | Quantity of the LineItem. | [optional] 
**secondary_taxable** | **bool** | Whether the LineItem is secondary taxable. | [optional] 
**taxable** | **bool** | Whether the LineItem taxable. | [optional] 
**update_original_record** | **bool** | Whether the associated activity will be updated. | [optional] 

## Example

```python
from openapi_client.models.line_item_update_request_data import LineItemUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemUpdateRequestData from a JSON string
line_item_update_request_data_instance = LineItemUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(LineItemUpdateRequestData.to_json())

# convert the object into a dict
line_item_update_request_data_dict = line_item_update_request_data_instance.to_dict()
# create an instance of LineItemUpdateRequestData from a dict
line_item_update_request_data_from_dict = LineItemUpdateRequestData.from_dict(line_item_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


