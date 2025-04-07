# MatterCreateRequestDataRelationshipsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Describe the relationship between a Contact and a Matter. | 
**contact** | [**MatterCreateRequestDataRelationshipsInnerContact**](MatterCreateRequestDataRelationshipsInnerContact.md) |  | 

## Example

```python
from openapi_client.models.matter_create_request_data_relationships_inner import MatterCreateRequestDataRelationshipsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataRelationshipsInner from a JSON string
matter_create_request_data_relationships_inner_instance = MatterCreateRequestDataRelationshipsInner.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataRelationshipsInner.to_json())

# convert the object into a dict
matter_create_request_data_relationships_inner_dict = matter_create_request_data_relationships_inner_instance.to_dict()
# create an instance of MatterCreateRequestDataRelationshipsInner from a dict
matter_create_request_data_relationships_inner_from_dict = MatterCreateRequestDataRelationshipsInner.from_dict(matter_create_request_data_relationships_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


