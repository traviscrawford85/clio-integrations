# MatterUpdateRequestDataTaskTemplateListInstancesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_template_list** | [**MatterUpdateRequestDataTaskTemplateListInstancesInnerTaskTemplateList**](MatterUpdateRequestDataTaskTemplateListInstancesInnerTaskTemplateList.md) |  | [optional] 
**assignee_id** | **int** | The id of the user to assign the task template list to. | [optional] 
**notify_assignees** | **bool** | Whether or not task list assignees should be notified when the task list is assigned to a matter. | [optional] 
**due_at** | **date** | Due date of the tasks. (Expects an ISO-8601 date). | [optional] 

## Example

```python
from openapi_client.models.matter_update_request_data_task_template_list_instances_inner import MatterUpdateRequestDataTaskTemplateListInstancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatterUpdateRequestDataTaskTemplateListInstancesInner from a JSON string
matter_update_request_data_task_template_list_instances_inner_instance = MatterUpdateRequestDataTaskTemplateListInstancesInner.from_json(json)
# print the JSON string representation of the object
print(MatterUpdateRequestDataTaskTemplateListInstancesInner.to_json())

# convert the object into a dict
matter_update_request_data_task_template_list_instances_inner_dict = matter_update_request_data_task_template_list_instances_inner_instance.to_dict()
# create an instance of MatterUpdateRequestDataTaskTemplateListInstancesInner from a dict
matter_update_request_data_task_template_list_instances_inner_from_dict = MatterUpdateRequestDataTaskTemplateListInstancesInner.from_dict(matter_update_request_data_task_template_list_instances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


