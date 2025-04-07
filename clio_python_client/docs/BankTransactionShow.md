# BankTransactionShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BankTransaction**](BankTransaction.md) |  | 

## Example

```python
from openapi_client.models.bank_transaction_show import BankTransactionShow

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionShow from a JSON string
bank_transaction_show_instance = BankTransactionShow.from_json(json)
# print the JSON string representation of the object
print(BankTransactionShow.to_json())

# convert the object into a dict
bank_transaction_show_dict = bank_transaction_show_instance.to_dict()
# create an instance of BankTransactionShow from a dict
bank_transaction_show_from_dict = BankTransactionShow.from_dict(bank_transaction_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


