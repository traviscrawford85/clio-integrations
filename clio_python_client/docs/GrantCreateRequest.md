# GrantCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GrantCreateRequestData**](GrantCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.grant_create_request import GrantCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrantCreateRequest from a JSON string
grant_create_request_instance = GrantCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GrantCreateRequest.to_json())

# convert the object into a dict
grant_create_request_dict = grant_create_request_instance.to_dict()
# create an instance of GrantCreateRequest from a dict
grant_create_request_from_dict = GrantCreateRequest.from_dict(grant_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


