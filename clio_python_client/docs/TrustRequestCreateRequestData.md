# TrustRequestCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **bool** | Whether or not the TrustRequest should be automatically approved. | 
**client_id** | **int** | The client_id associated to the TrustRequest | 
**due_date** | **date** | The date the TrustRequest is due (Expects an ISO-8601 date). | 
**issue_date** | **date** | The date the TrustRequest is issued (Expects an ISO-8601 date). | 
**matter** | [**List[TrustRequestCreateRequestDataMatterInner]**](TrustRequestCreateRequestDataMatterInner.md) |  | [optional] 
**note** | **str** | The client level TrustRequest note | [optional] 
**trust_amount** | **float** | The TrustRequest&#39;s amount | 
**trust_type** | **str** | The type of TrustRequest | 

## Example

```python
from openapi_client.models.trust_request_create_request_data import TrustRequestCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TrustRequestCreateRequestData from a JSON string
trust_request_create_request_data_instance = TrustRequestCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(TrustRequestCreateRequestData.to_json())

# convert the object into a dict
trust_request_create_request_data_dict = trust_request_create_request_data_instance.to_dict()
# create an instance of TrustRequestCreateRequestData from a dict
trust_request_create_request_data_from_dict = TrustRequestCreateRequestData.from_dict(trust_request_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


