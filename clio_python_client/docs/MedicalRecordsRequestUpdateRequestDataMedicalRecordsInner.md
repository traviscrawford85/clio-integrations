# MedicalRecordsRequestUpdateRequestDataMedicalRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **int** | The unique identifier for a single MedicalRecord associated with the MedicalRecordsRequest. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**end_date** | **datetime** | End date for Medical Record. | [optional] 
**start_date** | **datetime** | Start date for Medical Record. | [optional] 

## Example

```python
from openapi_client.models.medical_records_request_update_request_data_medical_records_inner import MedicalRecordsRequestUpdateRequestDataMedicalRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordsRequestUpdateRequestDataMedicalRecordsInner from a JSON string
medical_records_request_update_request_data_medical_records_inner_instance = MedicalRecordsRequestUpdateRequestDataMedicalRecordsInner.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordsRequestUpdateRequestDataMedicalRecordsInner.to_json())

# convert the object into a dict
medical_records_request_update_request_data_medical_records_inner_dict = medical_records_request_update_request_data_medical_records_inner_instance.to_dict()
# create an instance of MedicalRecordsRequestUpdateRequestDataMedicalRecordsInner from a dict
medical_records_request_update_request_data_medical_records_inner_from_dict = MedicalRecordsRequestUpdateRequestDataMedicalRecordsInner.from_dict(medical_records_request_update_request_data_medical_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


