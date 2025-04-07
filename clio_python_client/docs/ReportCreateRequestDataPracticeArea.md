# ReportCreateRequestDataPracticeArea


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single PracticeArea associated with the Report. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.report_create_request_data_practice_area import ReportCreateRequestDataPracticeArea

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCreateRequestDataPracticeArea from a JSON string
report_create_request_data_practice_area_instance = ReportCreateRequestDataPracticeArea.from_json(json)
# print the JSON string representation of the object
print(ReportCreateRequestDataPracticeArea.to_json())

# convert the object into a dict
report_create_request_data_practice_area_dict = report_create_request_data_practice_area_instance.to_dict()
# create an instance of ReportCreateRequestDataPracticeArea from a dict
report_create_request_data_practice_area_from_dict = ReportCreateRequestDataPracticeArea.from_dict(report_create_request_data_practice_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


