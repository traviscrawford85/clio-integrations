# MedicalRecordsRequestUpdateRequestDataMedicalBillsInnerPayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Lien amount. | [optional] 
**holder_id** | **int** | The unique identifier for a single Damage associated with the MedicalRecordsRequest. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**mark_as_lien** | **bool** | Mark record as Lien. | [optional] 

## Example

```python
from openapi_client.models.medical_records_request_update_request_data_medical_bills_inner_payers_inner import MedicalRecordsRequestUpdateRequestDataMedicalBillsInnerPayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordsRequestUpdateRequestDataMedicalBillsInnerPayersInner from a JSON string
medical_records_request_update_request_data_medical_bills_inner_payers_inner_instance = MedicalRecordsRequestUpdateRequestDataMedicalBillsInnerPayersInner.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordsRequestUpdateRequestDataMedicalBillsInnerPayersInner.to_json())

# convert the object into a dict
medical_records_request_update_request_data_medical_bills_inner_payers_inner_dict = medical_records_request_update_request_data_medical_bills_inner_payers_inner_instance.to_dict()
# create an instance of MedicalRecordsRequestUpdateRequestDataMedicalBillsInnerPayersInner from a dict
medical_records_request_update_request_data_medical_bills_inner_payers_inner_from_dict = MedicalRecordsRequestUpdateRequestDataMedicalBillsInnerPayersInner.from_dict(medical_records_request_update_request_data_medical_bills_inner_payers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


