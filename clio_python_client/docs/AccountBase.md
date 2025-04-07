# AccountBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Account* | [optional] 
**etag** | **str** | ETag for the *Account* | [optional] 
**name** | **str** | The name of the *Account* | [optional] 
**state** | **str** | Account state | [optional] 
**created_at** | **datetime** | The time the *Account* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Account* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.account_base import AccountBase

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBase from a JSON string
account_base_instance = AccountBase.from_json(json)
# print the JSON string representation of the object
print(AccountBase.to_json())

# convert the object into a dict
account_base_dict = account_base_instance.to_dict()
# create an instance of AccountBase from a dict
account_base_from_dict = AccountBase.from_dict(account_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


