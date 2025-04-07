# OutstandingClientBalanceBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_matter_ids** | **List[int]** | An array of Matter IDs associated with bills in the unpaid state | [optional] 
**etag** | **str** | ETag for the *OutstandingClientBalance* | [optional] 
**id** | **int** | Unique identifier for the *OutstandingClientBalance* | [optional] 
**last_payment_date** | **date** | The date the most recent payment from the contact was received | [optional] 
**last_shared_date** | **date** | The date of the most recently shared bills through the outstanding balance table | [optional] 
**newest_issued_bill_due_date** | **date** | The due date of the contact&#39;s newest bill | [optional] 
**pending_payments_total** | **float** | The sum of all online payments in a pending state on the outstanding bills | [optional] 
**reminders_enabled** | **bool** | The status of automated reminders for this client | [optional] 
**total_outstanding_balance** | **float** | The sum of all bills in the unpaid state | [optional] 
**created_at** | **datetime** | The time the *OutstandingClientBalance* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *OutstandingClientBalance* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.outstanding_client_balance_base import OutstandingClientBalanceBase

# TODO update the JSON string below
json = "{}"
# create an instance of OutstandingClientBalanceBase from a JSON string
outstanding_client_balance_base_instance = OutstandingClientBalanceBase.from_json(json)
# print the JSON string representation of the object
print(OutstandingClientBalanceBase.to_json())

# convert the object into a dict
outstanding_client_balance_base_dict = outstanding_client_balance_base_instance.to_dict()
# create an instance of OutstandingClientBalanceBase from a dict
outstanding_client_balance_base_from_dict = OutstandingClientBalanceBase.from_dict(outstanding_client_balance_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


