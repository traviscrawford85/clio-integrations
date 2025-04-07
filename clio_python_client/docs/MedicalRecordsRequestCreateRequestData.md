# MedicalRecordsRequestCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bills_follow_up_date** | **datetime** | Follow up date for Medical Bills. (Expects an ISO-8601 date). | [optional] 
**bills_request_date** | **datetime** | Requested date for Medical Bills. (Expects an ISO-8601 date). | [optional] 
**bills_status** | **str** | Current status for the Medical Bills. | 
**description** | **str** | Detailed description of the Medical Records Detail. | [optional] 
**in_treatment** | **bool** | True or false value to record if the treatment has been completed. | 
**matter_id** | **int** | The ID of the matter that the Medical Records Detail belongs to. | 
**medical_bills** | [**List[MedicalRecordsRequestCreateRequestDataMedicalBillsInner]**](MedicalRecordsRequestCreateRequestDataMedicalBillsInner.md) |  | [optional] 
**medical_provider_id** | **int** | The unique identifier for a single Medical Provider associated with this Medical Records Detail. | 
**medical_records** | [**List[MedicalRecordsRequestCreateRequestDataMedicalRecordsInner]**](MedicalRecordsRequestCreateRequestDataMedicalRecordsInner.md) |  | [optional] 
**records_follow_up_date** | **datetime** | Follow up date for Medical Records. (Expects an ISO-8601 date). | [optional] 
**records_request_date** | **datetime** | Requested date for Medical Records. (Expects an ISO-8601 date). | [optional] 
**records_status** | **str** | Current status for the Medical Records. | 
**treatment_end_date** | **datetime** | End date for the treatment. (Expects an ISO-8601 date). | [optional] 
**treatment_start_date** | **datetime** | Start date for the treatment. (Expects an ISO-8601 date). | [optional] 

## Example

```python
from openapi_client.models.medical_records_request_create_request_data import MedicalRecordsRequestCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordsRequestCreateRequestData from a JSON string
medical_records_request_create_request_data_instance = MedicalRecordsRequestCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordsRequestCreateRequestData.to_json())

# convert the object into a dict
medical_records_request_create_request_data_dict = medical_records_request_create_request_data_instance.to_dict()
# create an instance of MedicalRecordsRequestCreateRequestData from a dict
medical_records_request_create_request_data_from_dict = MedicalRecordsRequestCreateRequestData.from_dict(medical_records_request_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


