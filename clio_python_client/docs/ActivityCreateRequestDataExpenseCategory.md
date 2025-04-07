# ActivityCreateRequestDataExpenseCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single ExpenseCategory associated with an Activity. Use the keyword &#x60;null&#x60; to specify no association.  | [optional] 

## Example

```python
from openapi_client.models.activity_create_request_data_expense_category import ActivityCreateRequestDataExpenseCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCreateRequestDataExpenseCategory from a JSON string
activity_create_request_data_expense_category_instance = ActivityCreateRequestDataExpenseCategory.from_json(json)
# print the JSON string representation of the object
print(ActivityCreateRequestDataExpenseCategory.to_json())

# convert the object into a dict
activity_create_request_data_expense_category_dict = activity_create_request_data_expense_category_instance.to_dict()
# create an instance of ActivityCreateRequestDataExpenseCategory from a dict
activity_create_request_data_expense_category_from_dict = ActivityCreateRequestDataExpenseCategory.from_dict(activity_create_request_data_expense_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


