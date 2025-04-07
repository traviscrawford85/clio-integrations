# ContingencyFeeBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ContingencyFee* | [optional] 
**etag** | **str** | ETag for the *ContingencyFee* | [optional] 
**created_at** | **datetime** | The time the *ContingencyFee* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ContingencyFee* was last updated (as a ISO-8601 timestamp) | [optional] 
**show_contingency_award** | **bool** | Whether the *ContingencyFee* is posted or on a bill | [optional] 

## Example

```python
from openapi_client.models.contingency_fee_base import ContingencyFeeBase

# TODO update the JSON string below
json = "{}"
# create an instance of ContingencyFeeBase from a JSON string
contingency_fee_base_instance = ContingencyFeeBase.from_json(json)
# print the JSON string representation of the object
print(ContingencyFeeBase.to_json())

# convert the object into a dict
contingency_fee_base_dict = contingency_fee_base_instance.to_dict()
# create an instance of ContingencyFeeBase from a dict
contingency_fee_base_from_dict = ContingencyFeeBase.from_dict(contingency_fee_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


