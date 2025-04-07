# ExpenseCategoryCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **object** | Currency of the Expense Category. | [optional] 
**entry_type** | **str** | Defaults to unassociated. | [optional] 
**groups** | [**List[ExpenseCategoryCreateRequestDataGroupsInner]**](ExpenseCategoryCreateRequestDataGroupsInner.md) |  | [optional] 
**name** | **str** | Name of the Expense Category. | 
**rate** | **float** | Rate of the Expense Category, default is null. | [optional] 
**utbms_code** | [**ExpenseCategoryCreateRequestDataUtbmsCode**](ExpenseCategoryCreateRequestDataUtbmsCode.md) |  | [optional] 

## Example

```python
from openapi_client.models.expense_category_create_request_data import ExpenseCategoryCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseCategoryCreateRequestData from a JSON string
expense_category_create_request_data_instance = ExpenseCategoryCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(ExpenseCategoryCreateRequestData.to_json())

# convert the object into a dict
expense_category_create_request_data_dict = expense_category_create_request_data_instance.to_dict()
# create an instance of ExpenseCategoryCreateRequestData from a dict
expense_category_create_request_data_from_dict = ExpenseCategoryCreateRequestData.from_dict(expense_category_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


