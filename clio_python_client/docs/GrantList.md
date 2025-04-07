# GrantList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Grant]**](Grant.md) | Grant List Response | 

## Example

```python
from openapi_client.models.grant_list import GrantList

# TODO update the JSON string below
json = "{}"
# create an instance of GrantList from a JSON string
grant_list_instance = GrantList.from_json(json)
# print the JSON string representation of the object
print(GrantList.to_json())

# convert the object into a dict
grant_list_dict = grant_list_instance.to_dict()
# create an instance of GrantList from a dict
grant_list_from_dict = GrantList.from_dict(grant_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


