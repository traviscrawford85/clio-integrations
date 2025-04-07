# ParticipantBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Participant* | [optional] 
**etag** | **str** | ETag for the *Participant* | [optional] 
**created_at** | **datetime** | The time the *Participant* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Participant* was last updated (as a ISO-8601 timestamp) | [optional] 
**type** | **str** | The type of the Participant. Person and Company are subtypes of Contact | [optional] 
**identifier** | **str** | A string to identify the *Participant* | [optional] 
**secondary_identifier** | **str** | A secondary string to identify the *Participant* | [optional] 
**enabled** | **bool** | The enabled state of the *Participant* record. Always &#39;null&#39; if *Participant* type is Contact | [optional] 
**name** | **str** | The name of the *Participant* record | [optional] 
**initials** | **str** | A  string with the participant initials | [optional] 
**job_title_name** | **str** | the job title name of the participant if they are a firm user and have one | [optional] 

## Example

```python
from openapi_client.models.participant_base import ParticipantBase

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantBase from a JSON string
participant_base_instance = ParticipantBase.from_json(json)
# print the JSON string representation of the object
print(ParticipantBase.to_json())

# convert the object into a dict
participant_base_dict = participant_base_instance.to_dict()
# create an instance of ParticipantBase from a dict
participant_base_from_dict = ParticipantBase.from_dict(participant_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


