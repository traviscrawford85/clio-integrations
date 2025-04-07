# MedicalBill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *MedicalBill* | [optional] 
**adjustment** | **float** | Adjustment for Medical Bill | [optional] 
**amount** | **float** | Amount for Medical Bill | [optional] 
**bill_date** | **date** | Bill date for Medical Bill (as a ISO-8601 date) | [optional] 
**bill_received_date** | **date** | Bill received date for Medical Bill (as a ISO-8601 date) | [optional] 
**damage_type** | **str** | Damage Type | [optional] 
**document_id** | **int** | The id of the document associated with the Medical Bill | [optional] 
**etag** | **str** | ETag for the *MedicalBill* | [optional] 
**name** | **str** | Name of the Medical Bill | [optional] 
**created_at** | **datetime** | The time the *MedicalBill* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *MedicalBill* was last updated (as a ISO-8601 timestamp) | [optional] 
**matter** | [**MatterBase**](MatterBase.md) |  | [optional] 
**liens** | [**List[LienBase]**](LienBase.md) | Lien | [optional] 

## Example

```python
from openapi_client.models.medical_bill import MedicalBill

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalBill from a JSON string
medical_bill_instance = MedicalBill.from_json(json)
# print the JSON string representation of the object
print(MedicalBill.to_json())

# convert the object into a dict
medical_bill_dict = medical_bill_instance.to_dict()
# create an instance of MedicalBill from a dict
medical_bill_from_dict = MedicalBill.from_dict(medical_bill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


