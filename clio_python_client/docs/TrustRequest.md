# TrustRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *TrustRequest* | [optional] 
**etag** | **str** | ETag for the *TrustRequest* | [optional] 
**created_at** | **datetime** | The time the *TrustRequest* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *TrustRequest* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.trust_request import TrustRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrustRequest from a JSON string
trust_request_instance = TrustRequest.from_json(json)
# print the JSON string representation of the object
print(TrustRequest.to_json())

# convert the object into a dict
trust_request_dict = trust_request_instance.to_dict()
# create an instance of TrustRequest from a dict
trust_request_from_dict = TrustRequest.from_dict(trust_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


