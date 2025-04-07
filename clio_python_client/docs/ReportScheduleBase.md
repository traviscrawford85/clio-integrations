# ReportScheduleBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ReportSchedule* | [optional] 
**etag** | **str** | ETag for the *ReportSchedule* | [optional] 
**time_of_day** | **datetime** | What time the Report Schedule is run | [optional] 
**frequency** | **str** | How often the Report Schedule is run | [optional] 
**days_of_week** | **List[int]** | If the frequency is weekly, which days of the week the Report Schedule is run. Values are 0 to 6, representing Sunday to Saturday. | [optional] 
**day_of_month** | **int** | If the frequency is monthly, which day of the month the Report Schedule is run. 32 is used to represent the last day of the month. | [optional] 
**status** | **str** | The status of the Report Schedule | [optional] 
**status_updated_at** | **datetime** | When the status of the Report Schedule was last updated | [optional] 
**next_scheduled_date** | **datetime** | The next time the Report Schedule should run | [optional] 
**time_zone** | **str** | Used in conjunction with &#x60;time_of_day&#x60; to determine when the Report Schedule should run | [optional] 
**report_preset_id** | **int** | The unique identifier of the Report Preset to use when generating the scheduled report | [optional] 
**created_at** | **datetime** | The time the *ReportSchedule* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ReportSchedule* was last updated (as a ISO-8601 timestamp) | [optional] 
**every_no_of_months** | **int** | If the frequency is monthly, how many months between each run of the Report Schedule | [optional] 
**effective_from** | **date** | The date the Report Schedule will become enabled (a ISO-8601 date) | [optional] 

## Example

```python
from openapi_client.models.report_schedule_base import ReportScheduleBase

# TODO update the JSON string below
json = "{}"
# create an instance of ReportScheduleBase from a JSON string
report_schedule_base_instance = ReportScheduleBase.from_json(json)
# print the JSON string representation of the object
print(ReportScheduleBase.to_json())

# convert the object into a dict
report_schedule_base_dict = report_schedule_base_instance.to_dict()
# create an instance of ReportScheduleBase from a dict
report_schedule_base_from_dict = ReportScheduleBase.from_dict(report_schedule_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


