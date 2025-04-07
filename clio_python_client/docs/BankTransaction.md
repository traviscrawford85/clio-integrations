# BankTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *BankTransaction* | [optional] 
**type** | **str** | The type of the *BankTransaction* | [optional] 
**etag** | **str** | ETag for the *BankTransaction* | [optional] 
**created_at** | **datetime** | The time the *BankTransaction* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *BankTransaction* was last updated (as a ISO-8601 timestamp) | [optional] 
**bank_account_id** | **int** | The associated bank account. | [optional] 
**source** | **str** | Where the transaction came from. | [optional] 
**confirmation** | **str** | The reference code for the transaction. | [optional] 
**var_date** | **date** | The date of the transaction. | [optional] 
**amount** | **float** | The amount of the transaction. | [optional] 
**currency** | **str** | The currency of the transaction. | [optional] 
**description** | **str** | The description of the transaction. | [optional] 
**exchange_rate** | **float** | The exchange rate of the transaction. | [optional] 
**transaction_type** | **str** | What kind of transaction. | [optional] 
**funds_in** | **float** | The amount of funds received in this transaction. | [optional] 
**funds_out** | **float** | The amount of funds withdrawn in this transaction. | [optional] 
**clio_payments_transaction** | **bool** | Whether the transaction was created through online payments. | [optional] 
**current_account_balance** | **float** | The current account balance. | [optional] 
**read_only_confirmation** | **bool** | Whether the transaction&#39;s reference code is read-only. | [optional] 
**client** | [**ContactBase**](ContactBase.md) |  | [optional] 
**matter** | [**MatterBase**](MatterBase.md) |  | [optional] 
**bank_account** | [**BankAccountBase**](BankAccountBase.md) |  | [optional] 
**bill** | [**BillBase**](BillBase.md) |  | [optional] 
**allocation** | [**AllocationBase**](AllocationBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.bank_transaction import BankTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransaction from a JSON string
bank_transaction_instance = BankTransaction.from_json(json)
# print the JSON string representation of the object
print(BankTransaction.to_json())

# convert the object into a dict
bank_transaction_dict = bank_transaction_instance.to_dict()
# create an instance of BankTransaction from a dict
bank_transaction_from_dict = BankTransaction.from_dict(bank_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


