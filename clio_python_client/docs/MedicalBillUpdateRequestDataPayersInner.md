# MedicalBillUpdateRequestDataPayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Lien amount. | [optional] 
**holder_id** | **int** | Lien holder ID | [optional] 
**mark_as_lien** | **bool** | Mark record as Lien. | [optional] 

## Example

```python
from openapi_client.models.medical_bill_update_request_data_payers_inner import MedicalBillUpdateRequestDataPayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalBillUpdateRequestDataPayersInner from a JSON string
medical_bill_update_request_data_payers_inner_instance = MedicalBillUpdateRequestDataPayersInner.from_json(json)
# print the JSON string representation of the object
print(MedicalBillUpdateRequestDataPayersInner.to_json())

# convert the object into a dict
medical_bill_update_request_data_payers_inner_dict = medical_bill_update_request_data_payers_inner_instance.to_dict()
# create an instance of MedicalBillUpdateRequestDataPayersInner from a dict
medical_bill_update_request_data_payers_inner_from_dict = MedicalBillUpdateRequestDataPayersInner.from_dict(medical_bill_update_request_data_payers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


