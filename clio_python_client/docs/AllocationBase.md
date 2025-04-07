# AllocationBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Allocation* | [optional] 
**etag** | **str** | ETag for the *Allocation* | [optional] 
**var_date** | **date** | The date the allocation was applied (as a ISO-8601 date) | [optional] 
**amount** | **float** | The total amount of money that the user has allocated | [optional] 
**interest** | **bool** | Whether the allocation is applied to interest amount | [optional] 
**voided_at** | **datetime** | Time the *Allocation* was voided (as a ISO-8601 timestamp) | [optional] 
**created_at** | **datetime** | The time the *Allocation* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Allocation* was last updated (as a ISO-8601 timestamp) | [optional] 
**description** | **str** | The description from the associated Credit Memo (if applicable) | [optional] 
**has_online_payment** | **bool** | Whether this allocation is associated with an online payment or not | [optional] 
**destroyable** | **bool** | Whether the record can be deleted or not | [optional] 
**payment_type** | **str** | A string indicating whether the payment is a card or an eCheck payment. | [optional] 

## Example

```python
from openapi_client.models.allocation_base import AllocationBase

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationBase from a JSON string
allocation_base_instance = AllocationBase.from_json(json)
# print the JSON string representation of the object
print(AllocationBase.to_json())

# convert the object into a dict
allocation_base_dict = allocation_base_instance.to_dict()
# create an instance of AllocationBase from a dict
allocation_base_from_dict = AllocationBase.from_dict(allocation_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


