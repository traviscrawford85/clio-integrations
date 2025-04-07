# BankAccountUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BankAccountUpdateRequestData**](BankAccountUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.bank_account_update_request import BankAccountUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountUpdateRequest from a JSON string
bank_account_update_request_instance = BankAccountUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(BankAccountUpdateRequest.to_json())

# convert the object into a dict
bank_account_update_request_dict = bank_account_update_request_instance.to_dict()
# create an instance of BankAccountUpdateRequest from a dict
bank_account_update_request_from_dict = BankAccountUpdateRequest.from_dict(bank_account_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


