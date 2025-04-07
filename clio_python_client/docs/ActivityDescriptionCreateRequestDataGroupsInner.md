# ActivityDescriptionCreateRequestDataGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Group associated with the ActivityDescription. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 

## Example

```python
from openapi_client.models.activity_description_create_request_data_groups_inner import ActivityDescriptionCreateRequestDataGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityDescriptionCreateRequestDataGroupsInner from a JSON string
activity_description_create_request_data_groups_inner_instance = ActivityDescriptionCreateRequestDataGroupsInner.from_json(json)
# print the JSON string representation of the object
print(ActivityDescriptionCreateRequestDataGroupsInner.to_json())

# convert the object into a dict
activity_description_create_request_data_groups_inner_dict = activity_description_create_request_data_groups_inner_instance.to_dict()
# create an instance of ActivityDescriptionCreateRequestDataGroupsInner from a dict
activity_description_create_request_data_groups_inner_from_dict = ActivityDescriptionCreateRequestDataGroupsInner.from_dict(activity_description_create_request_data_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


