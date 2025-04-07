# AllocationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Allocation]**](Allocation.md) | Allocation List Response | 

## Example

```python
from openapi_client.models.allocation_list import AllocationList

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationList from a JSON string
allocation_list_instance = AllocationList.from_json(json)
# print the JSON string representation of the object
print(AllocationList.to_json())

# convert the object into a dict
allocation_list_dict = allocation_list_instance.to_dict()
# create an instance of AllocationList from a dict
allocation_list_from_dict = AllocationList.from_dict(allocation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


