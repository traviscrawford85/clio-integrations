# ReportPresetUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | What format the report will be generated in. | [optional] 
**kind** | **str** | What kind of report will be generated. | [optional] 
**name** | **str** | Name of the ReportPreset. | [optional] 
**options** | **str** | What the report generation parameters are. See [Creating a Report Preset](#section/Creating-a-Report-Preset) for a sample request. | [optional] 

## Example

```python
from openapi_client.models.report_preset_update_request_data import ReportPresetUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportPresetUpdateRequestData from a JSON string
report_preset_update_request_data_instance = ReportPresetUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(ReportPresetUpdateRequestData.to_json())

# convert the object into a dict
report_preset_update_request_data_dict = report_preset_update_request_data_instance.to_dict()
# create an instance of ReportPresetUpdateRequestData from a dict
report_preset_update_request_data_from_dict = ReportPresetUpdateRequestData.from_dict(report_preset_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


