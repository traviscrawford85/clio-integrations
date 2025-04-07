# MatterCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MatterCreateRequestData**](MatterCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.matter_create_request import MatterCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequest from a JSON string
matter_create_request_instance = MatterCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequest.to_json())

# convert the object into a dict
matter_create_request_dict = matter_create_request_instance.to_dict()
# create an instance of MatterCreateRequest from a dict
matter_create_request_from_dict = MatterCreateRequest.from_dict(matter_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


