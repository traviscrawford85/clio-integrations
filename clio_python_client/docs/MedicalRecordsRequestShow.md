# MedicalRecordsRequestShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MedicalRecordsRequest**](MedicalRecordsRequest.md) |  | 

## Example

```python
from openapi_client.models.medical_records_request_show import MedicalRecordsRequestShow

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordsRequestShow from a JSON string
medical_records_request_show_instance = MedicalRecordsRequestShow.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordsRequestShow.to_json())

# convert the object into a dict
medical_records_request_show_dict = medical_records_request_show_instance.to_dict()
# create an instance of MedicalRecordsRequestShow from a dict
medical_records_request_show_from_dict = MedicalRecordsRequestShow.from_dict(medical_records_request_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


