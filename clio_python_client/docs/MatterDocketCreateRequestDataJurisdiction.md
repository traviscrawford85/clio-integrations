# MatterDocketCreateRequestDataJurisdiction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Jurisdiction associated with the MatterDocket. The keyword &#x60;null&#x60; is not valid for this field. | 

## Example

```python
from openapi_client.models.matter_docket_create_request_data_jurisdiction import MatterDocketCreateRequestDataJurisdiction

# TODO update the JSON string below
json = "{}"
# create an instance of MatterDocketCreateRequestDataJurisdiction from a JSON string
matter_docket_create_request_data_jurisdiction_instance = MatterDocketCreateRequestDataJurisdiction.from_json(json)
# print the JSON string representation of the object
print(MatterDocketCreateRequestDataJurisdiction.to_json())

# convert the object into a dict
matter_docket_create_request_data_jurisdiction_dict = matter_docket_create_request_data_jurisdiction_instance.to_dict()
# create an instance of MatterDocketCreateRequestDataJurisdiction from a dict
matter_docket_create_request_data_jurisdiction_from_dict = MatterDocketCreateRequestDataJurisdiction.from_dict(matter_docket_create_request_data_jurisdiction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


