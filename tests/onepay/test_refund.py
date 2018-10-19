import unittest
import unittest.mock

import requests_mock
import re

from transbank import onepay

from transbank.onepay import Options
from transbank.onepay.refund import Refund, RefundCreateRequest, RefundCreateResponse
from transbank.onepay.error import RefundCreateError, SignError

class RefundTestCase(unittest.TestCase):

    external_unique_number_test = "f506a955-800c-4185-8818-4ef9fca97aae"
    occ_commit_test = "1807829988419927"
    shared_secret_mock = "P4DCPS55QB2QLT56SQH6#W#LV76IAPYX"
    api_key_mock = "mUc0GxYGor6X8u-_oB3e-HWJulRG01WoC96-_tUA3Bg"
    auth_code_test = "623245"

    def setUp(self):
        onepay.integration_type = onepay.IntegrationType.MOCK
        onepay.api_key = self.api_key_mock
        onepay.shared_secret = self.shared_secret_mock

    def test_get_signable_elements(self):
        RefundCreateRequest(1, 1000, 1, 100, None)
        request = RefundCreateRequest(1,1000,1, 100, 100, None)
        self.assertEqual(request.signable_data(), [1, 1000, 1, 100, 100])

    def test_raise_error_response_create_refund(self):
        with requests_mock.Mocker() as m:
            m.register_uri("POST", re.compile("/nullifytransaction"), text="{\"response_code\": \"ERROR\", \"description\": \"ERROR\"}")
            with self.assertRaisesRegex(RefundCreateError, "ERROR : ERROR"):
                Refund.create(1000,1000,1000, 1000)

    def test_create_refund_global_options(self):
        response = Refund.create(27500, self.occ_commit_test, self.external_unique_number_test, self.auth_code_test)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.occ)
        self.assertIsNotNone(response.signature)
        self.assertIsNotNone(response.reverse_code)
        self.assertIsNotNone(response.external_unique_number)
        self.assertIsNotNone(response.issued_at)

    def test_create_refund_given_options(self):
        onepay.api_key = None
        onepay.shared_secret = None
        options = Options(self.api_key_mock, self.shared_secret_mock)
        response = Refund.create(27500, self.occ_commit_test, self.external_unique_number_test, self.auth_code_test, options)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.occ)
        self.assertIsNotNone(response.signature)
        self.assertIsNotNone(response.reverse_code)
        self.assertIsNotNone(response.external_unique_number)
        self.assertIsNotNone(response.issued_at)
