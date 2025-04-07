# ExpenseCategoryCreateRequestDataGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Group associated with the ExpenseCategory. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**deleted** | **bool** | A flag to determine if this Group should lose access to this ExpenseCategory. | [optional] 

## Example

```python
from openapi_client.models.expense_category_create_request_data_groups_inner import ExpenseCategoryCreateRequestDataGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseCategoryCreateRequestDataGroupsInner from a JSON string
expense_category_create_request_data_groups_inner_instance = ExpenseCategoryCreateRequestDataGroupsInner.from_json(json)
# print the JSON string representation of the object
print(ExpenseCategoryCreateRequestDataGroupsInner.to_json())

# convert the object into a dict
expense_category_create_request_data_groups_inner_dict = expense_category_create_request_data_groups_inner_instance.to_dict()
# create an instance of ExpenseCategoryCreateRequestDataGroupsInner from a dict
expense_category_create_request_data_groups_inner_from_dict = ExpenseCategoryCreateRequestDataGroupsInner.from_dict(expense_category_create_request_data_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


