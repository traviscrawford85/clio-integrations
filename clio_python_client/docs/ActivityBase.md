# ActivityBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Activity* | [optional] 
**etag** | **str** | ETag for the *Activity* | [optional] 
**type** | **str** | The type of the *Activity* | [optional] 
**var_date** | **date** | The date the *Activity* was performed (as a ISO-8601 date) | [optional] 
**quantity_in_hours** | **float** | The number of hours the TimeEntry took. | [optional] 
**rounded_quantity_in_hours** | **float** | The number of hours rounded accordingly to the billing settings. The rounded value is used to calculate the total.  | [optional] 
**quantity** | **float** | The field is applicable to TimeEntry, ExpenseEntry, and SoftCostEntry.  **Version &lt;&#x3D; 4.0.3:** The number of hours the TimeEntry took.  **Latest version:** The number of seconds the TimeEntry took.  | [optional] 
**rounded_quantity** | **float** | The field is applicable to time entries only.  **Version &lt;&#x3D; 4.0.3:** The number of hours rounded accordingly to the billing settings. The rounded value is used to calculate the total.  **Latest version:** The number of seconds rounded accordingly to the billing settings. The rounded value is used to calculate the total.  | [optional] 
**quantity_redacted** | **bool** | Is &#x60;true&#x60; if any of the following fields are redacted: &#x60;quantity&#x60;, &#x60;rounded_quantity&#x60;, &#x60;rounded_quantity_in_hours&#x60;, &#x60;quantity_in_hours&#x60;, &#x60;total&#x60;, &#x60;non_billable_total&#x60;  | [optional] 
**price** | **float** | The hourly or flat rate of the *Activity* | [optional] 
**note** | **str** | The details about the *Activity* | [optional] 
**flat_rate** | **bool** | Whether the *Activity* is a flat rate | [optional] 
**billed** | **bool** | Whether the *Activity* has been added to an active bill that is in the state of &#x60;awaiting_payment&#x60; or &#x60;paid&#x60; | [optional] 
**on_bill** | **bool** | Whether the *Activity* has been added to an active bill that is in the state of &#x60;draft&#x60;, &#x60;awaiting_approval&#x60;, &#x60;awaiting_payment&#x60; or &#x60;paid&#x60; | [optional] 
**total** | **float** | The total cost of draft, billable and billed items in the *Activity* | [optional] 
**contingency_fee** | **bool** | Whether or not the *Activity* is a contingency fee | [optional] 
**created_at** | **datetime** | The time the *Activity* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Activity* was last updated (as a ISO-8601 timestamp) | [optional] 
**reference** | **str** | A check reference for a HardCostEntry. | [optional] 
**non_billable** | **bool** | Whether the *Activity* is non-billable | [optional] 
**non_billable_total** | **float** | The total cost of non-billable items in the *Activity* | [optional] 
**no_charge** | **bool** | Whether the non-billable *Activity* is shown on the bill. | [optional] 
**tax_setting** | **str** | The option denoting whether primary tax, secondary tax, or both is applied to an expense entry. | [optional] 
**currency** | **object** | The currency of the *Activity* | [optional] 

## Example

```python
from openapi_client.models.activity_base import ActivityBase

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityBase from a JSON string
activity_base_instance = ActivityBase.from_json(json)
# print the JSON string representation of the object
print(ActivityBase.to_json())

# convert the object into a dict
activity_base_dict = activity_base_instance.to_dict()
# create an instance of ActivityBase from a dict
activity_base_from_dict = ActivityBase.from_dict(activity_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


