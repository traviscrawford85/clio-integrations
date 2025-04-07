# ReportScheduleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReportSchedule]**](ReportSchedule.md) | ReportSchedule List Response | 

## Example

```python
from openapi_client.models.report_schedule_list import ReportScheduleList

# TODO update the JSON string below
json = "{}"
# create an instance of ReportScheduleList from a JSON string
report_schedule_list_instance = ReportScheduleList.from_json(json)
# print the JSON string representation of the object
print(ReportScheduleList.to_json())

# convert the object into a dict
report_schedule_list_dict = report_schedule_list_instance.to_dict()
# create an instance of ReportScheduleList from a dict
report_schedule_list_from_dict = ReportScheduleList.from_dict(report_schedule_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


