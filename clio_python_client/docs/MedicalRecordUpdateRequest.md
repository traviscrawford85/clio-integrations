# MedicalRecordUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MedicalRecordUpdateRequestData**](MedicalRecordUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.medical_record_update_request import MedicalRecordUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordUpdateRequest from a JSON string
medical_record_update_request_instance = MedicalRecordUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordUpdateRequest.to_json())

# convert the object into a dict
medical_record_update_request_dict = medical_record_update_request_instance.to_dict()
# create an instance of MedicalRecordUpdateRequest from a dict
medical_record_update_request_from_dict = MedicalRecordUpdateRequest.from_dict(medical_record_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


