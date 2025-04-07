# Currency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Currency* | [optional] 
**etag** | **str** | ETag for the *Currency* | [optional] 
**code** | **str** | ISO 4217 code for the *Currency* | [optional] 
**sign** | **str** | Symbol used to denote monetary values using this *Currency* | [optional] 
**created_at** | **datetime** | The time the *Currency* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Currency* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from openapi_client.models.currency import Currency

# TODO update the JSON string below
json = "{}"
# create an instance of Currency from a JSON string
currency_instance = Currency.from_json(json)
# print the JSON string representation of the object
print(Currency.to_json())

# convert the object into a dict
currency_dict = currency_instance.to_dict()
# create an instance of Currency from a dict
currency_from_dict = Currency.from_dict(currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


