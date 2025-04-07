# GrantFundingSourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GrantFundingSource]**](GrantFundingSource.md) | GrantFundingSource List Response | 

## Example

```python
from openapi_client.models.grant_funding_source_list import GrantFundingSourceList

# TODO update the JSON string below
json = "{}"
# create an instance of GrantFundingSourceList from a JSON string
grant_funding_source_list_instance = GrantFundingSourceList.from_json(json)
# print the JSON string representation of the object
print(GrantFundingSourceList.to_json())

# convert the object into a dict
grant_funding_source_list_dict = grant_funding_source_list_instance.to_dict()
# create an instance of GrantFundingSourceList from a dict
grant_funding_source_list_from_dict = GrantFundingSourceList.from_dict(grant_funding_source_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


