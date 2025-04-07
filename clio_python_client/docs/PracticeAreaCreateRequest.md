# PracticeAreaCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PracticeAreaCreateRequestData**](PracticeAreaCreateRequestData.md) |  | 

## Example

```python
from openapi_client.models.practice_area_create_request import PracticeAreaCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PracticeAreaCreateRequest from a JSON string
practice_area_create_request_instance = PracticeAreaCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PracticeAreaCreateRequest.to_json())

# convert the object into a dict
practice_area_create_request_dict = practice_area_create_request_instance.to_dict()
# create an instance of PracticeAreaCreateRequest from a dict
practice_area_create_request_from_dict = PracticeAreaCreateRequest.from_dict(practice_area_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


