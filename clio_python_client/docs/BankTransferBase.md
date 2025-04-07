# BankTransferBase


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

## Example

```python
from openapi_client.models.bank_transfer_base import BankTransferBase

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransferBase from a JSON string
bank_transfer_base_instance = BankTransferBase.from_json(json)
# print the JSON string representation of the object
print(BankTransferBase.to_json())

# convert the object into a dict
bank_transfer_base_dict = bank_transfer_base_instance.to_dict()
# create an instance of BankTransferBase from a dict
bank_transfer_base_from_dict = BankTransferBase.from_dict(bank_transfer_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


