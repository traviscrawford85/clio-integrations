# MatterStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MatterStage]**](MatterStage.md) | MatterStage List Response | 

## Example

```python
from openapi_client.models.matter_stage_list import MatterStageList

# TODO update the JSON string below
json = "{}"
# create an instance of MatterStageList from a JSON string
matter_stage_list_instance = MatterStageList.from_json(json)
# print the JSON string representation of the object
print(MatterStageList.to_json())

# convert the object into a dict
matter_stage_list_dict = matter_stage_list_instance.to_dict()
# create an instance of MatterStageList from a dict
matter_stage_list_from_dict = MatterStageList.from_dict(matter_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


