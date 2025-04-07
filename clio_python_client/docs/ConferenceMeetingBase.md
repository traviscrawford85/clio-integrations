# ConferenceMeetingBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference_id** | **int** | Third-party provider unique meeting ID | [optional] 
**conference_password** | **str** | Third-party provider meeting password | [optional] 
**created_at** | **datetime** | The time the *ConferenceMeeting* was created (as a ISO-8601 timestamp) | [optional] 
**etag** | **str** | ETag for the *ConferenceMeeting* | [optional] 
**id** | **int** | Unique identifier for the *ConferenceMeeting* | [optional] 
**join_url** | **str** | URL for participants to join the video conference | [optional] 
**type** | **str** | The type of video conference | [optional] 
**source_id** | **int** | The external ID of the video conference meeting | [optional] 
**updated_at** | **datetime** | The time the *ConferenceMeeting* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.conference_meeting_base import ConferenceMeetingBase

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceMeetingBase from a JSON string
conference_meeting_base_instance = ConferenceMeetingBase.from_json(json)
# print the JSON string representation of the object
print(ConferenceMeetingBase.to_json())

# convert the object into a dict
conference_meeting_base_dict = conference_meeting_base_instance.to_dict()
# create an instance of ConferenceMeetingBase from a dict
conference_meeting_base_from_dict = ConferenceMeetingBase.from_dict(conference_meeting_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


