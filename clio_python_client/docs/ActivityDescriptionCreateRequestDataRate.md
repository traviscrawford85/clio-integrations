# ActivityDescriptionCreateRequestDataRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The rate of the ActivityDescription. This is ignored for &#39;User&#39; rates. | [optional] [default to 0]
**non_billable_amount** | **float** | The non billable rate of the ActivityDescription. This is ignored for &#39;User&#39; rates. | [optional] [default to 0]
**type** | **str** | What kind of rate it will be. | [optional] 

## Example

```python
from openapi_client.models.activity_description_create_request_data_rate import ActivityDescriptionCreateRequestDataRate

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityDescriptionCreateRequestDataRate from a JSON string
activity_description_create_request_data_rate_instance = ActivityDescriptionCreateRequestDataRate.from_json(json)
# print the JSON string representation of the object
print(ActivityDescriptionCreateRequestDataRate.to_json())

# convert the object into a dict
activity_description_create_request_data_rate_dict = activity_description_create_request_data_rate_instance.to_dict()
# create an instance of ActivityDescriptionCreateRequestDataRate from a dict
activity_description_create_request_data_rate_from_dict = ActivityDescriptionCreateRequestDataRate.from_dict(activity_description_create_request_data_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


