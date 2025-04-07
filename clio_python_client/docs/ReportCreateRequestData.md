# ReportCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | [**ReportCreateRequestDataClient**](ReportCreateRequestDataClient.md) |  | [optional] 
**end_date** | **date** | Filters Report data by date. (Expects an ISO-8601 date). | [optional] 
**format** | **str** | What format the Report will be generated in. | 
**kind** | **str** | What kind of Report will be generated. | 
**matter** | [**ReportCreateRequestDataMatter**](ReportCreateRequestDataMatter.md) |  | [optional] 
**originating_attorney** | [**ReportCreateRequestDataOriginatingAttorney**](ReportCreateRequestDataOriginatingAttorney.md) |  | [optional] 
**practice_area** | [**ReportCreateRequestDataPracticeArea**](ReportCreateRequestDataPracticeArea.md) |  | [optional] 
**responsible_attorney** | [**ReportCreateRequestDataOriginatingAttorney**](ReportCreateRequestDataOriginatingAttorney.md) |  | [optional] 
**start_date** | **date** | Filters Report data by date. (Expects an ISO-8601 date). | [optional] 
**user** | [**ReportCreateRequestDataOriginatingAttorney**](ReportCreateRequestDataOriginatingAttorney.md) |  | [optional] 
**year** | **str** | Filters Report data by year. Sets start_date and end_date. (Expects a year). | [optional] 

## Example

```python
from openapi_client.models.report_create_request_data import ReportCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCreateRequestData from a JSON string
report_create_request_data_instance = ReportCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(ReportCreateRequestData.to_json())

# convert the object into a dict
report_create_request_data_dict = report_create_request_data_instance.to_dict()
# create an instance of ReportCreateRequestData from a dict
report_create_request_data_from_dict = ReportCreateRequestData.from_dict(report_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


