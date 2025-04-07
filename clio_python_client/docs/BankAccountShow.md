# BankAccountShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BankAccount**](BankAccount.md) |  | 

## Example

```python
from openapi_client.models.bank_account_show import BankAccountShow

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountShow from a JSON string
bank_account_show_instance = BankAccountShow.from_json(json)
# print the JSON string representation of the object
print(BankAccountShow.to_json())

# convert the object into a dict
bank_account_show_dict = bank_account_show_instance.to_dict()
# create an instance of BankAccountShow from a dict
bank_account_show_from_dict = BankAccountShow.from_dict(bank_account_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


