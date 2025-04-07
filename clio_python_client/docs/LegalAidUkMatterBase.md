# LegalAidUkMatterBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_point** | **str** | Access point | [optional] 
**laa_office_number** | **str** | LAA office number | [optional] 
**ait_hearing_centre** | **int** | AIT hearing centre | [optional] 
**attended_several_hearings_acting_for_multiple_clients** | **bool** | Attended several hearings acting for multiple clients | [optional] 
**bill_ho_ucn** | **str** | Bill HO UCN | [optional] 
**bill_number_of_attendances** | **int** | Bill number of attendances | [optional] 
**bill_outcome_for_the_client_code** | **int** | Bill outcome for the client code | [optional] 
**bill_stage_reached_code** | **int** | Bill stage reached code | [optional] 
**case_reference** | **str** | Case reference | [optional] 
**case_start_date** | **date** | Case start date | [optional] 
**category** | **int** | Category | [optional] 
**category_as_string** | **str** | Category as string | [optional] 
**certificate_effective_date** | **date** | Certificate effective date | [optional] 
**certificate_expiration_date** | **date** | Certificate expiration date | [optional] 
**certificate_number** | **str** | Certificate number | [optional] 
**certificate_scope** | **str** | Certificate scope | [optional] 
**certification_type** | **int** | Certification type | [optional] 
**change_of_solicitor** | **bool** | Change of solicitor | [optional] 
**client_equal_opportunity_monitoring** | **str** | Client equal opportunity monitoring | [optional] 
**client_type** | **int** | Client type | [optional] 
**clr_start_date** | **date** | CLR start date | [optional] 
**clr_total_profit_costs** | **str** | CLR total profit costs | [optional] 
**cost_limit** | **str** | Cost limit | [optional] 
**counsel** | **int** | Counsel | [optional] 
**court** | **int** | Court | [optional] 
**court_id** | **int** | Court ID | [optional] 
**court_id_code** | **str** | Court ID code | [optional] 
**created_at** | **datetime** | The time the *LegalAidUkMatter* was created (as a ISO-8601 timestamp) | [optional] 
**delivery_location** | **str** | Delivery location | [optional] 
**dscc_number** | **str** | DSCC number | [optional] 
**duty_solicitor** | **bool** | Duty solicitor | [optional] 
**etag** | **str** | ETag for the *LegalAidUkMatter* | [optional] 
**exceptional_case_funding_reference** | **str** | Exceptional case funding reference | [optional] 
**expense_limit** | **str** | Expense limit | [optional] 
**fee_scheme** | **int** | Fee scheme | [optional] 
**first_conducting_solicitor** | **bool** | First conducting solicitor | [optional] 
**id** | **int** | Unique identifier for the *LegalAidUkMatter* | [optional] 
**irc_surgery** | **str** | Irc surgery | [optional] 
**legacy_case** | **str** | Legacy case | [optional] 
**legal_representation_number** | **str** | Legal representation number | [optional] 
**lh_total_disbursements** | **str** | LH total disbursements | [optional] 
**lh_start_date** | **str** | LH start date | [optional] 
**lh_total_profit_costs** | **str** | LH total profit costs | [optional] 
**linked_matter_id** | **int** | Linked matter ID | [optional] 
**local_authority_number** | **str** | Local authority number | [optional] 
**maat_id** | **str** | MAAT ID | [optional] 
**matter_type** | **int** | Matter type | [optional] 
**matter_type_code** | **str** | Matter type code | [optional] 
**matter_type_1** | **int** | Matter type 1 | [optional] 
**matter_type_1_code** | **str** | Matter type 1 code | [optional] 
**matter_type_1_title** | **str** | Matter type 1 title | [optional] 
**matter_type_2** | **int** | Matter type 2 | [optional] 
**matter_type_2_code** | **str** | Matter type 2 code | [optional] 
**matter_type_2_title** | **str** | Matter type 2 title | [optional] 
**matter_types_combined** | **str** | Matter types combined | [optional] 
**number_of_clients_seen_at_surgery** | **int** | Number of clients seen at surgery | [optional] 
**number_of_clients** | **int** | Number of clients | [optional] 
**party** | **int** | Party | [optional] 
**police_station** | **str** | Police station | [optional] 
**post_transfer_clients_represented** | **int** | Post transfer clients represented | [optional] 
**postal_application_accepted** | **str** | Postal application accepted | [optional] 
**prior_authority_reference** | **str** | Priory authority reference | [optional] 
**prison_id** | **int** | Prison ID | [optional] 
**prison_law_prior_approval_number** | **str** | Prison law prior approval number | [optional] 
**procurement_area** | **str** | Procurement area | [optional] 
**region** | **int** | Region | [optional] 
**related_claims_number** | **str** | Related claims number | [optional] 
**representation_order_date** | **date** | Representation order date | [optional] 
**schedule_reference_number** | **str** | Schedule reference number | [optional] 
**scheme_id** | **str** | Scheme ID | [optional] 
**session_type** | **int** | Session type | [optional] 
**solicitor_type** | **int** | Solicitor type | [optional] 
**standard_fee_category** | **int** | Standard fee category | [optional] 
**surgery_clients_resulting_in_a_legal_help_matter_opened** | **int** | Surgery clients resulting in a legal help matter opened | [optional] 
**surgery_clients** | **int** | Surgery clients | [optional] 
**surgery_date** | **date** | Surgery date | [optional] 
**transfer_date** | **date** | Transfer date | [optional] 
**type_of_advice** | **int** | Type of advice | [optional] 
**type_of_service** | **str** | Type of service | [optional] 
**ucn** | **str** | UCN | [optional] 
**ufn** | **str** | UFN | [optional] 
**undesignated_area_court** | **bool** | Undesignated area court | [optional] 
**updated_at** | **datetime** | The time the *LegalAidUkMatter* was last updated (as a ISO-8601 timestamp) | [optional] 
**user_type** | **int** | User type | [optional] 
**youth_court** | **bool** | Youth court | [optional] 

## Example

```python
from openapi_client.models.legal_aid_uk_matter_base import LegalAidUkMatterBase

# TODO update the JSON string below
json = "{}"
# create an instance of LegalAidUkMatterBase from a JSON string
legal_aid_uk_matter_base_instance = LegalAidUkMatterBase.from_json(json)
# print the JSON string representation of the object
print(LegalAidUkMatterBase.to_json())

# convert the object into a dict
legal_aid_uk_matter_base_dict = legal_aid_uk_matter_base_instance.to_dict()
# create an instance of LegalAidUkMatterBase from a dict
legal_aid_uk_matter_base_from_dict = LegalAidUkMatterBase.from_dict(legal_aid_uk_matter_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


