# ReportCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReportCreateRequestData**](ReportCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.report_create_request import ReportCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCreateRequest from a JSON string
report_create_request_instance = ReportCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ReportCreateRequest.to_json())

# convert the object into a dict
report_create_request_dict = report_create_request_instance.to_dict()
# create an instance of ReportCreateRequest from a dict
report_create_request_from_dict = ReportCreateRequest.from_dict(report_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


