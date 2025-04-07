# LogEntryBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *LogEntry* | [optional] 
**etag** | **str** | ETag for the *LogEntry* | [optional] 
**type** | **str** | The type of the *LogEntry* | [optional] 
**accessed_at** | **datetime** | The time the item was last accessed (as a ISO-8601 timestamp) | [optional] 
**created_at** | **datetime** | The time the *LogEntry* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *LogEntry* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.log_entry_base import LogEntryBase

# TODO update the JSON string below
json = "{}"
# create an instance of LogEntryBase from a JSON string
log_entry_base_instance = LogEntryBase.from_json(json)
# print the JSON string representation of the object
print(LogEntryBase.to_json())

# convert the object into a dict
log_entry_base_dict = log_entry_base_instance.to_dict()
# create an instance of LogEntryBase from a dict
log_entry_base_from_dict = LogEntryBase.from_dict(log_entry_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


