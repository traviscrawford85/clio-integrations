# MatterBudgetBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *MatterBudget* | [optional] 
**etag** | **str** | ETag for the *MatterBudget* | [optional] 
**budget** | **float** | The amount allocated for the matter. | [optional] 
**include_expenses** | **bool** | Whether the budget includes expenses. | [optional] 
**notification_threshold** | **int** | Percentage of the budget when it starts notifying users. The number must be between 0 and 100. | [optional] 
**notify_users** | **bool** | Whether to notify users when the matter reaches the notification threshold. | [optional] 
**created_at** | **datetime** | The time the *MatterBudget* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *MatterBudget* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.matter_budget_base import MatterBudgetBase

# TODO update the JSON string below
json = "{}"
# create an instance of MatterBudgetBase from a JSON string
matter_budget_base_instance = MatterBudgetBase.from_json(json)
# print the JSON string representation of the object
print(MatterBudgetBase.to_json())

# convert the object into a dict
matter_budget_base_dict = matter_budget_base_instance.to_dict()
# create an instance of MatterBudgetBase from a dict
matter_budget_base_from_dict = MatterBudgetBase.from_dict(matter_budget_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


