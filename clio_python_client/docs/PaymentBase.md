# PaymentBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Payment* | [optional] 
**etag** | **str** | ETag for the *Payment* | [optional] 
**description** | **str** | A detailed description of the *Payment* | [optional] 
**reference** | **str** | A reference for the payment | [optional] 
**amount** | **float** | Total amount paid. The default is 0.00. | [optional] 
**var_date** | **date** | The date the *Payment* was recorded (as a ISO-8601 date) | [optional] 
**source_fund_type** | **str** | The fund type for *Payment* source | [optional] 
**voided_at** | **datetime** | Time the *Payment* was voided (as a ISO-8601 timestamp) | [optional] 
**created_at** | **datetime** | The time the *Payment* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Payment* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.payment_base import PaymentBase

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBase from a JSON string
payment_base_instance = PaymentBase.from_json(json)
# print the JSON string representation of the object
print(PaymentBase.to_json())

# convert the object into a dict
payment_base_dict = payment_base_instance.to_dict()
# create an instance of PaymentBase from a dict
payment_base_from_dict = PaymentBase.from_dict(payment_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


