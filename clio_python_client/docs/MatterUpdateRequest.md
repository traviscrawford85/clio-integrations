# MatterUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MatterUpdateRequestData**](MatterUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.matter_update_request import MatterUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatterUpdateRequest from a JSON string
matter_update_request_instance = MatterUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MatterUpdateRequest.to_json())

# convert the object into a dict
matter_update_request_dict = matter_update_request_instance.to_dict()
# create an instance of MatterUpdateRequest from a dict
matter_update_request_from_dict = MatterUpdateRequest.from_dict(matter_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


