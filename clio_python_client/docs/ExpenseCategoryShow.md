# ExpenseCategoryShow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExpenseCategory**](ExpenseCategory.md) |  | 

## Example

```python
from openapi_client.models.expense_category_show import ExpenseCategoryShow

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseCategoryShow from a JSON string
expense_category_show_instance = ExpenseCategoryShow.from_json(json)
# print the JSON string representation of the object
print(ExpenseCategoryShow.to_json())

# convert the object into a dict
expense_category_show_dict = expense_category_show_instance.to_dict()
# create an instance of ExpenseCategoryShow from a dict
expense_category_show_from_dict = ExpenseCategoryShow.from_dict(expense_category_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


