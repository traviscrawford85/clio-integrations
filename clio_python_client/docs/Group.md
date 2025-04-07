# Group


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_connect_user** | **bool** | Whether or not the Group is a UserGroup for a Clio Connect User | [optional] 
**etag** | **str** | ETag for the *Group* | [optional] 
**id** | **int** | Unique identifier for the *Group* | [optional] 
**name** | **str** | The name of the *Group* | [optional] 
**type** | **str** | The type of the *Group* | [optional] 
**updated_at** | **datetime** | The time the *Group* was last updated (as a ISO-8601 timestamp) | [optional] 
**users** | [**List[UserBase]**](UserBase.md) | User | [optional] 

## Example

```python
from openapi_client.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


