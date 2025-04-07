# Payment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Payment* | [optional] 
**etag** | **str** | ETag for the *Payment* | [optional] 
**description** | **str** | A detailed description of the *Payment* | [optional] 
**reference** | **str** | A reference for the payment | [optional] 
**amount** | **float** | Total amount paid. The default is 0.00. | [optional] 
**var_date** | **date** | The date the *Payment* was recorded (as a ISO-8601 date) | [optional] 
**source_fund_type** | **str** | The fund type for *Payment* source | [optional] 
**voided_at** | **datetime** | Time the *Payment* was voided (as a ISO-8601 timestamp) | [optional] 
**created_at** | **datetime** | The time the *Payment* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Payment* was last updated (as a ISO-8601 timestamp) | [optional] 
**contact** | [**ContactBase**](ContactBase.md) |  | [optional] 
**user** | [**UserBase**](UserBase.md) |  | [optional] 
**source_bank_account** | [**BankAccountBase**](BankAccountBase.md) |  | [optional] 
**destination_bank_account** | [**BankAccountBase**](BankAccountBase.md) |  | [optional] 
**allocations** | [**List[AllocationBase]**](AllocationBase.md) | Allocation | [optional] 

## Example

```python
from openapi_client.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print(Payment.to_json())

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_from_dict = Payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


