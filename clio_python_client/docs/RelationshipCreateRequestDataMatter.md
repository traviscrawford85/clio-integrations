# RelationshipCreateRequestDataMatter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Matter associated with the Relationship. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.relationship_create_request_data_matter import RelationshipCreateRequestDataMatter

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipCreateRequestDataMatter from a JSON string
relationship_create_request_data_matter_instance = RelationshipCreateRequestDataMatter.from_json(json)
# print the JSON string representation of the object
print(RelationshipCreateRequestDataMatter.to_json())

# convert the object into a dict
relationship_create_request_data_matter_dict = relationship_create_request_data_matter_instance.to_dict()
# create an instance of RelationshipCreateRequestDataMatter from a dict
relationship_create_request_data_matter_from_dict = RelationshipCreateRequestDataMatter.from_dict(relationship_create_request_data_matter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


