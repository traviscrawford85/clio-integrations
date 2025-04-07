# PracticeAreaUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PracticeAreaUpdateRequestData**](PracticeAreaUpdateRequestData.md) |  | 

## Example

```python
from openapi_client.models.practice_area_update_request import PracticeAreaUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PracticeAreaUpdateRequest from a JSON string
practice_area_update_request_instance = PracticeAreaUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PracticeAreaUpdateRequest.to_json())

# convert the object into a dict
practice_area_update_request_dict = practice_area_update_request_instance.to_dict()
# create an instance of PracticeAreaUpdateRequest from a dict
practice_area_update_request_from_dict = PracticeAreaUpdateRequest.from_dict(practice_area_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


