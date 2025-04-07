# GroupBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_connect_user** | **bool** | Whether or not the Group is a UserGroup for a Clio Connect User | [optional] 
**etag** | **str** | ETag for the *Group* | [optional] 
**id** | **int** | Unique identifier for the *Group* | [optional] 
**name** | **str** | The name of the *Group* | [optional] 
**type** | **str** | The type of the *Group* | [optional] 
**updated_at** | **datetime** | The time the *Group* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.group_base import GroupBase

# TODO update the JSON string below
json = "{}"
# create an instance of GroupBase from a JSON string
group_base_instance = GroupBase.from_json(json)
# print the JSON string representation of the object
print(GroupBase.to_json())

# convert the object into a dict
group_base_dict = group_base_instance.to_dict()
# create an instance of GroupBase from a dict
group_base_from_dict = GroupBase.from_dict(group_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


