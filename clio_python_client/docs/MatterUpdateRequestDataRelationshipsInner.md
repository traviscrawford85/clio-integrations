# MatterUpdateRequestDataRelationshipsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Describe the relationship between a Contact and a Matter. | [optional] 
**contact** | [**MatterUpdateRequestDataRelationshipsInnerContact**](MatterUpdateRequestDataRelationshipsInnerContact.md) |  | [optional] 
**id** | **int** | The unique identifier for a single Relationship associated with the Matter. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**destroy** | **bool** | The destroy flag. If the flag is set to &#x60;true&#x60; and the unique identifier of the associated Relationship is present, the Relationship is deleted from the Matter. | [optional] 

## Example

```python
from openapi_client.models.matter_update_request_data_relationships_inner import MatterUpdateRequestDataRelationshipsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatterUpdateRequestDataRelationshipsInner from a JSON string
matter_update_request_data_relationships_inner_instance = MatterUpdateRequestDataRelationshipsInner.from_json(json)
# print the JSON string representation of the object
print(MatterUpdateRequestDataRelationshipsInner.to_json())

# convert the object into a dict
matter_update_request_data_relationships_inner_dict = matter_update_request_data_relationships_inner_instance.to_dict()
# create an instance of MatterUpdateRequestDataRelationshipsInner from a dict
matter_update_request_data_relationships_inner_from_dict = MatterUpdateRequestDataRelationshipsInner.from_dict(matter_update_request_data_relationships_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


