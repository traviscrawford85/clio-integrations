# RelationshipCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RelationshipCreateRequestData**](RelationshipCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.relationship_create_request import RelationshipCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipCreateRequest from a JSON string
relationship_create_request_instance = RelationshipCreateRequest.from_json(json)
# print the JSON string representation of the object
print(RelationshipCreateRequest.to_json())

# convert the object into a dict
relationship_create_request_dict = relationship_create_request_instance.to_dict()
# create an instance of RelationshipCreateRequest from a dict
relationship_create_request_from_dict = RelationshipCreateRequest.from_dict(relationship_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


