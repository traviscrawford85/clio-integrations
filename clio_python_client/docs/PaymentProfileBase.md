# PaymentProfileBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *PaymentProfile* | [optional] 
**etag** | **str** | ETag for the *PaymentProfile* | [optional] 
**created_at** | **datetime** | The time the *PaymentProfile* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *PaymentProfile* was last updated (as a ISO-8601 timestamp) | [optional] 
**billing_setting_id** | **int** | The unique identifier for the *PaymentProfile | [optional] 
**name** | **str** | The name of the *PaymentProfile | [optional] 
**terms** | **int** | The total grace period for the *PaymentProfile | [optional] 
**discount_rate** | **float** | The early payment discount rate for the *PaymentProfile | [optional] 
**discount_period** | **int** | The early payment discount period for the *PaymentProfile | [optional] 
**interest_rate** | **float** | The interest rate for the *PaymentProfile | [optional] 
**interest_period** | **int** | The interest period interval for the *PaymentProfile | [optional] 
**interest_type** | **str** | The type of interest to be calculated for the *PaymentProfile (Simple or Compound) | [optional] 

## Example

```python
from openapi_client.models.payment_profile_base import PaymentProfileBase

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentProfileBase from a JSON string
payment_profile_base_instance = PaymentProfileBase.from_json(json)
# print the JSON string representation of the object
print(PaymentProfileBase.to_json())

# convert the object into a dict
payment_profile_base_dict = payment_profile_base_instance.to_dict()
# create an instance of PaymentProfileBase from a dict
payment_profile_base_from_dict = PaymentProfileBase.from_dict(payment_profile_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


