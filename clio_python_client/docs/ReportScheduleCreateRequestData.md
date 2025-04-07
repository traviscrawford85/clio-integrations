# ReportScheduleCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_month** | **int** | If the frequency is monthly, which day of the month the Report Schedule should run. 32 is used to represent the last day of the month. | [optional] 
**days_of_week** | **List[int]** | If the frequency is weekly, which days of the week the Report Schedule should run. Values are 0 to 6, representing Sunday to Saturday. | [optional] 
**effective_from** | **date** | Date the Report Schedule should be enabled. (Expects an ISO-8601 date). | [optional] 
**every_no_of_months** | **int** | If the frequency is monthly, how many months between each run of the Report Schedule. | [optional] 
**frequency** | **str** | How often to run the Report Schedule. | 
**report_preset_id** | **int** | What Report Preset the Report Schedule should use to generate a report. | 
**time_of_day** | **datetime** | What time the Report Schedule should run. Although the entire datetime is sent, only the time information is used. | 
**time_zone** | **str** | Used in conjunction with &#x60;time_of_day&#x60; to determine when the Report Schedule should be run. | 

## Example

```python
from openapi_client.models.report_schedule_create_request_data import ReportScheduleCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportScheduleCreateRequestData from a JSON string
report_schedule_create_request_data_instance = ReportScheduleCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(ReportScheduleCreateRequestData.to_json())

# convert the object into a dict
report_schedule_create_request_data_dict = report_schedule_create_request_data_instance.to_dict()
# create an instance of ReportScheduleCreateRequestData from a dict
report_schedule_create_request_data_from_dict = ReportScheduleCreateRequestData.from_dict(report_schedule_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


