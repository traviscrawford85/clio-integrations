# ReportList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Report]**](Report.md) | Report List Response | 

## Example

```python
from openapi_client.models.report_list import ReportList

# TODO update the JSON string below
json = "{}"
# create an instance of ReportList from a JSON string
report_list_instance = ReportList.from_json(json)
# print the JSON string representation of the object
print(ReportList.to_json())

# convert the object into a dict
report_list_dict = report_list_instance.to_dict()
# create an instance of ReportList from a dict
report_list_from_dict = ReportList.from_dict(report_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


