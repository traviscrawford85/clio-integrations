# BankAccountUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | Account number for the BankAccount. | [optional] 
**controlled_account** | **bool** | Whether is a controlled account. | [optional] 
**currency** | **str** | Currency the BankAccount is in. | [optional] 
**default_account** | **bool** | Whether or not the BankAccount should be the default account. | [optional] 
**domicile_branch** | **str** | Branch where the BankAccount was opened. | [optional] 
**general_ledger_number** | **str** | General ledger number used for the Law Society of Alberta. | [optional] 
**holder** | **str** | BankAccount holder. | [optional] 
**institution** | **str** | Financial institution. | [optional] 
**name** | **str** | BankAccount name. | [optional] 
**swift** | **str** | Identification code for the financial institution. | [optional] 
**transit_number** | **str** | Transit number for the BankAccount branch. | [optional] 

## Example

```python
from openapi_client.models.bank_account_update_request_data import BankAccountUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountUpdateRequestData from a JSON string
bank_account_update_request_data_instance = BankAccountUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(BankAccountUpdateRequestData.to_json())

# convert the object into a dict
bank_account_update_request_data_dict = bank_account_update_request_data_instance.to_dict()
# create an instance of BankAccountUpdateRequestData from a dict
bank_account_update_request_data_from_dict = BankAccountUpdateRequestData.from_dict(bank_account_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


