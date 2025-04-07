# MatterDocketList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MatterDocket]**](MatterDocket.md) | MatterDocket List Response | 

## Example

```python
from openapi_client.models.matter_docket_list import MatterDocketList

# TODO update the JSON string below
json = "{}"
# create an instance of MatterDocketList from a JSON string
matter_docket_list_instance = MatterDocketList.from_json(json)
# print the JSON string representation of the object
print(MatterDocketList.to_json())

# convert the object into a dict
matter_docket_list_dict = matter_docket_list_instance.to_dict()
# create an instance of MatterDocketList from a dict
matter_docket_list_from_dict = MatterDocketList.from_dict(matter_docket_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


