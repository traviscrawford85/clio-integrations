# GrantFundingSourceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GrantFundingSourceCreateRequestData**](GrantFundingSourceCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.grant_funding_source_create_request import GrantFundingSourceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrantFundingSourceCreateRequest from a JSON string
grant_funding_source_create_request_instance = GrantFundingSourceCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GrantFundingSourceCreateRequest.to_json())

# convert the object into a dict
grant_funding_source_create_request_dict = grant_funding_source_create_request_instance.to_dict()
# create an instance of GrantFundingSourceCreateRequest from a dict
grant_funding_source_create_request_from_dict = GrantFundingSourceCreateRequest.from_dict(grant_funding_source_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


