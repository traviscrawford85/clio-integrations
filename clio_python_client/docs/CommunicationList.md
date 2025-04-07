# CommunicationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Communication]**](Communication.md) | Communication List Response | 

## Example

```python
from openapi_client.models.communication_list import CommunicationList

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationList from a JSON string
communication_list_instance = CommunicationList.from_json(json)
# print the JSON string representation of the object
print(CommunicationList.to_json())

# convert the object into a dict
communication_list_dict = communication_list_instance.to_dict()
# create an instance of CommunicationList from a dict
communication_list_from_dict = CommunicationList.from_dict(communication_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


