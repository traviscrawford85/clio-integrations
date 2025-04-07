# GrantFundingSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *GrantFundingSource* | [optional] 
**etag** | **str** | ETag for the *GrantFundingSource* | [optional] 
**name** | **str** | The name of the *GrantFundingSource* | [optional] 
**created_at** | **datetime** | The time the *GrantFundingSource* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *GrantFundingSource* was last updated (as a ISO-8601 timestamp) | [optional] 
**grants** | [**List[GrantBase]**](GrantBase.md) | Grant | [optional] 

## Example

```python
from openapi_client.models.grant_funding_source import GrantFundingSource

# TODO update the JSON string below
json = "{}"
# create an instance of GrantFundingSource from a JSON string
grant_funding_source_instance = GrantFundingSource.from_json(json)
# print the JSON string representation of the object
print(GrantFundingSource.to_json())

# convert the object into a dict
grant_funding_source_dict = grant_funding_source_instance.to_dict()
# create an instance of GrantFundingSource from a dict
grant_funding_source_from_dict = GrantFundingSource.from_dict(grant_funding_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


