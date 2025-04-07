# JurisdictionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Jurisdiction]**](Jurisdiction.md) | Jurisdiction List Response | 

## Example

```python
from openapi_client.models.jurisdiction_list import JurisdictionList

# TODO update the JSON string below
json = "{}"
# create an instance of JurisdictionList from a JSON string
jurisdiction_list_instance = JurisdictionList.from_json(json)
# print the JSON string representation of the object
print(JurisdictionList.to_json())

# convert the object into a dict
jurisdiction_list_dict = jurisdiction_list_instance.to_dict()
# create an instance of JurisdictionList from a dict
jurisdiction_list_from_dict = JurisdictionList.from_dict(jurisdiction_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


