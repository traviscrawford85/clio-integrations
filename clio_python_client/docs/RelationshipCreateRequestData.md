# RelationshipCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**MatterUpdateRequestDataRelationshipsInnerContact**](MatterUpdateRequestDataRelationshipsInnerContact.md) |  | [optional] 
**description** | **str** | Describe the relationship between a Contact and a Matter. | [optional] 
**matter** | [**RelationshipCreateRequestDataMatter**](RelationshipCreateRequestDataMatter.md) |  | [optional] 

## Example

```python
from openapi_client.models.relationship_create_request_data import RelationshipCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipCreateRequestData from a JSON string
relationship_create_request_data_instance = RelationshipCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(RelationshipCreateRequestData.to_json())

# convert the object into a dict
relationship_create_request_data_dict = relationship_create_request_data_instance.to_dict()
# create an instance of RelationshipCreateRequestData from a dict
relationship_create_request_data_from_dict = RelationshipCreateRequestData.from_dict(relationship_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


