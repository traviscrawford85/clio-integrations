# CommunicationCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The body value. | 
**var_date** | **str** | The date for the Communication. (Expects an ISO-8601 date.) | [optional] 
**external_properties** | [**List[CommunicationCreateRequestDataExternalPropertiesInner]**](CommunicationCreateRequestDataExternalPropertiesInner.md) |  | [optional] 
**matter** | [**CommunicationCreateRequestDataMatter**](CommunicationCreateRequestDataMatter.md) |  | [optional] 
**notification_event_subscribers** | [**List[CommunicationCreateRequestDataNotificationEventSubscribersInner]**](CommunicationCreateRequestDataNotificationEventSubscribersInner.md) |  | [optional] 
**received_at** | **str** | The date-time for the Communication. (Expects an ISO-8601 date-time.) | [optional] 
**receivers** | [**List[CommunicationCreateRequestDataReceiversInner]**](CommunicationCreateRequestDataReceiversInner.md) |  | [optional] 
**senders** | [**List[CommunicationCreateRequestDataSendersInner]**](CommunicationCreateRequestDataSendersInner.md) |  | [optional] 
**subject** | **str** | The subject value. | 
**type** | **str** | Type of the Communication. | 

## Example

```python
from openapi_client.models.communication_create_request_data import CommunicationCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCreateRequestData from a JSON string
communication_create_request_data_instance = CommunicationCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(CommunicationCreateRequestData.to_json())

# convert the object into a dict
communication_create_request_data_dict = communication_create_request_data_instance.to_dict()
# create an instance of CommunicationCreateRequestData from a dict
communication_create_request_data_from_dict = CommunicationCreateRequestData.from_dict(communication_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


