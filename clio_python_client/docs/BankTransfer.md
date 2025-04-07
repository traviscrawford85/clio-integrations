# BankTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *BankTransfer* | [optional] 
**etag** | **str** | ETag for the *BankTransfer* | [optional] 
**amount** | **float** | The amount of the transfer. | [optional] 
**var_date** | **datetime** | The date of the transfer. | [optional] 
**description** | **str** | The description of the transfer. | [optional] 
**primary_authorizer** | **str** | The primary authorizer of the transfer. | [optional] 
**secondary_authorizer** | **str** | The secondary authorizer of the transfer. | [optional] 
**created_at** | **datetime** | The time the *BankTransfer* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *BankTransfer* was last updated (as a ISO-8601 timestamp) | [optional] 
**client** | [**ContactBase**](ContactBase.md) |  | [optional] 
**destination_account** | [**BankAccountBase**](BankAccountBase.md) |  | [optional] 
**matter** | [**MatterBase**](MatterBase.md) |  | [optional] 
**source_account** | [**BankAccountBase**](BankAccountBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.bank_transfer import BankTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransfer from a JSON string
bank_transfer_instance = BankTransfer.from_json(json)
# print the JSON string representation of the object
print(BankTransfer.to_json())

# convert the object into a dict
bank_transfer_dict = bank_transfer_instance.to_dict()
# create an instance of BankTransfer from a dict
bank_transfer_from_dict = BankTransfer.from_dict(bank_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


