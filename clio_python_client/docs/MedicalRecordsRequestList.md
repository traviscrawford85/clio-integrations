# MedicalRecordsRequestList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MedicalRecordsRequest]**](MedicalRecordsRequest.md) | MedicalRecordsRequest List Response | 

## Example

```python
from openapi_client.models.medical_records_request_list import MedicalRecordsRequestList

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordsRequestList from a JSON string
medical_records_request_list_instance = MedicalRecordsRequestList.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordsRequestList.to_json())

# convert the object into a dict
medical_records_request_list_dict = medical_records_request_list_instance.to_dict()
# create an instance of MedicalRecordsRequestList from a dict
medical_records_request_list_from_dict = MedicalRecordsRequestList.from_dict(medical_records_request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


