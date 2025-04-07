# MatterUpdateRequestDataSplitInvoicePayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **int** | Contact id for the matter payer. | [optional] 
**id** | **int** | The id for the payer. | [optional] 
**send_to_bill_recipients** | **bool** | Boolean indication to send a split invoice to all bill recipients. | [optional] 
**split_portion** | **float** | The split portion for the payer. | [optional] 
**destroy** | **bool** | If this flag is set to &#x60;true&#x60;, the split invoice payer will be deleted from the Matter. | [optional] 

## Example

```python
from openapi_client.models.matter_update_request_data_split_invoice_payers_inner import MatterUpdateRequestDataSplitInvoicePayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatterUpdateRequestDataSplitInvoicePayersInner from a JSON string
matter_update_request_data_split_invoice_payers_inner_instance = MatterUpdateRequestDataSplitInvoicePayersInner.from_json(json)
# print the JSON string representation of the object
print(MatterUpdateRequestDataSplitInvoicePayersInner.to_json())

# convert the object into a dict
matter_update_request_data_split_invoice_payers_inner_dict = matter_update_request_data_split_invoice_payers_inner_instance.to_dict()
# create an instance of MatterUpdateRequestDataSplitInvoicePayersInner from a dict
matter_update_request_data_split_invoice_payers_inner_from_dict = MatterUpdateRequestDataSplitInvoicePayersInner.from_dict(matter_update_request_data_split_invoice_payers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


