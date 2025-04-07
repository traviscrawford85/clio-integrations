# ClioPaymentsLinkCreateRequestDataDestinationContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Only applicable for a direct payment. The contact that the payment will be associated with. If not defined, and the payment is collecting an unallocated balance, then the payment can be associated with a contact manually within Manage after it has been made. | [optional] 

## Example

```python
from openapi_client.models.clio_payments_link_create_request_data_destination_contact import ClioPaymentsLinkCreateRequestDataDestinationContact

# TODO update the JSON string below
json = "{}"
# create an instance of ClioPaymentsLinkCreateRequestDataDestinationContact from a JSON string
clio_payments_link_create_request_data_destination_contact_instance = ClioPaymentsLinkCreateRequestDataDestinationContact.from_json(json)
# print the JSON string representation of the object
print(ClioPaymentsLinkCreateRequestDataDestinationContact.to_json())

# convert the object into a dict
clio_payments_link_create_request_data_destination_contact_dict = clio_payments_link_create_request_data_destination_contact_instance.to_dict()
# create an instance of ClioPaymentsLinkCreateRequestDataDestinationContact from a dict
clio_payments_link_create_request_data_destination_contact_from_dict = ClioPaymentsLinkCreateRequestDataDestinationContact.from_dict(clio_payments_link_create_request_data_destination_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


