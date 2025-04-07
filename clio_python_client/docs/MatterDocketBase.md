# MatterDocketBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *MatterDocket* | [optional] 
**etag** | **str** | ETag for the *MatterDocket* | [optional] 
**name** | **str** | The name of the *MatterDocket* | [optional] 
**start_date** | **date** | The date the *MatterDocket* will start (as a ISO-8601 date) | [optional] 
**start_time** | **datetime** | The time the *MatterDocket* will start, required for specific triggers (as a ISO-8601 timestamp) | [optional] 
**status** | **str** | The status of the *MatterDocket* creation | [optional] 
**created_at** | **datetime** | The time the *MatterDocket* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *MatterDocket* was last updated (as a ISO-8601 timestamp) | [optional] 
**deleted_at** | **datetime** | The time the *MatterDocket* was deleted (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.matter_docket_base import MatterDocketBase

# TODO update the JSON string below
json = "{}"
# create an instance of MatterDocketBase from a JSON string
matter_docket_base_instance = MatterDocketBase.from_json(json)
# print the JSON string representation of the object
print(MatterDocketBase.to_json())

# convert the object into a dict
matter_docket_base_dict = matter_docket_base_instance.to_dict()
# create an instance of MatterDocketBase from a dict
matter_docket_base_from_dict = MatterDocketBase.from_dict(matter_docket_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


