# ReportPresetCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReportPresetCreateRequestData**](ReportPresetCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.report_preset_create_request import ReportPresetCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportPresetCreateRequest from a JSON string
report_preset_create_request_instance = ReportPresetCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ReportPresetCreateRequest.to_json())

# convert the object into a dict
report_preset_create_request_dict = report_preset_create_request_instance.to_dict()
# create an instance of ReportPresetCreateRequest from a dict
report_preset_create_request_from_dict = ReportPresetCreateRequest.from_dict(report_preset_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


