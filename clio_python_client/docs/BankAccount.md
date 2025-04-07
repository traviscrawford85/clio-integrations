# BankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | The account number for *BankAccount* | [optional] 
**balance** | **float** | The current balance of the *BankAccount* | [optional] 
**bank_transactions_count** | **int** | The number of bank transactions associated with the account. | [optional] 
**clio_payment_page_link** | **str** | Link to Single Payment Page which allows to transfer funds without logging in. | [optional] 
**clio_payment_page_qr_code** | **str** | A QR code that links to a Single Payment Page which allows to transfer funds without logging in. | [optional] 
**clio_payments_enabled** | **bool** | Whether the bank account is connected to Clio Payments | [optional] 
**controlled_account** | **bool** | Whether is a controlled account | [optional] 
**created_at** | **datetime** | The time the *BankAccount* was created (as a ISO-8601 timestamp) | [optional] 
**currency** | **str** | The currency type of the *BankAccount* | [optional] 
**currency_id** | **float** | The currency ID of the *BankAccount* | [optional] 
**default_account** | **bool** | Whether it is the default account | [optional] 
**domicile_branch** | **str** | The name of the branch where the account was opened | [optional] 
**etag** | **str** | ETag for the *BankAccount* | [optional] 
**general_ledger_number** | **str** | General ledger number | [optional] 
**holder** | **str** | The name of the person or business that owns the *BankAccount* | [optional] 
**id** | **int** | Unique identifier for the *BankAccount* | [optional] 
**institution** | **str** | The financial institution where the *BankAccount* is registered | [optional] 
**name** | **str** | The name of the *BankAccount* | [optional] 
**swift** | **str** | A unique identification code for the financial institution | [optional] 
**transit_number** | **str** | Transit number for the bank account branch | [optional] 
**type** | **str** | The type of the *BankAccount* | [optional] 
**updated_at** | **datetime** | The time the *BankAccount* was last updated (as a ISO-8601 timestamp) | [optional] 
**user** | [**UserBase**](UserBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.bank_account import BankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccount from a JSON string
bank_account_instance = BankAccount.from_json(json)
# print the JSON string representation of the object
print(BankAccount.to_json())

# convert the object into a dict
bank_account_dict = bank_account_instance.to_dict()
# create an instance of BankAccount from a dict
bank_account_from_dict = BankAccount.from_dict(bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


