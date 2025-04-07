# MedicalRecordUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime** | End date for Medical Record. | [optional] 
**start_date** | **datetime** | Start date for Medical Record. | [optional] 

## Example

```python
from openapi_client.models.medical_record_update_request_data import MedicalRecordUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordUpdateRequestData from a JSON string
medical_record_update_request_data_instance = MedicalRecordUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordUpdateRequestData.to_json())

# convert the object into a dict
medical_record_update_request_data_dict = medical_record_update_request_data_instance.to_dict()
# create an instance of MedicalRecordUpdateRequestData from a dict
medical_record_update_request_data_from_dict = MedicalRecordUpdateRequestData.from_dict(medical_record_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


