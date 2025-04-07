# MedicalRecordsRequestBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *MedicalRecordsRequest* | [optional] 
**etag** | **str** | ETag for the *MedicalRecordsRequest* | [optional] 
**bills_follow_up_date** | **datetime** | Follow up date for Medical Bills (as a ISO-8601 date) | [optional] 
**bills_request_date** | **datetime** | Date for when the Medical Bills were requested (as a ISO-8601 date) | [optional] 
**bills_status** | **str** | Medical Bills status | [optional] 
**description** | **str** | Description of the Medical Records Detail | [optional] 
**in_treatment** | **bool** | Treatment status for Medical Records Detail | [optional] 
**records_follow_up_date** | **datetime** | Follow up date for Medical Records (as a ISO-8601 date) | [optional] 
**records_request_date** | **datetime** | Date for when the Medical Records were requested (as a ISO-8601 date) | [optional] 
**records_status** | **str** | Medical Records status | [optional] 
**treatment_end_date** | **datetime** | Treatment end date for Medical Records Detail (as a ISO-8601 date) | [optional] 
**treatment_start_date** | **datetime** | Treatment start date for Medical Records Detail (as a ISO-8601 date) | [optional] 
**created_at** | **datetime** | The time the *MedicalRecordsRequest* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *MedicalRecordsRequest* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.medical_records_request_base import MedicalRecordsRequestBase

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordsRequestBase from a JSON string
medical_records_request_base_instance = MedicalRecordsRequestBase.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordsRequestBase.to_json())

# convert the object into a dict
medical_records_request_base_dict = medical_records_request_base_instance.to_dict()
# create an instance of MedicalRecordsRequestBase from a dict
medical_records_request_base_from_dict = MedicalRecordsRequestBase.from_dict(medical_records_request_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


