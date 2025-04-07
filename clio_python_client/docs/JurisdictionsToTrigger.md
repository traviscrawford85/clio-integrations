# JurisdictionsToTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *JurisdictionsToTrigger* | [optional] 
**etag** | **str** | ETag for the *JurisdictionsToTrigger* | [optional] 
**system_id** | **int** | Server id | [optional] 
**description** | **str** | A detailed description of the *JurisdictionsToTrigger* | [optional] 
**do_not_recalculate** | **bool** | Whether the associated dates should not be recalculated | [optional] 
**is_served** | **bool** | Whether the user must select a Date Offset (Service Type) | [optional] 
**is_requirements_required** | **bool** | Whether the trigger has requirements | [optional] 
**created_at** | **datetime** | The time the *JurisdictionsToTrigger* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *JurisdictionsToTrigger* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.jurisdictions_to_trigger import JurisdictionsToTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of JurisdictionsToTrigger from a JSON string
jurisdictions_to_trigger_instance = JurisdictionsToTrigger.from_json(json)
# print the JSON string representation of the object
print(JurisdictionsToTrigger.to_json())

# convert the object into a dict
jurisdictions_to_trigger_dict = jurisdictions_to_trigger_instance.to_dict()
# create an instance of JurisdictionsToTrigger from a dict
jurisdictions_to_trigger_from_dict = JurisdictionsToTrigger.from_dict(jurisdictions_to_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


