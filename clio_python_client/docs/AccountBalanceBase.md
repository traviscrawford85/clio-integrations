# AccountBalanceBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *AccountBalance* | [optional] 
**balance** | **float** | The current balance of the bank account available to the matter or contact | [optional] 
**type** | **str** | The bank account type. Either Operating or Trust | [optional] 
**name** | **str** | The name of the bank account | [optional] 

## Example

```python
from openapi_client.models.account_balance_base import AccountBalanceBase

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBalanceBase from a JSON string
account_balance_base_instance = AccountBalanceBase.from_json(json)
# print the JSON string representation of the object
print(AccountBalanceBase.to_json())

# convert the object into a dict
account_balance_base_dict = account_balance_base_instance.to_dict()
# create an instance of AccountBalanceBase from a dict
account_balance_base_from_dict = AccountBalanceBase.from_dict(account_balance_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


