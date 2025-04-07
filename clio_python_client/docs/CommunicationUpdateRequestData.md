# CommunicationUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The body value. | [optional] 
**var_date** | **str** | The date for the Communication. (Expects an ISO-8601 date.) | [optional] 
**external_properties** | [**List[CommunicationUpdateRequestDataExternalPropertiesInner]**](CommunicationUpdateRequestDataExternalPropertiesInner.md) |  | [optional] 
**matter** | [**CommunicationCreateRequestDataMatter**](CommunicationCreateRequestDataMatter.md) |  | [optional] 
**notification_event_subscribers** | [**List[CommunicationUpdateRequestDataNotificationEventSubscribersInner]**](CommunicationUpdateRequestDataNotificationEventSubscribersInner.md) |  | [optional] 
**received_at** | **str** | The date-time for the Communication. (Expects an ISO-8601 date-time.) | [optional] 
**receivers** | [**List[CommunicationCreateRequestDataReceiversInner]**](CommunicationCreateRequestDataReceiversInner.md) |  | [optional] 
**senders** | [**List[CommunicationCreateRequestDataSendersInner]**](CommunicationCreateRequestDataSendersInner.md) |  | [optional] 
**subject** | **str** | The subject value. | [optional] 
**type** | **str** | Type of the Communication. | [optional] 

## Example

```python
from openapi_client.models.communication_update_request_data import CommunicationUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationUpdateRequestData from a JSON string
communication_update_request_data_instance = CommunicationUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(CommunicationUpdateRequestData.to_json())

# convert the object into a dict
communication_update_request_data_dict = communication_update_request_data_instance.to_dict()
# create an instance of CommunicationUpdateRequestData from a dict
communication_update_request_data_from_dict = CommunicationUpdateRequestData.from_dict(communication_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


