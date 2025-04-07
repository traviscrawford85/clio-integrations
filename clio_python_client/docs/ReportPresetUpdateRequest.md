# ReportPresetUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReportPresetUpdateRequestData**](ReportPresetUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.report_preset_update_request import ReportPresetUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportPresetUpdateRequest from a JSON string
report_preset_update_request_instance = ReportPresetUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReportPresetUpdateRequest.to_json())

# convert the object into a dict
report_preset_update_request_dict = report_preset_update_request_instance.to_dict()
# create an instance of ReportPresetUpdateRequest from a dict
report_preset_update_request_from_dict = ReportPresetUpdateRequest.from_dict(report_preset_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


