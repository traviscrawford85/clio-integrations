# ExpenseCategoryUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **object** | Currency of the Expense Category. | [optional] 
**entry_type** | **str** | Defaults to unassociated. | [optional] 
**groups** | [**List[ExpenseCategoryCreateRequestDataGroupsInner]**](ExpenseCategoryCreateRequestDataGroupsInner.md) |  | [optional] 
**name** | **str** | Name of the Expense Category. | [optional] 
**rate** | **float** | Rate of the Expense Category, default is null. | [optional] 
**utbms_code** | [**ExpenseCategoryCreateRequestDataUtbmsCode**](ExpenseCategoryCreateRequestDataUtbmsCode.md) |  | [optional] 

## Example

```python
from openapi_client.models.expense_category_update_request_data import ExpenseCategoryUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseCategoryUpdateRequestData from a JSON string
expense_category_update_request_data_instance = ExpenseCategoryUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(ExpenseCategoryUpdateRequestData.to_json())

# convert the object into a dict
expense_category_update_request_data_dict = expense_category_update_request_data_instance.to_dict()
# create an instance of ExpenseCategoryUpdateRequestData from a dict
expense_category_update_request_data_from_dict = ExpenseCategoryUpdateRequestData.from_dict(expense_category_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


