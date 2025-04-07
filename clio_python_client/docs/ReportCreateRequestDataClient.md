# ReportCreateRequestDataClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Contact associated with the Report. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.report_create_request_data_client import ReportCreateRequestDataClient

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCreateRequestDataClient from a JSON string
report_create_request_data_client_instance = ReportCreateRequestDataClient.from_json(json)
# print the JSON string representation of the object
print(ReportCreateRequestDataClient.to_json())

# convert the object into a dict
report_create_request_data_client_dict = report_create_request_data_client_instance.to_dict()
# create an instance of ReportCreateRequestDataClient from a dict
report_create_request_data_client_from_dict = ReportCreateRequestDataClient.from_dict(report_create_request_data_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


