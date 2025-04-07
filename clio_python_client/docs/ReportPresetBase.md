# ReportPresetBase


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

## Example

```python
from openapi_client.models.report_preset_base import ReportPresetBase

# TODO update the JSON string below
json = "{}"
# create an instance of ReportPresetBase from a JSON string
report_preset_base_instance = ReportPresetBase.from_json(json)
# print the JSON string representation of the object
print(ReportPresetBase.to_json())

# convert the object into a dict
report_preset_base_dict = report_preset_base_instance.to_dict()
# create an instance of ReportPresetBase from a dict
report_preset_base_from_dict = ReportPresetBase.from_dict(report_preset_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


