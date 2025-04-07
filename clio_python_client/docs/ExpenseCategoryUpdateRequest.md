# ExpenseCategoryUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExpenseCategoryUpdateRequestData**](ExpenseCategoryUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.expense_category_update_request import ExpenseCategoryUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseCategoryUpdateRequest from a JSON string
expense_category_update_request_instance = ExpenseCategoryUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ExpenseCategoryUpdateRequest.to_json())

# convert the object into a dict
expense_category_update_request_dict = expense_category_update_request_instance.to_dict()
# create an instance of ExpenseCategoryUpdateRequest from a dict
expense_category_update_request_from_dict = ExpenseCategoryUpdateRequest.from_dict(expense_category_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


