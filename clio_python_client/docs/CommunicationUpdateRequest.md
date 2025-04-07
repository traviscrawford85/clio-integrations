# CommunicationUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommunicationUpdateRequestData**](CommunicationUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.communication_update_request import CommunicationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationUpdateRequest from a JSON string
communication_update_request_instance = CommunicationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CommunicationUpdateRequest.to_json())

# convert the object into a dict
communication_update_request_dict = communication_update_request_instance.to_dict()
# create an instance of CommunicationUpdateRequest from a dict
communication_update_request_from_dict = CommunicationUpdateRequest.from_dict(communication_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


