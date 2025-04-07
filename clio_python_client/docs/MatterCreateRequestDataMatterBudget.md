# MatterCreateRequestDataMatterBudget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destroy** | **bool** | Determines whether the matter budget associated with the matter should be destroyed. Only users with matter budget destroy capabilities can destroy matter budgets. | [optional] 
**budget** | **float** | The amount allocated for the matter. | [optional] 
**include_expenses** | **bool** | Determines whether the budget includes expenses in the calculation. | [optional] 
**notification_threshold** | **int** | Percentage of the budget when it starts notifying users. | [optional] 
**notify_users** | **bool** | Determine whether to notify users when the matter reaches the notification threshold. | [optional] [default to False]

## Example

```python
from openapi_client.models.matter_create_request_data_matter_budget import MatterCreateRequestDataMatterBudget

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataMatterBudget from a JSON string
matter_create_request_data_matter_budget_instance = MatterCreateRequestDataMatterBudget.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataMatterBudget.to_json())

# convert the object into a dict
matter_create_request_data_matter_budget_dict = matter_create_request_data_matter_budget_instance.to_dict()
# create an instance of MatterCreateRequestDataMatterBudget from a dict
matter_create_request_data_matter_budget_from_dict = MatterCreateRequestDataMatterBudget.from_dict(matter_create_request_data_matter_budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


