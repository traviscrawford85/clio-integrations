# InterestChargeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InterestCharge]**](InterestCharge.md) | InterestCharge List Response | 

## Example

```python
from openapi_client.models.interest_charge_list import InterestChargeList

# TODO update the JSON string below
json = "{}"
# create an instance of InterestChargeList from a JSON string
interest_charge_list_instance = InterestChargeList.from_json(json)
# print the JSON string representation of the object
print(InterestChargeList.to_json())

# convert the object into a dict
interest_charge_list_dict = interest_charge_list_instance.to_dict()
# create an instance of InterestChargeList from a dict
interest_charge_list_from_dict = InterestChargeList.from_dict(interest_charge_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


