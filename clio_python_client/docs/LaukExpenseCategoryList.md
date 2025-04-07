# LaukExpenseCategoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LaukExpenseCategory]**](LaukExpenseCategory.md) | LaukExpenseCategory List Response | 

## Example

```python
from openapi_client.models.lauk_expense_category_list import LaukExpenseCategoryList

# TODO update the JSON string below
json = "{}"
# create an instance of LaukExpenseCategoryList from a JSON string
lauk_expense_category_list_instance = LaukExpenseCategoryList.from_json(json)
# print the JSON string representation of the object
print(LaukExpenseCategoryList.to_json())

# convert the object into a dict
lauk_expense_category_list_dict = lauk_expense_category_list_instance.to_dict()
# create an instance of LaukExpenseCategoryList from a dict
lauk_expense_category_list_from_dict = LaukExpenseCategoryList.from_dict(lauk_expense_category_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


