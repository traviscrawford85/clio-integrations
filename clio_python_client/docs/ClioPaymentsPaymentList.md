# ClioPaymentsPaymentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClioPaymentsPayment]**](ClioPaymentsPayment.md) | ClioPaymentsPayment List Response | 

## Example

```python
from openapi_client.models.clio_payments_payment_list import ClioPaymentsPaymentList

# TODO update the JSON string below
json = "{}"
# create an instance of ClioPaymentsPaymentList from a JSON string
clio_payments_payment_list_instance = ClioPaymentsPaymentList.from_json(json)
# print the JSON string representation of the object
print(ClioPaymentsPaymentList.to_json())

# convert the object into a dict
clio_payments_payment_list_dict = clio_payments_payment_list_instance.to_dict()
# create an instance of ClioPaymentsPaymentList from a dict
clio_payments_payment_list_from_dict = ClioPaymentsPaymentList.from_dict(clio_payments_payment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


