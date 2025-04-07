# Note


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Note* | [optional] 
**etag** | **str** | ETag for the *Note* | [optional] 
**type** | **str** | The type of the *Note* | [optional] 
**subject** | **str** | The subject of the *Note* | [optional] 
**detail** | **str** | The body of the *Note* | [optional] 
**var_date** | **date** | The date the *Note* is for (as a ISO-8601 date) | [optional] 
**created_at** | **datetime** | The time the *Note* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Note* was last updated (as a ISO-8601 timestamp) | [optional] 
**time_entries_count** | **int** | The number of time_entries associated with the *Note* | [optional] 
**matter** | [**MatterBase**](MatterBase.md) |  | [optional] 
**contact** | [**ContactBase**](ContactBase.md) |  | [optional] 
**author** | [**UserBase**](UserBase.md) |  | [optional] 
**time_entries** | [**List[ActivityBase]**](ActivityBase.md) | Activity | [optional] 
**notification_event_subscribers** | [**List[NotificationEventSubscriberBase]**](NotificationEventSubscriberBase.md) | NotificationEventSubscriber | [optional] 

## Example

```python
from openapi_client.models.note import Note

# TODO update the JSON string below
json = "{}"
# create an instance of Note from a JSON string
note_instance = Note.from_json(json)
# print the JSON string representation of the object
print(Note.to_json())

# convert the object into a dict
note_dict = note_instance.to_dict()
# create an instance of Note from a dict
note_from_dict = Note.from_dict(note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


