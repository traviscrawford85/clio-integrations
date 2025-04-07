# MatterCreateRequestDataStatuteOfLimitations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The task status of Statue of Limitations. Users without advanced tasks are allowed to select &#x60;Complete&#39; or &#x60;Pending&#x60; only. | [optional] 
**due_at** | **date** | The due date of Statute of Limitations. (Expects an ISO-8601 date). | [optional] 
**reminders** | [**List[MatterCreateRequestDataStatuteOfLimitationsRemindersInner]**](MatterCreateRequestDataStatuteOfLimitationsRemindersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.matter_create_request_data_statute_of_limitations import MatterCreateRequestDataStatuteOfLimitations

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataStatuteOfLimitations from a JSON string
matter_create_request_data_statute_of_limitations_instance = MatterCreateRequestDataStatuteOfLimitations.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataStatuteOfLimitations.to_json())

# convert the object into a dict
matter_create_request_data_statute_of_limitations_dict = matter_create_request_data_statute_of_limitations_instance.to_dict()
# create an instance of MatterCreateRequestDataStatuteOfLimitations from a dict
matter_create_request_data_statute_of_limitations_from_dict = MatterCreateRequestDataStatuteOfLimitations.from_dict(matter_create_request_data_statute_of_limitations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


