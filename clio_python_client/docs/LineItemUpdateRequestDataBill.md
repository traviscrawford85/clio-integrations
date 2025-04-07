# LineItemUpdateRequestDataBill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Bill associated with the LineItem. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.line_item_update_request_data_bill import LineItemUpdateRequestDataBill

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemUpdateRequestDataBill from a JSON string
line_item_update_request_data_bill_instance = LineItemUpdateRequestDataBill.from_json(json)
# print the JSON string representation of the object
print(LineItemUpdateRequestDataBill.to_json())

# convert the object into a dict
line_item_update_request_data_bill_dict = line_item_update_request_data_bill_instance.to_dict()
# create an instance of LineItemUpdateRequestDataBill from a dict
line_item_update_request_data_bill_from_dict = LineItemUpdateRequestDataBill.from_dict(line_item_update_request_data_bill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


