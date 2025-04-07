# UtbmsSetList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UtbmsSet]**](UtbmsSet.md) | UtbmsSet List Response | 

## Example

```python
from openapi_client.models.utbms_set_list import UtbmsSetList

# TODO update the JSON string below
json = "{}"
# create an instance of UtbmsSetList from a JSON string
utbms_set_list_instance = UtbmsSetList.from_json(json)
# print the JSON string representation of the object
print(UtbmsSetList.to_json())

# convert the object into a dict
utbms_set_list_dict = utbms_set_list_instance.to_dict()
# create an instance of UtbmsSetList from a dict
utbms_set_list_from_dict = UtbmsSetList.from_dict(utbms_set_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


