# MedicalRecordsRequestUpdateRequestDataMedicalBillsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment** | **float** | Adjustment for Medical Bill. | [optional] 
**amount** | **float** | Amount for Medical Bill. | [optional] 
**balance** | **float** | Balance for Medical Bill. | [optional] 
**bill_date** | **date** | Bill date for Medical Bill. (Expects an ISO-8601 date). | [optional] 
**bill_received_date** | **date** | Bill received date for Medical Bill. (Expects an ISO-8601 date). | [optional] 
**document_id** | **int** | The unique identifier for a single Damage associated with the MedicalRecordsRequest. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**name** | **str** | Name for Medical Bill. | [optional] 
**mark_balance_as_lien** | **bool** | Setting the balance of the Medical Bill as a lien. | [optional] 
**payers** | [**List[MedicalRecordsRequestUpdateRequestDataMedicalBillsInnerPayersInner]**](MedicalRecordsRequestUpdateRequestDataMedicalBillsInnerPayersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.medical_records_request_update_request_data_medical_bills_inner import MedicalRecordsRequestUpdateRequestDataMedicalBillsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordsRequestUpdateRequestDataMedicalBillsInner from a JSON string
medical_records_request_update_request_data_medical_bills_inner_instance = MedicalRecordsRequestUpdateRequestDataMedicalBillsInner.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordsRequestUpdateRequestDataMedicalBillsInner.to_json())

# convert the object into a dict
medical_records_request_update_request_data_medical_bills_inner_dict = medical_records_request_update_request_data_medical_bills_inner_instance.to_dict()
# create an instance of MedicalRecordsRequestUpdateRequestDataMedicalBillsInner from a dict
medical_records_request_update_request_data_medical_bills_inner_from_dict = MedicalRecordsRequestUpdateRequestDataMedicalBillsInner.from_dict(medical_records_request_update_request_data_medical_bills_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


