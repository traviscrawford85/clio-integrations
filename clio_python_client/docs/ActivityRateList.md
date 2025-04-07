# ActivityRateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ActivityRate]**](ActivityRate.md) | ActivityRate List Response | 

## Example

```python
from openapi_client.models.activity_rate_list import ActivityRateList

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityRateList from a JSON string
activity_rate_list_instance = ActivityRateList.from_json(json)
# print the JSON string representation of the object
print(ActivityRateList.to_json())

# convert the object into a dict
activity_rate_list_dict = activity_rate_list_instance.to_dict()
# create an instance of ActivityRateList from a dict
activity_rate_list_from_dict = ActivityRateList.from_dict(activity_rate_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


