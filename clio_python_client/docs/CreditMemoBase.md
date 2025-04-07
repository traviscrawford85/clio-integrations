# CreditMemoBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *CreditMemo* | [optional] 
**etag** | **str** | ETag for the *CreditMemo* | [optional] 
**var_date** | **date** | Date the *CreditMemo* was recorded (as a ISO-8601 date) | [optional] 
**amount** | **float** | Total amount credited | [optional] 
**description** | **str** | A detailed description for the *CreditMemo* | [optional] 
**discount** | **bool** | Whether the *CreditMemo* is applied as discount | [optional] 
**voided_at** | **datetime** | Time the *CreditMemo* was voided (as a ISO-8601 timestamp) | [optional] 
**created_at** | **datetime** | The time the *CreditMemo* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *CreditMemo* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.credit_memo_base import CreditMemoBase

# TODO update the JSON string below
json = "{}"
# create an instance of CreditMemoBase from a JSON string
credit_memo_base_instance = CreditMemoBase.from_json(json)
# print the JSON string representation of the object
print(CreditMemoBase.to_json())

# convert the object into a dict
credit_memo_base_dict = credit_memo_base_instance.to_dict()
# create an instance of CreditMemoBase from a dict
credit_memo_base_from_dict = CreditMemoBase.from_dict(credit_memo_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


