# BankTransferShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BankTransfer**](BankTransfer.md) |  | 

## Example

```python
from openapi_client.models.bank_transfer_show import BankTransferShow

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransferShow from a JSON string
bank_transfer_show_instance = BankTransferShow.from_json(json)
# print the JSON string representation of the object
print(BankTransferShow.to_json())

# convert the object into a dict
bank_transfer_show_dict = bank_transfer_show_instance.to_dict()
# create an instance of BankTransferShow from a dict
bank_transfer_show_from_dict = BankTransferShow.from_dict(bank_transfer_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


