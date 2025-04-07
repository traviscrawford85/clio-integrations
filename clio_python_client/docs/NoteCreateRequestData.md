# NoteCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**NoteCreateRequestDataContact**](NoteCreateRequestDataContact.md) |  | 
**var_date** | **date** | Date for the Note. (Expects an ISO-8601 date). | [optional] 
**detail** | **str** | Note body. | [optional] 
**matter** | [**NoteCreateRequestDataMatter**](NoteCreateRequestDataMatter.md) |  | 
**notification_event_subscribers** | [**List[NoteCreateRequestDataNotificationEventSubscribersInner]**](NoteCreateRequestDataNotificationEventSubscribersInner.md) |  | [optional] 
**subject** | **str** | Note subject. | [optional] 
**type** | **str** | Note type. | 

## Example

```python
from openapi_client.models.note_create_request_data import NoteCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of NoteCreateRequestData from a JSON string
note_create_request_data_instance = NoteCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(NoteCreateRequestData.to_json())

# convert the object into a dict
note_create_request_data_dict = note_create_request_data_instance.to_dict()
# create an instance of NoteCreateRequestData from a dict
note_create_request_data_from_dict = NoteCreateRequestData.from_dict(note_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


