# ActivityDescriptionUpdateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **object** | Currency of the ActivityDescription. | [optional] 
**default** | **bool** | Whether or not this should be the API User&#39;s default ActivityDescription. | [optional] 
**groups** | [**List[ActivityDescriptionUpdateRequestDataGroupsInner]**](ActivityDescriptionUpdateRequestDataGroupsInner.md) |  | [optional] 
**name** | **str** | A detailed description of the ActivityDescription. | [optional] 
**rate** | [**ActivityDescriptionCreateRequestDataRate**](ActivityDescriptionCreateRequestDataRate.md) |  | [optional] 
**visible_to_co_counsel** | **bool** | Whether or not co counsels on the account can see this ActivityDescription. | [optional] 

## Example

```python
from openapi_client.models.activity_description_update_request_data import ActivityDescriptionUpdateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityDescriptionUpdateRequestData from a JSON string
activity_description_update_request_data_instance = ActivityDescriptionUpdateRequestData.from_json(json)
# print the JSON string representation of the object
print(ActivityDescriptionUpdateRequestData.to_json())

# convert the object into a dict
activity_description_update_request_data_dict = activity_description_update_request_data_instance.to_dict()
# create an instance of ActivityDescriptionUpdateRequestData from a dict
activity_description_update_request_data_from_dict = ActivityDescriptionUpdateRequestData.from_dict(activity_description_update_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


