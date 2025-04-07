# GrantFundingSourceCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the GrantFundingSource. | [optional] 

## Example

```python
from openapi_client.models.grant_funding_source_create_request_data import GrantFundingSourceCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of GrantFundingSourceCreateRequestData from a JSON string
grant_funding_source_create_request_data_instance = GrantFundingSourceCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(GrantFundingSourceCreateRequestData.to_json())

# convert the object into a dict
grant_funding_source_create_request_data_dict = grant_funding_source_create_request_data_instance.to_dict()
# create an instance of GrantFundingSourceCreateRequestData from a dict
grant_funding_source_create_request_data_from_dict = GrantFundingSourceCreateRequestData.from_dict(grant_funding_source_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


