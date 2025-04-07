# MatterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Matter]**](Matter.md) | Matter List Response | 

## Example

```python
from openapi_client.models.matter_list import MatterList

# TODO update the JSON string below
json = "{}"
# create an instance of MatterList from a JSON string
matter_list_instance = MatterList.from_json(json)
# print the JSON string representation of the object
print(MatterList.to_json())

# convert the object into a dict
matter_list_dict = matter_list_instance.to_dict()
# create an instance of MatterList from a dict
matter_list_from_dict = MatterList.from_dict(matter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


