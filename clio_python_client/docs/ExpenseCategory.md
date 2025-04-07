# ExpenseCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ExpenseCategory* | [optional] 
**etag** | **str** | ETag for the *ExpenseCategory* | [optional] 
**name** | **str** | The name of the expense category | [optional] 
**rate** | **int** | The price charged per unit cost | [optional] 
**entry_type** | **str** | The type of expense entry the category is associated to. Can be either \&quot;hard_cost\&quot;, \&quot;soft_cost\&quot; or \&quot;unassociated\&quot; | [optional] 
**created_at** | **datetime** | The time the *ExpenseCategory* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ExpenseCategory* was last updated (as a ISO-8601 timestamp) | [optional] 
**xero_expense_code** | **str** | Custom Xero expense code for an expense category | [optional] 
**accessible_to_user** | **bool** | Determines if expense category is accessible to user | [optional] 
**tax_setting** | **str** | The type of tax rate applied to the expense category. | [optional] 
**currency** | **object** | The currency details for the expense category | [optional] 
**groups** | [**List[GroupBase]**](GroupBase.md) | Group | [optional] 
**utbms_code** | [**UtbmsCodeBase**](UtbmsCodeBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.expense_category import ExpenseCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseCategory from a JSON string
expense_category_instance = ExpenseCategory.from_json(json)
# print the JSON string representation of the object
print(ExpenseCategory.to_json())

# convert the object into a dict
expense_category_dict = expense_category_instance.to_dict()
# create an instance of ExpenseCategory from a dict
expense_category_from_dict = ExpenseCategory.from_dict(expense_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


