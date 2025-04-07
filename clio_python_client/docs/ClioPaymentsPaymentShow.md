# ClioPaymentsPaymentShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClioPaymentsPayment**](ClioPaymentsPayment.md) |  | 

## Example

```python
from openapi_client.models.clio_payments_payment_show import ClioPaymentsPaymentShow

# TODO update the JSON string below
json = "{}"
# create an instance of ClioPaymentsPaymentShow from a JSON string
clio_payments_payment_show_instance = ClioPaymentsPaymentShow.from_json(json)
# print the JSON string representation of the object
print(ClioPaymentsPaymentShow.to_json())

# convert the object into a dict
clio_payments_payment_show_dict = clio_payments_payment_show_instance.to_dict()
# create an instance of ClioPaymentsPaymentShow from a dict
clio_payments_payment_show_from_dict = ClioPaymentsPaymentShow.from_dict(clio_payments_payment_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


