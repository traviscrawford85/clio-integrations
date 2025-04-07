# MedicalRecordsRequestUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bills_follow_up_date** | **datetime** | Follow up date for Medical Bills. (Expects an ISO-8601 date). | [optional] 
**bills_request_date** | **datetime** | Requested date for Medical Bills. (Expects an ISO-8601 date). | [optional] 
**bills_status** | **str** | Current status for the Medical Bills. | [optional] 
**description** | **str** | Detailed description of the Medical Records Detail. | [optional] 
**in_treatment** | **bool** | True or false value to record if the treatment has been completed. | [optional] 
**medical_bills** | [**List[MedicalRecordsRequestUpdateRequestDataMedicalBillsInner]**](MedicalRecordsRequestUpdateRequestDataMedicalBillsInner.md) |  | [optional] 
**medical_provider_id** | **int** | The unique identifier for a single Medical Provider associated with this Medical Records Detail. | [optional] 
**medical_records** | [**List[MedicalRecordsRequestUpdateRequestDataMedicalRecordsInner]**](MedicalRecordsRequestUpdateRequestDataMedicalRecordsInner.md) |  | [optional] 
**records_follow_up_date** | **datetime** | Follow up date for Medical Records. (Expects an ISO-8601 date). | [optional] 
**records_request_date** | **datetime** | Requested date for Medical Records. (Expects an ISO-8601 date). | [optional] 
**records_status** | **str** | Current status for the Medical Records. | [optional] 
**treatment_end_date** | **datetime** | End date for the treatment. (Expects an ISO-8601 date). | [optional] 
**treatment_start_date** | **datetime** | Start date for the treatment. (Expects an ISO-8601 date). | [optional] 

## Example

```python
from openapi_client.models.medical_records_request_update_request_data import MedicalRecordsRequestUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordsRequestUpdateRequestData from a JSON string
medical_records_request_update_request_data_instance = MedicalRecordsRequestUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordsRequestUpdateRequestData.to_json())

# convert the object into a dict
medical_records_request_update_request_data_dict = medical_records_request_update_request_data_instance.to_dict()
# create an instance of MedicalRecordsRequestUpdateRequestData from a dict
medical_records_request_update_request_data_from_dict = MedicalRecordsRequestUpdateRequestData.from_dict(medical_records_request_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


