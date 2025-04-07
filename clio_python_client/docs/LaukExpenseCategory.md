# LaukExpenseCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificated** | **bool** | Certificated boolean identifier for expense | [optional] 
**civil** | **bool** | Civil boolean identifier for expense | [optional] 
**created_at** | **datetime** | The time the *LaukExpenseCategory* was created (as a ISO-8601 timestamp) | [optional] 
**criminal** | **bool** | Criminal boolean identifier for expense | [optional] 
**etag** | **str** | ETag for the *LaukExpenseCategory* | [optional] 
**id** | **int** | Unique identifier for the *LaukExpenseCategory* | [optional] 
**key** | **str** | Unique key | [optional] 
**name** | **str** | Expense name | [optional] 
**rate** | **float** | Determines rate based on region param | [optional] 
**updated_at** | **datetime** | The time the *LaukExpenseCategory* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.lauk_expense_category import LaukExpenseCategory

# TODO update the JSON string below
json = "{}"
# create an instance of LaukExpenseCategory from a JSON string
lauk_expense_category_instance = LaukExpenseCategory.from_json(json)
# print the JSON string representation of the object
print(LaukExpenseCategory.to_json())

# convert the object into a dict
lauk_expense_category_dict = lauk_expense_category_instance.to_dict()
# create an instance of LaukExpenseCategory from a dict
lauk_expense_category_from_dict = LaukExpenseCategory.from_dict(lauk_expense_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


