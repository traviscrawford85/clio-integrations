# ReportCreateRequestDataOriginatingAttorney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single User associated with the Report. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.report_create_request_data_originating_attorney import ReportCreateRequestDataOriginatingAttorney

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCreateRequestDataOriginatingAttorney from a JSON string
report_create_request_data_originating_attorney_instance = ReportCreateRequestDataOriginatingAttorney.from_json(json)
# print the JSON string representation of the object
print(ReportCreateRequestDataOriginatingAttorney.to_json())

# convert the object into a dict
report_create_request_data_originating_attorney_dict = report_create_request_data_originating_attorney_instance.to_dict()
# create an instance of ReportCreateRequestDataOriginatingAttorney from a dict
report_create_request_data_originating_attorney_from_dict = ReportCreateRequestDataOriginatingAttorney.from_dict(report_create_request_data_originating_attorney_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


