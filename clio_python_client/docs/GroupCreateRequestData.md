# GroupCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Group. | [optional] 

## Example

```python
from openapi_client.models.group_create_request_data import GroupCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCreateRequestData from a JSON string
group_create_request_data_instance = GroupCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(GroupCreateRequestData.to_json())

# convert the object into a dict
group_create_request_data_dict = group_create_request_data_instance.to_dict()
# create an instance of GroupCreateRequestData from a dict
group_create_request_data_from_dict = GroupCreateRequestData.from_dict(group_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


