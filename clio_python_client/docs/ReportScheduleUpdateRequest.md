# ReportScheduleUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReportScheduleUpdateRequestData**](ReportScheduleUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.report_schedule_update_request import ReportScheduleUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportScheduleUpdateRequest from a JSON string
report_schedule_update_request_instance = ReportScheduleUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReportScheduleUpdateRequest.to_json())

# convert the object into a dict
report_schedule_update_request_dict = report_schedule_update_request_instance.to_dict()
# create an instance of ReportScheduleUpdateRequest from a dict
report_schedule_update_request_from_dict = ReportScheduleUpdateRequest.from_dict(report_schedule_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


