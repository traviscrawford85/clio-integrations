# ReportPreset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ReportPreset* | [optional] 
**etag** | **str** | ETag for the *ReportPreset* | [optional] 
**name** | **str** | A specified name for the report preset | [optional] 
**kind** | **str** | The kind of report the preset generates | [optional] 
**format** | **str** | The format of the report the preset generates | [optional] 
**last_generated_at** | **datetime** | The time of the last generated report from this preset (as a ISO-8601 timestamp) | [optional] 
**created_at** | **datetime** | The time the *ReportPreset* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ReportPreset* was last updated (as a ISO-8601 timestamp) | [optional] 
**category** | **str** | The category of the report the preset generates | [optional] 
**options** | **str** | The report options parameters | [optional] 
**report_schedule** | [**ReportScheduleBase**](ReportScheduleBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.report_preset import ReportPreset

# TODO update the JSON string below
json = "{}"
# create an instance of ReportPreset from a JSON string
report_preset_instance = ReportPreset.from_json(json)
# print the JSON string representation of the object
print(ReportPreset.to_json())

# convert the object into a dict
report_preset_dict = report_preset_instance.to_dict()
# create an instance of ReportPreset from a dict
report_preset_from_dict = ReportPreset.from_dict(report_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


