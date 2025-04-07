# TrustRequestCreateRequestDataMatterInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The matter id associated to the TrustRequest | [optional] 
**trust_amount** | **int** | The matter level TrustRequest&#39;s amount | [optional] 
**note** | **str** | The client level TrustRequest note | [optional] 

## Example

```python
from openapi_client.models.trust_request_create_request_data_matter_inner import TrustRequestCreateRequestDataMatterInner

# TODO update the JSON string below
json = "{}"
# create an instance of TrustRequestCreateRequestDataMatterInner from a JSON string
trust_request_create_request_data_matter_inner_instance = TrustRequestCreateRequestDataMatterInner.from_json(json)
# print the JSON string representation of the object
print(TrustRequestCreateRequestDataMatterInner.to_json())

# convert the object into a dict
trust_request_create_request_data_matter_inner_dict = trust_request_create_request_data_matter_inner_instance.to_dict()
# create an instance of TrustRequestCreateRequestDataMatterInner from a dict
trust_request_create_request_data_matter_inner_from_dict = TrustRequestCreateRequestDataMatterInner.from_dict(trust_request_create_request_data_matter_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


