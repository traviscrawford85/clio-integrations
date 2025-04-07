# MedicalBillUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment** | **float** | Adjustment | [optional] 
**amount** | **float** | Amount | [optional] 
**balance** | **float** | Balance | [optional] 
**bill_date** | **date** | Bill Date (Expects an ISO-8601 date). | [optional] 
**bill_received_date** | **date** | Bill Received Date (Expects an ISO-8601 date). | [optional] 
**mark_balance_as_lien** | **bool** | Mark balance as lien | [optional] 
**name** | **str** | Name | [optional] 
**payers** | [**List[MedicalBillUpdateRequestDataPayersInner]**](MedicalBillUpdateRequestDataPayersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.medical_bill_update_request_data import MedicalBillUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalBillUpdateRequestData from a JSON string
medical_bill_update_request_data_instance = MedicalBillUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(MedicalBillUpdateRequestData.to_json())

# convert the object into a dict
medical_bill_update_request_data_dict = medical_bill_update_request_data_instance.to_dict()
# create an instance of MedicalBillUpdateRequestData from a dict
medical_bill_update_request_data_from_dict = MedicalBillUpdateRequestData.from_dict(medical_bill_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


