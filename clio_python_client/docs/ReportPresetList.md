# ReportPresetList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReportPreset]**](ReportPreset.md) | ReportPreset List Response | 

## Example

```python
from openapi_client.models.report_preset_list import ReportPresetList

# TODO update the JSON string below
json = "{}"
# create an instance of ReportPresetList from a JSON string
report_preset_list_instance = ReportPresetList.from_json(json)
# print the JSON string representation of the object
print(ReportPresetList.to_json())

# convert the object into a dict
report_preset_list_dict = report_preset_list_instance.to_dict()
# create an instance of ReportPresetList from a dict
report_preset_list_from_dict = ReportPresetList.from_dict(report_preset_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


