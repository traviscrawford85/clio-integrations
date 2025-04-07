# ClioPaymentsPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the payment. | [optional] 
**confirmation_number** | **str** | The confirmation number of the payment. | [optional] 
**created_at** | **datetime** | The time the *ClioPaymentsPayment* was created (as a ISO-8601 timestamp) | [optional] 
**currency** | **str** | The currency the payment was processed in. | [optional] 
**deposit_as_revenue** | **bool** | Whether the payment was deposited as revenue. | [optional] 
**description** | **str** | The description of the payment. | [optional] 
**email_address** | **str** | The email address of the client. | [optional] 
**id** | **int** | Unique identifier for the *ClioPaymentsPayment* | [optional] 
**state** | **str** | The state of the payment (authorized, completed, failed, etc). | [optional] 
**updated_at** | **datetime** | The time the *ClioPaymentsPayment* was last updated (as a ISO-8601 timestamp) | [optional] 
**bank_transaction** | [**BankTransactionBase**](BankTransactionBase.md) |  | [optional] 
**clio_payments_link** | [**ClioPaymentsLinkBase**](ClioPaymentsLinkBase.md) |  | [optional] 
**contact** | [**ContactBase**](ContactBase.md) |  | [optional] 
**destination_account** | [**BankAccountBase**](BankAccountBase.md) |  | [optional] 
**user** | [**UserBase**](UserBase.md) |  | [optional] 
**allocations** | [**List[AllocationBase]**](AllocationBase.md) | Allocation | [optional] 
**bills** | [**List[BillBase]**](BillBase.md) | Bill | [optional] 
**matters** | [**List[MatterBase]**](MatterBase.md) | Matter | [optional] 

## Example

```python
from openapi_client.models.clio_payments_payment import ClioPaymentsPayment

# TODO update the JSON string below
json = "{}"
# create an instance of ClioPaymentsPayment from a JSON string
clio_payments_payment_instance = ClioPaymentsPayment.from_json(json)
# print the JSON string representation of the object
print(ClioPaymentsPayment.to_json())

# convert the object into a dict
clio_payments_payment_dict = clio_payments_payment_instance.to_dict()
# create an instance of ClioPaymentsPayment from a dict
clio_payments_payment_from_dict = ClioPaymentsPayment.from_dict(clio_payments_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


