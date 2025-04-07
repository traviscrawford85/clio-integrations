# ClioPaymentsLinkCreateRequestDataDestinationAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the bank account that the payment will be deposited into. | 

## Example

```python
from openapi_client.models.clio_payments_link_create_request_data_destination_account import ClioPaymentsLinkCreateRequestDataDestinationAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ClioPaymentsLinkCreateRequestDataDestinationAccount from a JSON string
clio_payments_link_create_request_data_destination_account_instance = ClioPaymentsLinkCreateRequestDataDestinationAccount.from_json(json)
# print the JSON string representation of the object
print(ClioPaymentsLinkCreateRequestDataDestinationAccount.to_json())

# convert the object into a dict
clio_payments_link_create_request_data_destination_account_dict = clio_payments_link_create_request_data_destination_account_instance.to_dict()
# create an instance of ClioPaymentsLinkCreateRequestDataDestinationAccount from a dict
clio_payments_link_create_request_data_destination_account_from_dict = ClioPaymentsLinkCreateRequestDataDestinationAccount.from_dict(clio_payments_link_create_request_data_destination_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


