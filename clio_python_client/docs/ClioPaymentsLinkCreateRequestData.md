# ClioPaymentsLinkCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount to be paid. If not provided, the client will be able to specify an amount. | [optional] 
**currency** | **str** | The currency the payment will be processed in. The supported currency depends on the account&#39;s location (&#39;USD&#39; for a US account). The currency must be a valid ISO 4217 currency code. | 
**description** | **str** | Only applicable for a direct payment. A short description of the purpose of the payment. Max 255 characters. | 
**destination_account** | [**ClioPaymentsLinkCreateRequestDataDestinationAccount**](ClioPaymentsLinkCreateRequestDataDestinationAccount.md) |  | 
**destination_contact** | [**ClioPaymentsLinkCreateRequestDataDestinationContact**](ClioPaymentsLinkCreateRequestDataDestinationContact.md) |  | [optional] 
**duration** | **int** | The amount of time, in seconds, that the payment link will be active for. The maximum allowed value is &#39;7776000&#39; (90 days in seconds). | 
**email_address** | **str** | Pre-fills the relevant field for the client when filling out their details in the payment link. | [optional] 
**is_allocated_as_revenue** | **bool** | Only applicable for a direct payment. If true, the payment will be allocated as revenue. If false, the payment will be collected as an unallocated balance. Payments into trust can not be allocated as revenue. Defaults to false. | [optional] 
**subject** | [**ClioPaymentsLinkCreateRequestDataSubject**](ClioPaymentsLinkCreateRequestDataSubject.md) |  | 

## Example

```python
from openapi_client.models.clio_payments_link_create_request_data import ClioPaymentsLinkCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ClioPaymentsLinkCreateRequestData from a JSON string
clio_payments_link_create_request_data_instance = ClioPaymentsLinkCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(ClioPaymentsLinkCreateRequestData.to_json())

# convert the object into a dict
clio_payments_link_create_request_data_dict = clio_payments_link_create_request_data_instance.to_dict()
# create an instance of ClioPaymentsLinkCreateRequestData from a dict
clio_payments_link_create_request_data_from_dict = ClioPaymentsLinkCreateRequestData.from_dict(clio_payments_link_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


