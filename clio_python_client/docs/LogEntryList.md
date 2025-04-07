# LogEntryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LogEntry]**](LogEntry.md) | LogEntry List Response | 

## Example

```python
from openapi_client.models.log_entry_list import LogEntryList

# TODO update the JSON string below
json = "{}"
# create an instance of LogEntryList from a JSON string
log_entry_list_instance = LogEntryList.from_json(json)
# print the JSON string representation of the object
print(LogEntryList.to_json())

# convert the object into a dict
log_entry_list_dict = log_entry_list_instance.to_dict()
# create an instance of LogEntryList from a dict
log_entry_list_from_dict = LogEntryList.from_dict(log_entry_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


