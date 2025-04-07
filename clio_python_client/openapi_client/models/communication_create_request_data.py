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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.communication_create_request_data_external_properties_inner import CommunicationCreateRequestDataExternalPropertiesInner
from openapi_client.models.communication_create_request_data_matter import CommunicationCreateRequestDataMatter
from openapi_client.models.communication_create_request_data_notification_event_subscribers_inner import CommunicationCreateRequestDataNotificationEventSubscribersInner
from openapi_client.models.communication_create_request_data_receivers_inner import CommunicationCreateRequestDataReceiversInner
from openapi_client.models.communication_create_request_data_senders_inner import CommunicationCreateRequestDataSendersInner
from typing import Optional, Set
from typing_extensions import Self

class CommunicationCreateRequestData(BaseModel):
    """
    CommunicationCreateRequestData
    """ # noqa: E501
    body: StrictStr = Field(description="The body value.")
    var_date: Optional[StrictStr] = Field(default=None, description="The date for the Communication. (Expects an ISO-8601 date.)", alias="date")
    external_properties: Optional[List[CommunicationCreateRequestDataExternalPropertiesInner]] = None
    matter: Optional[CommunicationCreateRequestDataMatter] = None
    notification_event_subscribers: Optional[List[CommunicationCreateRequestDataNotificationEventSubscribersInner]] = None
    received_at: Optional[StrictStr] = Field(default=None, description="The date-time for the Communication. (Expects an ISO-8601 date-time.)")
    receivers: Optional[List[CommunicationCreateRequestDataReceiversInner]] = None
    senders: Optional[List[CommunicationCreateRequestDataSendersInner]] = None
    subject: StrictStr = Field(description="The subject value.")
    type: StrictStr = Field(description="Type of the Communication.")
    __properties: ClassVar[List[str]] = ["body", "date", "external_properties", "matter", "notification_event_subscribers", "received_at", "receivers", "senders", "subject", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PhoneCommunication', 'EmailCommunication']):
            raise ValueError("must be one of enum values ('PhoneCommunication', 'EmailCommunication')")
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
        """Create an instance of CommunicationCreateRequestData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in external_properties (list)
        _items = []
        if self.external_properties:
            for _item_external_properties in self.external_properties:
                if _item_external_properties:
                    _items.append(_item_external_properties.to_dict())
            _dict['external_properties'] = _items
        # override the default output from pydantic by calling `to_dict()` of matter
        if self.matter:
            _dict['matter'] = self.matter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notification_event_subscribers (list)
        _items = []
        if self.notification_event_subscribers:
            for _item_notification_event_subscribers in self.notification_event_subscribers:
                if _item_notification_event_subscribers:
                    _items.append(_item_notification_event_subscribers.to_dict())
            _dict['notification_event_subscribers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in receivers (list)
        _items = []
        if self.receivers:
            for _item_receivers in self.receivers:
                if _item_receivers:
                    _items.append(_item_receivers.to_dict())
            _dict['receivers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in senders (list)
        _items = []
        if self.senders:
            for _item_senders in self.senders:
                if _item_senders:
                    _items.append(_item_senders.to_dict())
            _dict['senders'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommunicationCreateRequestData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "body": obj.get("body"),
            "date": obj.get("date"),
            "external_properties": [CommunicationCreateRequestDataExternalPropertiesInner.from_dict(_item) for _item in obj["external_properties"]] if obj.get("external_properties") is not None else None,
            "matter": CommunicationCreateRequestDataMatter.from_dict(obj["matter"]) if obj.get("matter") is not None else None,
            "notification_event_subscribers": [CommunicationCreateRequestDataNotificationEventSubscribersInner.from_dict(_item) for _item in obj["notification_event_subscribers"]] if obj.get("notification_event_subscribers") is not None else None,
            "received_at": obj.get("received_at"),
            "receivers": [CommunicationCreateRequestDataReceiversInner.from_dict(_item) for _item in obj["receivers"]] if obj.get("receivers") is not None else None,
            "senders": [CommunicationCreateRequestDataSendersInner.from_dict(_item) for _item in obj["senders"]] if obj.get("senders") is not None else None,
            "subject": obj.get("subject"),
            "type": obj.get("type")
        })
        return _obj


