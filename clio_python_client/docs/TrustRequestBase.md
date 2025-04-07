# TrustRequestBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *TrustRequest* | [optional] 
**etag** | **str** | ETag for the *TrustRequest* | [optional] 
**created_at** | **datetime** | The time the *TrustRequest* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *TrustRequest* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.trust_request_base import TrustRequestBase

# TODO update the JSON string below
json = "{}"
# create an instance of TrustRequestBase from a JSON string
trust_request_base_instance = TrustRequestBase.from_json(json)
# print the JSON string representation of the object
print(TrustRequestBase.to_json())

# convert the object into a dict
trust_request_base_dict = trust_request_base_instance.to_dict()
# create an instance of TrustRequestBase from a dict
trust_request_base_from_dict = TrustRequestBase.from_dict(trust_request_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


