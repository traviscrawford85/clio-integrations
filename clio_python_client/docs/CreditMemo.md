# CreditMemo


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
**user** | [**UserBase**](UserBase.md) |  | [optional] 
**contact** | [**ContactBase**](ContactBase.md) |  | [optional] 
**allocations** | [**List[AllocationBase]**](AllocationBase.md) | Allocation | [optional] 

## Example

```python
from openapi_client.models.credit_memo import CreditMemo

# TODO update the JSON string below
json = "{}"
# create an instance of CreditMemo from a JSON string
credit_memo_instance = CreditMemo.from_json(json)
# print the JSON string representation of the object
print(CreditMemo.to_json())

# convert the object into a dict
credit_memo_dict = credit_memo_instance.to_dict()
# create an instance of CreditMemo from a dict
credit_memo_from_dict = CreditMemo.from_dict(credit_memo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


