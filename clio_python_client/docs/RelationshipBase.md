# RelationshipBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Relationship* | [optional] 
**etag** | **str** | ETag for the *Relationship* | [optional] 
**description** | **str** | A detailed description of the *Relationship* | [optional] 
**created_at** | **datetime** | The time the *Relationship* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Relationship* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.relationship_base import RelationshipBase

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipBase from a JSON string
relationship_base_instance = RelationshipBase.from_json(json)
# print the JSON string representation of the object
print(RelationshipBase.to_json())

# convert the object into a dict
relationship_base_dict = relationship_base_instance.to_dict()
# create an instance of RelationshipBase from a dict
relationship_base_from_dict = RelationshipBase.from_dict(relationship_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


