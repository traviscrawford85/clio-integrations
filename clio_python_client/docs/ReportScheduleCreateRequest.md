# ReportScheduleCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReportScheduleCreateRequestData**](ReportScheduleCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.report_schedule_create_request import ReportScheduleCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportScheduleCreateRequest from a JSON string
report_schedule_create_request_instance = ReportScheduleCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ReportScheduleCreateRequest.to_json())

# convert the object into a dict
report_schedule_create_request_dict = report_schedule_create_request_instance.to_dict()
# create an instance of ReportScheduleCreateRequest from a dict
report_schedule_create_request_from_dict = ReportScheduleCreateRequest.from_dict(report_schedule_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


