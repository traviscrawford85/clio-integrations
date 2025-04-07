# MedicalRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *MedicalRecord* | [optional] 
**document_id** | **int** | The id of the document associated with the Medical Record | [optional] 
**etag** | **str** | ETag for the *MedicalRecord* | [optional] 
**end_date** | **datetime** | End date for *MedicalRecord* (as a ISO-8601 date) | [optional] 
**start_date** | **datetime** | Start date for *MedicalRecord* (as a ISO-8601 date) | [optional] 
**created_at** | **datetime** | The time the *MedicalRecord* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *MedicalRecord* was last updated (as a ISO-8601 timestamp) | [optional] 
**matter** | [**MatterBase**](MatterBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.medical_record import MedicalRecord

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecord from a JSON string
medical_record_instance = MedicalRecord.from_json(json)
# print the JSON string representation of the object
print(MedicalRecord.to_json())

# convert the object into a dict
medical_record_dict = medical_record_instance.to_dict()
# create an instance of MedicalRecord from a dict
medical_record_from_dict = MedicalRecord.from_dict(medical_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


