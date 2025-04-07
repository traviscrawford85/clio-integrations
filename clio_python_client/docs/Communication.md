# Communication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Communication* | [optional] 
**etag** | **str** | ETag for the *Communication* | [optional] 
**subject** | **str** | The subject line of the *Communication* | [optional] 
**body** | **str** | The main content of the *Communication* | [optional] 
**type** | **str** | The type of the *Communication* | [optional] 
**var_date** | **date** | The date of the *Communication* (as a ISO-8601 datestamp) | [optional] 
**time_entries_count** | **int** | The number of time_entries associated with the *Communication* | [optional] 
**created_at** | **datetime** | The time the *Communication* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Communication* was last updated (as a ISO-8601 timestamp) | [optional] 
**received_at** | **datetime** | The date-time of the *Communication* (in ISO-8601 format) | [optional] 
**user** | [**UserBase**](UserBase.md) |  | [optional] 
**matter** | [**MatterBase**](MatterBase.md) |  | [optional] 
**communication_eml_file** | [**CommunicationEmlFileBase**](CommunicationEmlFileBase.md) |  | [optional] 
**senders** | [**List[Participant]**](Participant.md) | Participant | [optional] 
**receivers** | [**List[Participant]**](Participant.md) | Participant | [optional] 
**external_properties** | [**List[ExternalPropertyBase]**](ExternalPropertyBase.md) | ExternalProperty | [optional] 
**time_entries** | [**List[ActivityBase]**](ActivityBase.md) | Activity | [optional] 
**documents** | [**List[DocumentBase]**](DocumentBase.md) | Document | [optional] 
**notification_event_subscribers** | [**List[NotificationEventSubscriberBase]**](NotificationEventSubscriberBase.md) | NotificationEventSubscriber | [optional] 

## Example

```python
from openapi_client.models.communication import Communication

# TODO update the JSON string below
json = "{}"
# create an instance of Communication from a JSON string
communication_instance = Communication.from_json(json)
# print the JSON string representation of the object
print(Communication.to_json())

# convert the object into a dict
communication_dict = communication_instance.to_dict()
# create an instance of Communication from a dict
communication_from_dict = Communication.from_dict(communication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


