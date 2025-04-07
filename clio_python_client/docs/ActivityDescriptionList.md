# ActivityDescriptionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ActivityDescription]**](ActivityDescription.md) | ActivityDescription List Response | 

## Example

```python
from openapi_client.models.activity_description_list import ActivityDescriptionList

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityDescriptionList from a JSON string
activity_description_list_instance = ActivityDescriptionList.from_json(json)
# print the JSON string representation of the object
print(ActivityDescriptionList.to_json())

# convert the object into a dict
activity_description_list_dict = activity_description_list_instance.to_dict()
# create an instance of ActivityDescriptionList from a dict
activity_description_list_from_dict = ActivityDescriptionList.from_dict(activity_description_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


