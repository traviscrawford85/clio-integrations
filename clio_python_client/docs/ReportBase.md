# ReportBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Report* | [optional] 
**etag** | **str** | ETag for the *Report* | [optional] 
**name** | **str** | A specified name for the report | [optional] 
**state** | **str** | The current state of the report | [optional] 
**kind** | **str** | The kind of report to generate | [optional] 
**format** | **str** | The requested format of the report | [optional] 
**progress** | **int** | The integer percentage of how complete the report is. | [optional] 
**created_at** | **datetime** | The time the *Report* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Report* was last updated (as a ISO-8601 timestamp) | [optional] 
**category** | **str** | The category of the report | [optional] 
**source** | **str** | The source of the report | [optional] 

## Example

```python
from openapi_client.models.report_base import ReportBase

# TODO update the JSON string below
json = "{}"
# create an instance of ReportBase from a JSON string
report_base_instance = ReportBase.from_json(json)
# print the JSON string representation of the object
print(ReportBase.to_json())

# convert the object into a dict
report_base_dict = report_base_instance.to_dict()
# create an instance of ReportBase from a dict
report_base_from_dict = ReportBase.from_dict(report_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


