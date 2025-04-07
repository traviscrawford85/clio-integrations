# BankAccountCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BankAccountCreateRequestData**](BankAccountCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.bank_account_create_request import BankAccountCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountCreateRequest from a JSON string
bank_account_create_request_instance = BankAccountCreateRequest.from_json(json)
# print the JSON string representation of the object
print(BankAccountCreateRequest.to_json())

# convert the object into a dict
bank_account_create_request_dict = bank_account_create_request_instance.to_dict()
# create an instance of BankAccountCreateRequest from a dict
bank_account_create_request_from_dict = BankAccountCreateRequest.from_dict(bank_account_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


