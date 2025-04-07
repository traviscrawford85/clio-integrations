# MedicalRecordShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MedicalRecord**](MedicalRecord.md) |  | 

## Example

```python
from openapi_client.models.medical_record_show import MedicalRecordShow

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalRecordShow from a JSON string
medical_record_show_instance = MedicalRecordShow.from_json(json)
# print the JSON string representation of the object
print(MedicalRecordShow.to_json())

# convert the object into a dict
medical_record_show_dict = medical_record_show_instance.to_dict()
# create an instance of MedicalRecordShow from a dict
medical_record_show_from_dict = MedicalRecordShow.from_dict(medical_record_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


