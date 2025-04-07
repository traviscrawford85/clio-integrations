# MatterDocketCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MatterDocketCreateRequestData**](MatterDocketCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.matter_docket_create_request import MatterDocketCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatterDocketCreateRequest from a JSON string
matter_docket_create_request_instance = MatterDocketCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MatterDocketCreateRequest.to_json())

# convert the object into a dict
matter_docket_create_request_dict = matter_docket_create_request_instance.to_dict()
# create an instance of MatterDocketCreateRequest from a dict
matter_docket_create_request_from_dict = MatterDocketCreateRequest.from_dict(matter_docket_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


