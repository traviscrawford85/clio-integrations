# MatterDocketCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jurisdiction** | [**MatterDocketCreateRequestDataJurisdiction**](MatterDocketCreateRequestDataJurisdiction.md) |  | 
**name** | **str** | Name of the MatterDocket. | 
**start_date** | **date** | Start date of the MatterDocket. (Expects an ISO-8601 date). | 
**start_time** | **datetime** | Start time of the MatterDocket. Required for some triggers.  (Expects an ISO-8601 timestamp). | [optional] 
**trigger** | [**MatterDocketCreateRequestDataTrigger**](MatterDocketCreateRequestDataTrigger.md) |  | 

## Example

```python
from openapi_client.models.matter_docket_create_request_data import MatterDocketCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of MatterDocketCreateRequestData from a JSON string
matter_docket_create_request_data_instance = MatterDocketCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(MatterDocketCreateRequestData.to_json())

# convert the object into a dict
matter_docket_create_request_data_dict = matter_docket_create_request_data_instance.to_dict()
# create an instance of MatterDocketCreateRequestData from a dict
matter_docket_create_request_data_from_dict = MatterDocketCreateRequestData.from_dict(matter_docket_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


