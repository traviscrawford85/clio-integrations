# MatterCreateRequestDataSplitInvoicePayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **int** | Contact id for the matter payer. | 
**send_to_bill_recipients** | **bool** | Boolean indication to send a split invoice to all bill recipients. | [optional] 
**split_portion** | **float** | The split portion for the payer. | 

## Example

```python
from openapi_client.models.matter_create_request_data_split_invoice_payers_inner import MatterCreateRequestDataSplitInvoicePayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataSplitInvoicePayersInner from a JSON string
matter_create_request_data_split_invoice_payers_inner_instance = MatterCreateRequestDataSplitInvoicePayersInner.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataSplitInvoicePayersInner.to_json())

# convert the object into a dict
matter_create_request_data_split_invoice_payers_inner_dict = matter_create_request_data_split_invoice_payers_inner_instance.to_dict()
# create an instance of MatterCreateRequestDataSplitInvoicePayersInner from a dict
matter_create_request_data_split_invoice_payers_inner_from_dict = MatterCreateRequestDataSplitInvoicePayersInner.from_dict(matter_create_request_data_split_invoice_payers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


