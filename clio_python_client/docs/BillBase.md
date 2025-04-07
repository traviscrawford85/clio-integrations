# BillBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Bill* | [optional] 
**etag** | **str** | ETag for the *Bill* | [optional] 
**number** | **str** | The *Bill* identifier (not necessarily numeric)&#39; | [optional] 
**issued_at** | **date** | The time the *Bill* was issued (as a ISO-8601 date) | [optional] 
**created_at** | **datetime** | The time the *Bill* was created (as a ISO-8601 timestamp) | [optional] 
**due_at** | **date** | The date the *Bill* is due (as a ISO-8601 date) | [optional] 
**tax_rate** | **float** | The tax rate to the *Bill* | [optional] 
**secondary_tax_rate** | **float** | A secondary tax rate applied to the *Bill* | [optional] 
**updated_at** | **datetime** | The time the *Bill* was last updated (as a ISO-8601 timestamp) | [optional] 
**subject** | **str** | The subject of the *Bill* | [optional] 
**purchase_order** | **str** | The purchase order of the *Bill* | [optional] 
**type** | **str** | The type of the *Bill* | [optional] 
**memo** | **str** | A memo for the *Bill* | [optional] 
**start_at** | **date** | The time the billing period starts (as a ISO-8601 date) | [optional] 
**end_at** | **date** | The time the billing period ends (as a ISO-8601 date) | [optional] 
**balance** | **float** | The outstanding balance of the *Bill* | [optional] 
**state** | **str** | The billing state the *Bill* is in | [optional] 
**kind** | **str** | The kind of the *Bill* | [optional] 
**total** | **float** | The total with interest of the *Bill* | [optional] 
**paid** | **float** | The total amount paid for the *Bill* | [optional] 
**paid_at** | **datetime** | The date of the last payment on the *Bill* | [optional] 
**pending** | **float** | The amount of pending credit card payments on the *Bill* | [optional] 
**due** | **float** | The total amount of the *Bill* with interest and less discounts | [optional] 
**discount_services_only** | **str** | The selected discount is applied to services only. | [optional] 
**can_update** | **bool** | This value indicates if your *Bill*&#39;s line items and information can be updated. | [optional] 
**credits_issued** | **float** | The total credits issued for the *Bill* | [optional] 
**shared** | **bool** | Whether the *Bill* is a shared | [optional] 
**last_sent_at** | **datetime** | The last time the *Bill* was sent (as a ISO-8601 date) | [optional] 
**services_secondary_tax** | **float** | The total secondary tax of the bill&#39;s line items of a service kind | [optional] 
**services_sub_total** | **float** | The sub total of all the bill&#39;s line items of a service kind | [optional] 
**services_tax** | **float** | The total tax of the bill&#39;s line items of a service kind | [optional] 
**services_taxable_sub_total** | **int** | The services portion of the bill&#39;s primary tax | [optional] 
**services_secondary_taxable_sub_total** | **int** | The services portion of the bill&#39;s secondary tax | [optional] 
**taxable_sub_total** | **int** | The total taxable bill amount | [optional] 
**secondary_taxable_sub_total** | **int** | The subtotal of the bill&#39;s secondary tax | [optional] 
**sub_total** | **float** | Sub total for the *Bill* | [optional] 
**tax_sum** | **float** | Sum of primary tax for the model | [optional] 
**secondary_tax_sum** | **float** | Sum of secondary tax for the model | [optional] 
**total_tax** | **float** | The total amount of tax for the bill. | [optional] 
**available_state_transitions** | **List[str]** | The available *Bill* state transitions. | [optional] 

## Example

```python
from openapi_client.models.bill_base import BillBase

# TODO update the JSON string below
json = "{}"
# create an instance of BillBase from a JSON string
bill_base_instance = BillBase.from_json(json)
# print the JSON string representation of the object
print(BillBase.to_json())

# convert the object into a dict
bill_base_dict = bill_base_instance.to_dict()
# create an instance of BillBase from a dict
bill_base_from_dict = BillBase.from_dict(bill_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


