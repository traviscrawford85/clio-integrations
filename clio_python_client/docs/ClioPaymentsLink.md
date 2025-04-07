# ClioPaymentsLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether or not the payment link is active. | [optional] 
**amount** | **float** | The defined amount of the payment link, if set. | [optional] 
**created_at** | **datetime** | The time the *ClioPaymentsLink* was created (as a ISO-8601 timestamp) | [optional] 
**currency** | **str** | The currency the payment link will collect. | [optional] 
**description** | **str** | The defined description of the payment link, if set. | [optional] 
**email_address** | **str** | The email address to pre-fill the field on the the payment link, if set. | [optional] 
**etag** | **str** | ETag for the *ClioPaymentsLink* | [optional] 
**expires_at** | **datetime** | The ISO 8601 date and time the payment link will expire. | [optional] 
**id** | **int** | Unique identifier for the *ClioPaymentsLink* | [optional] 
**is_allocated_as_revenue** | **bool** | Whether the payment link is allocated as revenue. | [optional] 
**redirect_url** | **str** | The URL to redirect the client to after the payment has been made. | [optional] 
**url** | **str** | The URL of the payment link. | [optional] 
**bank_account** | [**BankAccountBase**](BankAccountBase.md) |  | [optional] 
**bill** | [**BillBase**](BillBase.md) |  | [optional] 
**clio_payments_payment** | [**ClioPaymentsPaymentBase**](ClioPaymentsPaymentBase.md) |  | [optional] 
**contact** | [**ContactBase**](ContactBase.md) |  | [optional] 
**destination_account** | [**BankAccountBase**](BankAccountBase.md) |  | [optional] 
**destination_contact** | [**ContactBase**](ContactBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.clio_payments_link import ClioPaymentsLink

# TODO update the JSON string below
json = "{}"
# create an instance of ClioPaymentsLink from a JSON string
clio_payments_link_instance = ClioPaymentsLink.from_json(json)
# print the JSON string representation of the object
print(ClioPaymentsLink.to_json())

# convert the object into a dict
clio_payments_link_dict = clio_payments_link_instance.to_dict()
# create an instance of ClioPaymentsLink from a dict
clio_payments_link_from_dict = ClioPaymentsLink.from_dict(clio_payments_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


