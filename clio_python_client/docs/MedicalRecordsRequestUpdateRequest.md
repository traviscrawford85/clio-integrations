# MedicalRecordsRequestUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MedicalRecordsRequestUpdateRequestData**](MedicalRecordsRequestUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.medical_records_request_update_request import MedicalRecordsRequestUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordsRequestUpdateRequest from a JSON string
medical_records_request_update_request_instance = MedicalRecordsRequestUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordsRequestUpdateRequest.to_json())

# convert the object into a dict
medical_records_request_update_request_dict = medical_records_request_update_request_instance.to_dict()
# create an instance of MedicalRecordsRequestUpdateRequest from a dict
medical_records_request_update_request_from_dict = MedicalRecordsRequestUpdateRequest.from_dict(medical_records_request_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


