# coding: utf-8

"""
    Clio API Documentation

    # Developer Support and Feedback * Clio takes the availability and stability of our API seriously; please report any **degradations** or **breakages** to Clio's API Support team at [api@clio.com](mailto:api@clio.com). * For business and partnership inquiries, contact our API Partnerships team at [api.partnerships@clio.com](mailto:api.partnerships@clio.com). * For best practices and tips from the Clio development community, join the conversation in the [Clio Developer Slack Channel](https://join.slack.com/t/clio-public/shared_invite/zt-1bd5nfbiv-WloZR3ZjepoUTv28SI1ezw).  A community-driven [Clio Developers Stack Overflow Group](https://stackoverflow.com/questions/tagged/clio-api) also exists where you can connect and ask questions from other Clio API users. # Getting Started > **Note:** The API is available in four distinct data regions: Australia (au.app.clio.com), Canada (ca.app.clio.com), EU (eu.app.clio.com) and US (app.clio.com). > > Likewise, the developer portal is available at region-specific links for the [Australia](https://au.developers.clio.com), [Canada](https://ca.developers.clio.com), [EU](https://eu.developers.clio.com), and [US](https://developers.clio.com) regions. > > This document assumes the US region is being used (app.clio.com). If you're building in one of the other regions, you should adapt the links and examples as necessary.  To start building on the Clio API, you’ll need a Clio account – you can review our [Developer Handbook](https://docs.developers.clio.com/) and follow the steps to sign up for an account.  Once you have an account, you can [create a developer application](https://docs.developers.clio.com/api-docs/applications) from the [Developer Portal](https://developers.clio.com) and start building! # Authorization with OAuth 2.0 See our [Authorization documentation →](https://docs.developers.clio.com/api-docs/authorization) # Permissions See our [Permissions documentation →](https://docs.developers.clio.com/api-docs/permissions) # Fields See our [Fields documentation →](https://docs.developers.clio.com/api-docs/fields) # Rate Limiting See our [Rate Limits documentation →](https://docs.developers.clio.com/api-docs/rate-limits) # Paging See our [Pagination documentation →](https://docs.developers.clio.com/api-docs/paging) # ETags See our [ETags documentation →](https://docs.developers.clio.com/api-docs/etags) # Minor Versions API v4 supports multiple minor versions. Versions are of the form '4.X.Y'. To request a specific version, you can use an `X-API-VERSION` header in your request, with the header value set to the API version you're requesting. If this header is omitted, it will be treated as a request for the default API version. If the header is present but invalid, it will return a `410 Gone` response. If the header is present and valid, but it is no longer supported, it will return a `410 Gone` response.  An `X-API-VERSION` will be included in all successful responses, with the value being set to the API version used.  You can find our [API Versioning Policy and Guidelines](https://docs.developers.clio.com/api-docs/api-versioning-policy) in our documentation hub.  The [API Changelog](https://docs.developers.clio.com/api-docs/api-changelog) explains each version's changes in further detail. - 4.0.4    Update `quantity` field to return values in seconds rather than hours for Activities  - 4.0.5    * Remove `matter_balances` field from Bills   * Standardize status/state enum values   * Add a Document association to completed DocumentAutomations   * Add rate visibility handling for Activity's price and total  - 4.0.6    Remove `document_versions` collection field from Documents  - 4.0.7    Change secure link format  - 4.0.8    * `Activity` hours are redacted in the response based on the activity hours visibility setting for the user   * Add `quantity_redacted` field to activities  - 4.0.9    **This is the default version**    Contacts are filtered and redacted in the response based on the new 'Contacts Visibility' user permission setting.  - 4.0.10    Fixed validation of `type` query parameter when querying Notes   

    The version of the OpenAPI document: v4
    Contact: api@clio.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.address_base import AddressBase
from openapi_client.models.balance_base import BalanceBase
from openapi_client.models.bank_account_base import BankAccountBase
from openapi_client.models.bill_base import BillBase
from openapi_client.models.bill_theme_base import BillThemeBase
from openapi_client.models.billing_setting_base import BillingSettingBase
from openapi_client.models.contact_base import ContactBase
from openapi_client.models.currency_base import CurrencyBase
from openapi_client.models.discount_base import DiscountBase
from openapi_client.models.group_base import GroupBase
from openapi_client.models.interest_base import InterestBase
from openapi_client.models.legal_aid_uk_bill_base import LegalAidUkBillBase
from openapi_client.models.matter_balance_base import MatterBalanceBase
from openapi_client.models.matter_base import MatterBase
from openapi_client.models.user_base import UserBase
from typing import Optional, Set
from typing_extensions import Self

class Bill(BaseModel):
    """
    Bill
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the *Bill*")
    etag: Optional[StrictStr] = Field(default=None, description="ETag for the *Bill*")
    number: Optional[StrictStr] = Field(default=None, description="The *Bill* identifier (not necessarily numeric)'")
    issued_at: Optional[date] = Field(default=None, description="The time the *Bill* was issued (as a ISO-8601 date)")
    created_at: Optional[datetime] = Field(default=None, description="The time the *Bill* was created (as a ISO-8601 timestamp)")
    due_at: Optional[date] = Field(default=None, description="The date the *Bill* is due (as a ISO-8601 date)")
    tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The tax rate to the *Bill*")
    secondary_tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A secondary tax rate applied to the *Bill*")
    updated_at: Optional[datetime] = Field(default=None, description="The time the *Bill* was last updated (as a ISO-8601 timestamp)")
    subject: Optional[StrictStr] = Field(default=None, description="The subject of the *Bill*")
    purchase_order: Optional[StrictStr] = Field(default=None, description="The purchase order of the *Bill*")
    type: Optional[StrictStr] = Field(default=None, description="The type of the *Bill*")
    memo: Optional[StrictStr] = Field(default=None, description="A memo for the *Bill*")
    start_at: Optional[date] = Field(default=None, description="The time the billing period starts (as a ISO-8601 date)")
    end_at: Optional[date] = Field(default=None, description="The time the billing period ends (as a ISO-8601 date)")
    balance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The outstanding balance of the *Bill*")
    state: Optional[StrictStr] = Field(default=None, description="The billing state the *Bill* is in")
    kind: Optional[StrictStr] = Field(default=None, description="The kind of the *Bill*")
    total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total with interest of the *Bill*")
    paid: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount paid for the *Bill*")
    paid_at: Optional[datetime] = Field(default=None, description="The date of the last payment on the *Bill*")
    pending: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of pending credit card payments on the *Bill*")
    due: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount of the *Bill* with interest and less discounts")
    discount_services_only: Optional[StrictStr] = Field(default=None, description="The selected discount is applied to services only.")
    can_update: Optional[StrictBool] = Field(default=None, description="This value indicates if your *Bill*'s line items and information can be updated.")
    credits_issued: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total credits issued for the *Bill*")
    shared: Optional[StrictBool] = Field(default=None, description="Whether the *Bill* is a shared")
    last_sent_at: Optional[datetime] = Field(default=None, description="The last time the *Bill* was sent (as a ISO-8601 date)")
    services_secondary_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total secondary tax of the bill's line items of a service kind")
    services_sub_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The sub total of all the bill's line items of a service kind")
    services_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total tax of the bill's line items of a service kind")
    services_taxable_sub_total: Optional[StrictInt] = Field(default=None, description="The services portion of the bill's primary tax")
    services_secondary_taxable_sub_total: Optional[StrictInt] = Field(default=None, description="The services portion of the bill's secondary tax")
    taxable_sub_total: Optional[StrictInt] = Field(default=None, description="The total taxable bill amount")
    secondary_taxable_sub_total: Optional[StrictInt] = Field(default=None, description="The subtotal of the bill's secondary tax")
    sub_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Sub total for the *Bill*")
    tax_sum: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Sum of primary tax for the model")
    secondary_tax_sum: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Sum of secondary tax for the model")
    total_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount of tax for the bill.")
    available_state_transitions: Optional[List[StrictStr]] = Field(default=None, description="The available *Bill* state transitions.")
    user: Optional[UserBase] = None
    client: Optional[ContactBase] = None
    discount: Optional[DiscountBase] = None
    interest: Optional[InterestBase] = None
    matters: Optional[List[MatterBase]] = Field(default=None, description="Matter")
    group: Optional[GroupBase] = None
    bill_theme: Optional[BillThemeBase] = None
    original_bill: Optional[BillBase] = None
    destination_account: Optional[BankAccountBase] = None
    balances: Optional[List[BalanceBase]] = Field(default=None, description="Balance")
    matter_totals: Optional[List[MatterBalanceBase]] = Field(default=None, description="MatterBalance")
    currency: Optional[CurrencyBase] = None
    billing_setting: Optional[BillingSettingBase] = None
    client_addresses: Optional[List[AddressBase]] = Field(default=None, description="Address")
    legal_aid_uk_bill: Optional[LegalAidUkBillBase] = None
    __properties: ClassVar[List[str]] = ["id", "etag", "number", "issued_at", "created_at", "due_at", "tax_rate", "secondary_tax_rate", "updated_at", "subject", "purchase_order", "type", "memo", "start_at", "end_at", "balance", "state", "kind", "total", "paid", "paid_at", "pending", "due", "discount_services_only", "can_update", "credits_issued", "shared", "last_sent_at", "services_secondary_tax", "services_sub_total", "services_tax", "services_taxable_sub_total", "services_secondary_taxable_sub_total", "taxable_sub_total", "secondary_taxable_sub_total", "sub_total", "tax_sum", "secondary_tax_sum", "total_tax", "available_state_transitions", "user", "client", "discount", "interest", "matters", "group", "bill_theme", "original_bill", "destination_account", "balances", "matter_totals", "currency", "billing_setting", "client_addresses", "legal_aid_uk_bill"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MatterBill', 'ClientBill']):
            raise ValueError("must be one of enum values ('MatterBill', 'ClientBill')")
        return value

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['draft', 'awaiting_approval', 'awaiting_payment', 'paid', 'void', 'deleted']):
            raise ValueError("must be one of enum values ('draft', 'awaiting_approval', 'awaiting_payment', 'paid', 'void', 'deleted')")
        return value

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['revenue_kind', 'summary_kind', 'trust_kind', 'aggregate_all', 'aggregate_split', 'aggregate_services', 'aggregate_expenses']):
            raise ValueError("must be one of enum values ('revenue_kind', 'summary_kind', 'trust_kind', 'aggregate_all', 'aggregate_split', 'aggregate_services', 'aggregate_expenses')")
        return value

    @field_validator('available_state_transitions')
    def available_state_transitions_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['awaiting_approval', 'awaiting_payment', 'paid', 'void', 'deleted']):
                raise ValueError("each list item must be one of ('awaiting_approval', 'awaiting_payment', 'paid', 'void', 'deleted')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Bill from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client
        if self.client:
            _dict['client'] = self.client.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount
        if self.discount:
            _dict['discount'] = self.discount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interest
        if self.interest:
            _dict['interest'] = self.interest.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in matters (list)
        _items = []
        if self.matters:
            for _item_matters in self.matters:
                if _item_matters:
                    _items.append(_item_matters.to_dict())
            _dict['matters'] = _items
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bill_theme
        if self.bill_theme:
            _dict['bill_theme'] = self.bill_theme.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original_bill
        if self.original_bill:
            _dict['original_bill'] = self.original_bill.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination_account
        if self.destination_account:
            _dict['destination_account'] = self.destination_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in balances (list)
        _items = []
        if self.balances:
            for _item_balances in self.balances:
                if _item_balances:
                    _items.append(_item_balances.to_dict())
            _dict['balances'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in matter_totals (list)
        _items = []
        if self.matter_totals:
            for _item_matter_totals in self.matter_totals:
                if _item_matter_totals:
                    _items.append(_item_matter_totals.to_dict())
            _dict['matter_totals'] = _items
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_setting
        if self.billing_setting:
            _dict['billing_setting'] = self.billing_setting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in client_addresses (list)
        _items = []
        if self.client_addresses:
            for _item_client_addresses in self.client_addresses:
                if _item_client_addresses:
                    _items.append(_item_client_addresses.to_dict())
            _dict['client_addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of legal_aid_uk_bill
        if self.legal_aid_uk_bill:
            _dict['legal_aid_uk_bill'] = self.legal_aid_uk_bill.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Bill from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "etag": obj.get("etag"),
            "number": obj.get("number"),
            "issued_at": obj.get("issued_at"),
            "created_at": obj.get("created_at"),
            "due_at": obj.get("due_at"),
            "tax_rate": obj.get("tax_rate"),
            "secondary_tax_rate": obj.get("secondary_tax_rate"),
            "updated_at": obj.get("updated_at"),
            "subject": obj.get("subject"),
            "purchase_order": obj.get("purchase_order"),
            "type": obj.get("type"),
            "memo": obj.get("memo"),
            "start_at": obj.get("start_at"),
            "end_at": obj.get("end_at"),
            "balance": obj.get("balance"),
            "state": obj.get("state"),
            "kind": obj.get("kind"),
            "total": obj.get("total"),
            "paid": obj.get("paid"),
            "paid_at": obj.get("paid_at"),
            "pending": obj.get("pending"),
            "due": obj.get("due"),
            "discount_services_only": obj.get("discount_services_only"),
            "can_update": obj.get("can_update"),
            "credits_issued": obj.get("credits_issued"),
            "shared": obj.get("shared"),
            "last_sent_at": obj.get("last_sent_at"),
            "services_secondary_tax": obj.get("services_secondary_tax"),
            "services_sub_total": obj.get("services_sub_total"),
            "services_tax": obj.get("services_tax"),
            "services_taxable_sub_total": obj.get("services_taxable_sub_total"),
            "services_secondary_taxable_sub_total": obj.get("services_secondary_taxable_sub_total"),
            "taxable_sub_total": obj.get("taxable_sub_total"),
            "secondary_taxable_sub_total": obj.get("secondary_taxable_sub_total"),
            "sub_total": obj.get("sub_total"),
            "tax_sum": obj.get("tax_sum"),
            "secondary_tax_sum": obj.get("secondary_tax_sum"),
            "total_tax": obj.get("total_tax"),
            "available_state_transitions": obj.get("available_state_transitions"),
            "user": UserBase.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "client": ContactBase.from_dict(obj["client"]) if obj.get("client") is not None else None,
            "discount": DiscountBase.from_dict(obj["discount"]) if obj.get("discount") is not None else None,
            "interest": InterestBase.from_dict(obj["interest"]) if obj.get("interest") is not None else None,
            "matters": [MatterBase.from_dict(_item) for _item in obj["matters"]] if obj.get("matters") is not None else None,
            "group": GroupBase.from_dict(obj["group"]) if obj.get("group") is not None else None,
            "bill_theme": BillThemeBase.from_dict(obj["bill_theme"]) if obj.get("bill_theme") is not None else None,
            "original_bill": BillBase.from_dict(obj["original_bill"]) if obj.get("original_bill") is not None else None,
            "destination_account": BankAccountBase.from_dict(obj["destination_account"]) if obj.get("destination_account") is not None else None,
            "balances": [BalanceBase.from_dict(_item) for _item in obj["balances"]] if obj.get("balances") is not None else None,
            "matter_totals": [MatterBalanceBase.from_dict(_item) for _item in obj["matter_totals"]] if obj.get("matter_totals") is not None else None,
            "currency": CurrencyBase.from_dict(obj["currency"]) if obj.get("currency") is not None else None,
            "billing_setting": BillingSettingBase.from_dict(obj["billing_setting"]) if obj.get("billing_setting") is not None else None,
            "client_addresses": [AddressBase.from_dict(_item) for _item in obj["client_addresses"]] if obj.get("client_addresses") is not None else None,
            "legal_aid_uk_bill": LegalAidUkBillBase.from_dict(obj["legal_aid_uk_bill"]) if obj.get("legal_aid_uk_bill") is not None else None
        })
        return _obj


