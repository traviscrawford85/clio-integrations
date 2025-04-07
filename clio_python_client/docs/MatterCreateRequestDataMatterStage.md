# MatterCreateRequestDataMatterStage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single MatterStage associated with the Matter. Use the keyword &#x60;null&#x60; to specify no association. | [optional] 

## Example

```python
from openapi_client.models.matter_create_request_data_matter_stage import MatterCreateRequestDataMatterStage

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataMatterStage from a JSON string
matter_create_request_data_matter_stage_instance = MatterCreateRequestDataMatterStage.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataMatterStage.to_json())

# convert the object into a dict
matter_create_request_data_matter_stage_dict = matter_create_request_data_matter_stage_instance.to_dict()
# create an instance of MatterCreateRequestDataMatterStage from a dict
matter_create_request_data_matter_stage_from_dict = MatterCreateRequestDataMatterStage.from_dict(matter_create_request_data_matter_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


