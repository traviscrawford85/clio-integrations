# CommunicationCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommunicationCreateRequestData**](CommunicationCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.communication_create_request import CommunicationCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCreateRequest from a JSON string
communication_create_request_instance = CommunicationCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CommunicationCreateRequest.to_json())

# convert the object into a dict
communication_create_request_dict = communication_create_request_instance.to_dict()
# create an instance of CommunicationCreateRequest from a dict
communication_create_request_from_dict = CommunicationCreateRequest.from_dict(communication_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


