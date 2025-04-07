# CreditMemoList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CreditMemo]**](CreditMemo.md) | CreditMemo List Response | 

## Example

```python
from openapi_client.models.credit_memo_list import CreditMemoList

# TODO update the JSON string below
json = "{}"
# create an instance of CreditMemoList from a JSON string
credit_memo_list_instance = CreditMemoList.from_json(json)
# print the JSON string representation of the object
print(CreditMemoList.to_json())

# convert the object into a dict
credit_memo_list_dict = credit_memo_list_instance.to_dict()
# create an instance of CreditMemoList from a dict
credit_memo_list_from_dict = CreditMemoList.from_dict(credit_memo_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


