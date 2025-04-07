# MedicalRecordsRequestCreateRequestDataMedicalBillsInnerPayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Lien amount. | 
**holder_id** | **int** | The unique identifier for a single Damage associated with the MedicalRecordsRequest. The keyword &#x60;null&#x60; is not valid for this field. | 
**mark_as_lien** | **bool** | Mark record as Lien. | 

## Example

```python
from openapi_client.models.medical_records_request_create_request_data_medical_bills_inner_payers_inner import MedicalRecordsRequestCreateRequestDataMedicalBillsInnerPayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordsRequestCreateRequestDataMedicalBillsInnerPayersInner from a JSON string
medical_records_request_create_request_data_medical_bills_inner_payers_inner_instance = MedicalRecordsRequestCreateRequestDataMedicalBillsInnerPayersInner.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordsRequestCreateRequestDataMedicalBillsInnerPayersInner.to_json())

# convert the object into a dict
medical_records_request_create_request_data_medical_bills_inner_payers_inner_dict = medical_records_request_create_request_data_medical_bills_inner_payers_inner_instance.to_dict()
# create an instance of MedicalRecordsRequestCreateRequestDataMedicalBillsInnerPayersInner from a dict
medical_records_request_create_request_data_medical_bills_inner_payers_inner_from_dict = MedicalRecordsRequestCreateRequestDataMedicalBillsInnerPayersInner.from_dict(medical_records_request_create_request_data_medical_bills_inner_payers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


