# CommunicationCreateRequestDataSendersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** | Whether or not the senders should be deleted. | [optional] 
**id** | **int** | Unique ids for the senders of this Communication. | [optional] 
**type** | **str** | Types of the senders of this Communication. | [optional] 

## Example

```python
from openapi_client.models.communication_create_request_data_senders_inner import CommunicationCreateRequestDataSendersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCreateRequestDataSendersInner from a JSON string
communication_create_request_data_senders_inner_instance = CommunicationCreateRequestDataSendersInner.from_json(json)
# print the JSON string representation of the object
print(CommunicationCreateRequestDataSendersInner.to_json())

# convert the object into a dict
communication_create_request_data_senders_inner_dict = communication_create_request_data_senders_inner_instance.to_dict()
# create an instance of CommunicationCreateRequestDataSendersInner from a dict
communication_create_request_data_senders_inner_from_dict = CommunicationCreateRequestDataSendersInner.from_dict(communication_create_request_data_senders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


