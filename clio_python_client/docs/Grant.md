# Grant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Grant* | [optional] 
**etag** | **str** | ETag for the *Grant* | [optional] 
**name** | **str** | The name of the *Grant* | [optional] 
**funding_code** | **str** | Funding code of the grant | [optional] 
**funding_code_and_name** | **str** | Funding code and name of the grant | [optional] 
**funding_source_name** | **str** | Name of the funding source of the grant | [optional] 
**created_at** | **datetime** | The time the *Grant* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Grant* was last updated (as a ISO-8601 timestamp) | [optional] 
**balance** | **str** | Balance of the grant | [optional] 
**start_date** | **date** | Start date of the grant | [optional] 
**end_date** | **date** | End date of the grant | [optional] 
**grant_funding_source** | [**GrantFundingSourceBase**](GrantFundingSourceBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.grant import Grant

# TODO update the JSON string below
json = "{}"
# create an instance of Grant from a JSON string
grant_instance = Grant.from_json(json)
# print the JSON string representation of the object
print(Grant.to_json())

# convert the object into a dict
grant_dict = grant_instance.to_dict()
# create an instance of Grant from a dict
grant_from_dict = Grant.from_dict(grant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


