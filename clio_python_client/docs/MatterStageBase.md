# MatterStageBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *MatterStage* | [optional] 
**etag** | **str** | ETag for the *MatterStage* | [optional] 
**practice_area_id** | **str** | Practice Area ID | [optional] 
**name** | **str** | The name of the *MatterStage* | [optional] 
**order** | **int** | The order of the matter stage within a practice area | [optional] 
**created_at** | **datetime** | The time the *MatterStage* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *MatterStage* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.matter_stage_base import MatterStageBase

# TODO update the JSON string below
json = "{}"
# create an instance of MatterStageBase from a JSON string
matter_stage_base_instance = MatterStageBase.from_json(json)
# print the JSON string representation of the object
print(MatterStageBase.to_json())

# convert the object into a dict
matter_stage_base_dict = matter_stage_base_instance.to_dict()
# create an instance of MatterStageBase from a dict
matter_stage_base_from_dict = MatterStageBase.from_dict(matter_stage_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


