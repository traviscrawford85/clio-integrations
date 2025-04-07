# ExpenseCategoryCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExpenseCategoryCreateRequestData**](ExpenseCategoryCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.expense_category_create_request import ExpenseCategoryCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseCategoryCreateRequest from a JSON string
expense_category_create_request_instance = ExpenseCategoryCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ExpenseCategoryCreateRequest.to_json())

# convert the object into a dict
expense_category_create_request_dict = expense_category_create_request_instance.to_dict()
# create an instance of ExpenseCategoryCreateRequest from a dict
expense_category_create_request_from_dict = ExpenseCategoryCreateRequest.from_dict(expense_category_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


