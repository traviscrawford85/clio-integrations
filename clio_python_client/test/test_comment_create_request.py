# coding: utf-8

"""
    Clio API Documentation

    # Developer Support and Feedback * Clio takes the availability and stability of our API seriously; please report any **degradations** or **breakages** to Clio's API Support team at [api@clio.com](mailto:api@clio.com). * For business and partnership inquiries, contact our API Partnerships team at [api.partnerships@clio.com](mailto:api.partnerships@clio.com). * For best practices and tips from the Clio development community, join the conversation in the [Clio Developer Slack Channel](https://join.slack.com/t/clio-public/shared_invite/zt-1bd5nfbiv-WloZR3ZjepoUTv28SI1ezw).  A community-driven [Clio Developers Stack Overflow Group](https://stackoverflow.com/questions/tagged/clio-api) also exists where you can connect and ask questions from other Clio API users. # Getting Started > **Note:** The API is available in four distinct data regions: Australia (au.app.clio.com), Canada (ca.app.clio.com), EU (eu.app.clio.com) and US (app.clio.com). > > Likewise, the developer portal is available at region-specific links for the [Australia](https://au.developers.clio.com), [Canada](https://ca.developers.clio.com), [EU](https://eu.developers.clio.com), and [US](https://developers.clio.com) regions. > > This document assumes the US region is being used (app.clio.com). If you're building in one of the other regions, you should adapt the links and examples as necessary.  To start building on the Clio API, you’ll need a Clio account – you can review our [Developer Handbook](https://docs.developers.clio.com/) and follow the steps to sign up for an account.  Once you have an account, you can [create a developer application](https://docs.developers.clio.com/api-docs/applications) from the [Developer Portal](https://developers.clio.com) and start building! # Authorization with OAuth 2.0 See our [Authorization documentation →](https://docs.developers.clio.com/api-docs/authorization) # Permissions See our [Permissions documentation →](https://docs.developers.clio.com/api-docs/permissions) # Fields See our [Fields documentation →](https://docs.developers.clio.com/api-docs/fields) # Rate Limiting See our [Rate Limits documentation →](https://docs.developers.clio.com/api-docs/rate-limits) # Paging See our [Pagination documentation →](https://docs.developers.clio.com/api-docs/paging) # ETags See our [ETags documentation →](https://docs.developers.clio.com/api-docs/etags) # Minor Versions API v4 supports multiple minor versions. Versions are of the form '4.X.Y'. To request a specific version, you can use an `X-API-VERSION` header in your request, with the header value set to the API version you're requesting. If this header is omitted, it will be treated as a request for the default API version. If the header is present but invalid, it will return a `410 Gone` response. If the header is present and valid, but it is no longer supported, it will return a `410 Gone` response.  An `X-API-VERSION` will be included in all successful responses, with the value being set to the API version used.  You can find our [API Versioning Policy and Guidelines](https://docs.developers.clio.com/api-docs/api-versioning-policy) in our documentation hub.  The [API Changelog](https://docs.developers.clio.com/api-docs/api-changelog) explains each version's changes in further detail. - 4.0.4    Update `quantity` field to return values in seconds rather than hours for Activities  - 4.0.5    * Remove `matter_balances` field from Bills   * Standardize status/state enum values   * Add a Document association to completed DocumentAutomations   * Add rate visibility handling for Activity's price and total  - 4.0.6    Remove `document_versions` collection field from Documents  - 4.0.7    Change secure link format  - 4.0.8    * `Activity` hours are redacted in the response based on the activity hours visibility setting for the user   * Add `quantity_redacted` field to activities  - 4.0.9    **This is the default version**    Contacts are filtered and redacted in the response based on the new 'Contacts Visibility' user permission setting.  - 4.0.10    Fixed validation of `type` query parameter when querying Notes   

    The version of the OpenAPI document: v4
    Contact: api@clio.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.comment_create_request import CommentCreateRequest

class TestCommentCreateRequest(unittest.TestCase):
    """CommentCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommentCreateRequest:
        """Test CommentCreateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommentCreateRequest`
        """
        model = CommentCreateRequest()
        if include_optional:
            return CommentCreateRequest(
                data = openapi_client.models.comment_create_request_data.Comment_create_request_data(
                    item = openapi_client.models.comment_create_request_data_item.Comment_create_request_data_item(
                        id = 56, ), 
                    message = '', )
            )
        else:
            return CommentCreateRequest(
                data = openapi_client.models.comment_create_request_data.Comment_create_request_data(
                    item = openapi_client.models.comment_create_request_data_item.Comment_create_request_data_item(
                        id = 56, ), 
                    message = '', ),
        )
        """

    def testCommentCreateRequest(self):
        """Test CommentCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
