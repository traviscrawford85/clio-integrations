# MedicalBillShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MedicalBill**](MedicalBill.md) |  | 

## Example

```python
from openapi_client.models.medical_bill_show import MedicalBillShow

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalBillShow from a JSON string
medical_bill_show_instance = MedicalBillShow.from_json(json)
# print the JSON string representation of the object
print(MedicalBillShow.to_json())

# convert the object into a dict
medical_bill_show_dict = medical_bill_show_instance.to_dict()
# create an instance of MedicalBillShow from a dict
medical_bill_show_from_dict = MedicalBillShow.from_dict(medical_bill_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


