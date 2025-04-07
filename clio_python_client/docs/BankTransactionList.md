# BankTransactionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BankTransaction]**](BankTransaction.md) | BankTransaction List Response | 

## Example

```python
from openapi_client.models.bank_transaction_list import BankTransactionList

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionList from a JSON string
bank_transaction_list_instance = BankTransactionList.from_json(json)
# print the JSON string representation of the object
print(BankTransactionList.to_json())

# convert the object into a dict
bank_transaction_list_dict = bank_transaction_list_instance.to_dict()
# create an instance of BankTransactionList from a dict
bank_transaction_list_from_dict = BankTransactionList.from_dict(bank_transaction_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


