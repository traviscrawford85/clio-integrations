# TaskTemplateCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cascading** | **bool** | Determines if the TaskTemplate has a due date that is derived from another TaskTemplate. (Note that if false, no other cascading information will be checked) | [optional] 
**cascading_offset** | **int** | The amount of time that will differentiate the cascaded TaskTemplate from its parent. | [optional] 
**cascading_offset_polarity** | **str** | Determines whether or not the cascading_offset occurs before or after its parent. | [optional] 
**cascading_offset_type** | **str** | Determines the quantity of the cascading offset (e.g. CalendarDays, CalendarWeeks etc.) | [optional] 
**cascading_source** | [**TaskTemplateCreateRequestDataCascadingSource**](TaskTemplateCreateRequestDataCascadingSource.md) |  | [optional] 
**description** | **str** | Longer description for the TaskTemplate. | [optional] 
**name** | **str** | Short name for the TaskTemplate. | 
**priority** | **str** | Priority of the task. | [optional] [default to 'Normal']
**private** | **bool** | Whether or not this TaskTemplate should be private. | [optional] 
**reminder_templates** | [**List[TaskTemplateCreateRequestDataReminderTemplatesInner]**](TaskTemplateCreateRequestDataReminderTemplatesInner.md) |  | [optional] 
**task_template_list** | [**TaskTemplateCreateRequestDataTaskTemplateList**](TaskTemplateCreateRequestDataTaskTemplateList.md) |  | [optional] 

## Example

```python
from openapi_client.models.task_template_create_request_data import TaskTemplateCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateCreateRequestData from a JSON string
task_template_create_request_data_instance = TaskTemplateCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateCreateRequestData.to_json())

# convert the object into a dict
task_template_create_request_data_dict = task_template_create_request_data_instance.to_dict()
# create an instance of TaskTemplateCreateRequestData from a dict
task_template_create_request_data_from_dict = TaskTemplateCreateRequestData.from_dict(task_template_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


