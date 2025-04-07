# GrantCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Grant. | [optional] 

## Example

```python
from openapi_client.models.grant_create_request_data import GrantCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of GrantCreateRequestData from a JSON string
grant_create_request_data_instance = GrantCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(GrantCreateRequestData.to_json())

# convert the object into a dict
grant_create_request_data_dict = grant_create_request_data_instance.to_dict()
# create an instance of GrantCreateRequestData from a dict
grant_create_request_data_from_dict = GrantCreateRequestData.from_dict(grant_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


