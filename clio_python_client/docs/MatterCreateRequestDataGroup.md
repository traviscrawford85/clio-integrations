# MatterCreateRequestDataGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Group associated with the Matter. Use the keyword &#x60;null&#x60; to specify no association. | [optional] 

## Example

```python
from openapi_client.models.matter_create_request_data_group import MatterCreateRequestDataGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MatterCreateRequestDataGroup from a JSON string
matter_create_request_data_group_instance = MatterCreateRequestDataGroup.from_json(json)
# print the JSON string representation of the object
print(MatterCreateRequestDataGroup.to_json())

# convert the object into a dict
matter_create_request_data_group_dict = matter_create_request_data_group_instance.to_dict()
# create an instance of MatterCreateRequestDataGroup from a dict
matter_create_request_data_group_from_dict = MatterCreateRequestDataGroup.from_dict(matter_create_request_data_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


