# Participant


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
**avatar** | [**AvatarBase**](AvatarBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.participant import Participant

# TODO update the JSON string below
json = "{}"
# create an instance of Participant from a JSON string
participant_instance = Participant.from_json(json)
# print the JSON string representation of the object
print(Participant.to_json())

# convert the object into a dict
participant_dict = participant_instance.to_dict()
# create an instance of Participant from a dict
participant_from_dict = Participant.from_dict(participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


