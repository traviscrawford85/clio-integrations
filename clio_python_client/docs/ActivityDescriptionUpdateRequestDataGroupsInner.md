# ActivityDescriptionUpdateRequestDataGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Group associated with the ActivityDescription. The keyword &#x60;null&#x60; is not valid for this field. | [optional] 
**deleted** | **bool** | A flag to determine if this Group should lose access to this ActivityDescription. | [optional] 

## Example

```python
from openapi_client.models.activity_description_update_request_data_groups_inner import ActivityDescriptionUpdateRequestDataGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityDescriptionUpdateRequestDataGroupsInner from a JSON string
activity_description_update_request_data_groups_inner_instance = ActivityDescriptionUpdateRequestDataGroupsInner.from_json(json)
# print the JSON string representation of the object
print(ActivityDescriptionUpdateRequestDataGroupsInner.to_json())

# convert the object into a dict
activity_description_update_request_data_groups_inner_dict = activity_description_update_request_data_groups_inner_instance.to_dict()
# create an instance of ActivityDescriptionUpdateRequestDataGroupsInner from a dict
activity_description_update_request_data_groups_inner_from_dict = ActivityDescriptionUpdateRequestDataGroupsInner.from_dict(activity_description_update_request_data_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


