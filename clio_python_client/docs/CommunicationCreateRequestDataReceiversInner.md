# CommunicationCreateRequestDataReceiversInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** | Whether or not the receivers should be deleted. | [optional] 
**id** | **int** | Unique ids for the receivers of this Communication. | [optional] 
**type** | **str** | Types of the receivers of this Communication. | [optional] 

## Example

```python
from openapi_client.models.communication_create_request_data_receivers_inner import CommunicationCreateRequestDataReceiversInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCreateRequestDataReceiversInner from a JSON string
communication_create_request_data_receivers_inner_instance = CommunicationCreateRequestDataReceiversInner.from_json(json)
# print the JSON string representation of the object
print(CommunicationCreateRequestDataReceiversInner.to_json())

# convert the object into a dict
communication_create_request_data_receivers_inner_dict = communication_create_request_data_receivers_inner_instance.to_dict()
# create an instance of CommunicationCreateRequestDataReceiversInner from a dict
communication_create_request_data_receivers_inner_from_dict = CommunicationCreateRequestDataReceiversInner.from_dict(communication_create_request_data_receivers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


