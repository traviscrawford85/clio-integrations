# CommunicationBase


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

## Example

```python
from openapi_client.models.communication_base import CommunicationBase

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationBase from a JSON string
communication_base_instance = CommunicationBase.from_json(json)
# print the JSON string representation of the object
print(CommunicationBase.to_json())

# convert the object into a dict
communication_base_dict = communication_base_instance.to_dict()
# create an instance of CommunicationBase from a dict
communication_base_from_dict = CommunicationBase.from_dict(communication_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


