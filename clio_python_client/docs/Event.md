# Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Event* | [optional] 
**etag** | **str** | ETag for the *Event* | [optional] 
**message** | **str** | Concise headline message describing the event | [optional] 
**icon** | **str** | Font Awesome icon to display (without the fa- prefix) | [optional] 
**title** | **str** | The title or subject of the event (e.g. Matter Number, Document Title) | [optional] 
**title_url** | **str** | Target URL that will be opened if the user clicks on the event title | [optional] 
**description** | **str** | Description or additional information about the event (e.g. Matter Description) | [optional] 
**description_url** | **str** | Target URL that will be opened if the user clicks on the event description | [optional] 
**primary_detail** | **str** | Optional additional information about the event (e.g. Matter Client, Document Author) | [optional] 
**primary_detail_url** | **str** | Target URL that will be opened if the user clicks on the primary detail | [optional] 
**secondary_detail** | **str** | Optional additional information about the event (e.g. Matter Status, Document Size) | [optional] 
**secondary_detail_url** | **str** | Target URL that will be opened if the user clicks on the secondary detail | [optional] 
**occurred_at** | **datetime** | When the event occurred | [optional] 
**mobile_icon** | **str** | Icon to be displayed in the mobile app | [optional] 
**subject_type** | **str** | The type of subject that triggered the notification (e.g. Matter, Document) | [optional] 
**subject_id** | **int** | Id of the subject that triggered the notification | [optional] 

## Example

```python
from openapi_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


