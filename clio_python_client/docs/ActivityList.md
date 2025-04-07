# ActivityList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Activity]**](Activity.md) | Activity List Response | 

## Example

```python
from openapi_client.models.activity_list import ActivityList

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityList from a JSON string
activity_list_instance = ActivityList.from_json(json)
# print the JSON string representation of the object
print(ActivityList.to_json())

# convert the object into a dict
activity_list_dict = activity_list_instance.to_dict()
# create an instance of ActivityList from a dict
activity_list_from_dict = ActivityList.from_dict(activity_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


