# PracticeAreaCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The practice area category associated with the *PracticeArea*. The friendly display values corresponding to the enum strings: * Administrative * Admiralty / Maritime * Anti-Trust / Competition * Appellate * Banking / Finance * Bankruptcy * Business Formation / Compliance * Civil Litigation * Civil Rights / Constitutional * Collections &amp; Debt * Commercial / Sale of Goods * Commercial Litigation * Construction * Consumer Protection * Contracts * Corporate Litigation * Criminal * Disability / Social Security * Education * Elder * Employment / Labor * Energy / Environmental * Ethics * Family * Food / Drug * General Practice * Government * Healthcare * Immigration * In-House Counsel * Insurance * Intellectual Property * International * Juvenile * Legal Aid * Mediation / Arbitration * Medical Malpractice * Military * Multi-Practice * Non-Profit / Pro Bono * Other * Personal Injury * Privacy / Information Security * Private Client * Product Liability * Real Estate * Science / Technology * Securities / Mergers &amp; Acquisitions * Small Claims * Sports / Entertainment / Gaming * Tax * Telecommunications * Traffic Offenses * Transportation * Tribal * Trusts * Wills &amp; Estates * Worker&#39;s Compensation  | [optional] 
**code** | **str** | The code attached to the PracticeArea. | [optional] 
**name** | **str** | Name of the PracticeArea. | 

## Example

```python
from openapi_client.models.practice_area_create_request_data import PracticeAreaCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of PracticeAreaCreateRequestData from a JSON string
practice_area_create_request_data_instance = PracticeAreaCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(PracticeAreaCreateRequestData.to_json())

# convert the object into a dict
practice_area_create_request_data_dict = practice_area_create_request_data_instance.to_dict()
# create an instance of PracticeAreaCreateRequestData from a dict
practice_area_create_request_data_from_dict = PracticeAreaCreateRequestData.from_dict(practice_area_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


