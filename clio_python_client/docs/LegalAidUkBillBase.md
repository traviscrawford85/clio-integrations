# LegalAidUkBillBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_travel_payment** | **bool** | Additional travel payment, for Legal Aid England and Wales | [optional] 
**adjourned_hearing_fee** | **str** | Adjourned hearing fee | [optional] 
**advocacy_costs** | **float** | Advocacy costs | [optional] 
**advice_time** | **int** | Advice time | [optional] 
**bill_type** | **int** | Bill type | [optional] 
**case_concluded** | **date** | Case concluded | [optional] 
**case_stage_level** | **int** | Case stage level | [optional] 
**cla_exemption_code** | **str** | CLA exemption code | [optional] 
**cla_reference** | **str** | CLA reference | [optional] 
**cmrh_oral** | **int** | CMRH oral | [optional] 
**cmrh_telephone** | **int** | CMRH telephone | [optional] 
**cost_of_counsel** | **str** | Cost of counsel | [optional] 
**costs_are_those_of** | **int** | Costs are those of | [optional] 
**court_location** | **str** | Court location (HPCDS matters) | [optional] 
**date_of_claim** | **date** | Date of claim | [optional] 
**designated_accredited_representative** | **int** | Designated accredited representative | [optional] 
**detention_travel_and_waiting_costs** | **str** | Detention travel &amp; waiting costs ex VAT | [optional] 
**disbursements_vat** | **float** | Disbursements VAT | [optional] 
**exceptional_case_funding_reference** | **str** | Exceptional case funding reference | [optional] 
**exemption_criteria_satisfied** | **int** | Exemption criteria satisfied | [optional] 
**follow_on_work** | **int** | Follow on work | [optional] 
**ho_interview** | **int** | HO interview | [optional] 
**ho_ucn** | **int** | HO UCN | [optional] 
**id** | **int** | Unique identifier for the *LegalAidUkBill* | [optional] 
**independent_medical_reports_claimed** | **str** | Independent medical reports claimed | [optional] 
**jr_form_filling** | **str** | JR/Form filling ex VAT, for Legal Aid England and Wales | [optional] 
**maat_id** | **str** | MAAT ID | [optional] 
**meetings_attended** | **int** | Meetings attended | [optional] 
**mht_ref_no** | **str** | MHT reference number | [optional] 
**net_disbursements** | **float** | Net disbursements | [optional] 
**net_profit_costs** | **float** | Net profit cost | [optional] 
**niat_disbursement_prior_authority_number** | **str** | NIAT disbursement prior authority number | [optional] 
**number_of_attendances** | **int** | Number of attendances | [optional] 
**outcome_for_the_client** | **int** | Outcome for the client | [optional] 
**profit_costs_ex_vat** | **int** | Profit costs ex VAT | [optional] 
**prior_authority_reference** | **str** | Prior authority reference number | [optional] 
**representation_order_date** | **date** | Representation order date | [optional] 
**stage_reached** | **int** | Stage reached | [optional] 
**substantive_hearing** | **int** | Substantive hearing | [optional] 
**travel_and_waiting_costs** | **float** | Travel &amp; waiting costs | [optional] 
**travel_time** | **int** | Travel time | [optional] 
**value_of_costs** | **str** | Value of costs | [optional] 
**waiting_time** | **int** | Waiting time | [optional] 

## Example

```python
from openapi_client.models.legal_aid_uk_bill_base import LegalAidUkBillBase

# TODO update the JSON string below
json = "{}"
# create an instance of LegalAidUkBillBase from a JSON string
legal_aid_uk_bill_base_instance = LegalAidUkBillBase.from_json(json)
# print the JSON string representation of the object
print(LegalAidUkBillBase.to_json())

# convert the object into a dict
legal_aid_uk_bill_base_dict = legal_aid_uk_bill_base_instance.to_dict()
# create an instance of LegalAidUkBillBase from a dict
legal_aid_uk_bill_base_from_dict = LegalAidUkBillBase.from_dict(legal_aid_uk_bill_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


