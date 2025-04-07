# RelationshipList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Relationship]**](Relationship.md) | Relationship List Response | 

## Example

```python
from openapi_client.models.relationship_list import RelationshipList

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipList from a JSON string
relationship_list_instance = RelationshipList.from_json(json)
# print the JSON string representation of the object
print(RelationshipList.to_json())

# convert the object into a dict
relationship_list_dict = relationship_list_instance.to_dict()
# create an instance of RelationshipList from a dict
relationship_list_from_dict = RelationshipList.from_dict(relationship_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


