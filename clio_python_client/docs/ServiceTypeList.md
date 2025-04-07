# ServiceTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceType]**](ServiceType.md) | ServiceType List Response | 

## Example

```python
from openapi_client.models.service_type_list import ServiceTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTypeList from a JSON string
service_type_list_instance = ServiceTypeList.from_json(json)
# print the JSON string representation of the object
print(ServiceTypeList.to_json())

# convert the object into a dict
service_type_list_dict = service_type_list_instance.to_dict()
# create an instance of ServiceTypeList from a dict
service_type_list_from_dict = ServiceTypeList.from_dict(service_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


