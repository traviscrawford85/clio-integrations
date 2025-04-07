# MedicalRecordsRequestCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MedicalRecordsRequestCreateRequestData**](MedicalRecordsRequestCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.medical_records_request_create_request import MedicalRecordsRequestCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordsRequestCreateRequest from a JSON string
medical_records_request_create_request_instance = MedicalRecordsRequestCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordsRequestCreateRequest.to_json())

# convert the object into a dict
medical_records_request_create_request_dict = medical_records_request_create_request_instance.to_dict()
# create an instance of MedicalRecordsRequestCreateRequest from a dict
medical_records_request_create_request_from_dict = MedicalRecordsRequestCreateRequest.from_dict(medical_records_request_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


