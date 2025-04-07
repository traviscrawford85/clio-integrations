# ExpenseCategoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExpenseCategory]**](ExpenseCategory.md) | ExpenseCategory List Response | 

## Example

```python
from openapi_client.models.expense_category_list import ExpenseCategoryList

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseCategoryList from a JSON string
expense_category_list_instance = ExpenseCategoryList.from_json(json)
# print the JSON string representation of the object
print(ExpenseCategoryList.to_json())

# convert the object into a dict
expense_category_list_dict = expense_category_list_instance.to_dict()
# create an instance of ExpenseCategoryList from a dict
expense_category_list_from_dict = ExpenseCategoryList.from_dict(expense_category_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


