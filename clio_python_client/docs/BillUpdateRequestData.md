# BillUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill_theme** | [**BillUpdateRequestDataBillTheme**](BillUpdateRequestDataBillTheme.md) |  | [optional] 
**currency_id** | **int** | ID of the currency applied to the Bill. | [optional] 
**discount** | [**BillUpdateRequestDataDiscount**](BillUpdateRequestDataDiscount.md) |  | [optional] 
**due_at** | **date** | Date the Bill is due. If &#x60;use_grace_period&#x60; is true, this field is ignored. | [optional] 
**interest** | [**BillUpdateRequestDataInterest**](BillUpdateRequestDataInterest.md) |  | [optional] 
**issued_at** | **date** | Date the Bill was issued. | [optional] 
**memo** | **str** | Memo for the Bill. | [optional] 
**number** | **str** | Bill&#39;s number. | [optional] 
**purchase_order** | **str** | Purchase order information for the Bill. | [optional] 
**secondary_tax_rate** | **float** | Secondary tax rate as percentage for the Bill. | [optional] 
**state** | **str** | Bill&#39;s state. | [optional] 
**subject** | **str** | Subject details for the Bill. | [optional] 
**tax_rate** | **float** | Tax rate as percentage for the Bill | [optional] 
**use_grace_period** | **bool** | When true, sets the bill&#39;s due date based on the client&#39;s grace period. This setting overrides the &#x60;due_at&#x60; parameter. | [optional] 

## Example

```python
from openapi_client.models.bill_update_request_data import BillUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BillUpdateRequestData from a JSON string
bill_update_request_data_instance = BillUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(BillUpdateRequestData.to_json())

# convert the object into a dict
bill_update_request_data_dict = bill_update_request_data_instance.to_dict()
# create an instance of BillUpdateRequestData from a dict
bill_update_request_data_from_dict = BillUpdateRequestData.from_dict(bill_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


